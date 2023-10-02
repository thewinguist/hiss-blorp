import argparse
import json
import os
import re
import csv

def prepare_input():
    p = argparse.ArgumentParser()
    p.add_argument("--target","-t", required=True,
                   choices=["csv", "json"],
                   help="The target can be either \"csv\" to export utterances from intents to .csv,\
                   or \"json\" to re-import the utterances with your edits from \"utts-xx-XX.csv\".")
    p.add_argument("--language","-l", required=True,
                   choices=["de", "fr", "it", "es"],
                   help="Type \"de\", \"fr\", \"it\", or \"es\",\
                    the region will be completed.")
    args = p.parse_args()
    target_format = str(args.target)
    selected_locale = f"{args.language}-{args.language.upper()}"
    csv_file = f"{data_dir}/utts-{selected_locale}.csv"
    return target_format, selected_locale, csv_file

def extract_utts(intent_dir, selected_locale):
    rows = []
    for filename in os.listdir(intent_dir):
        f = os.path.join(intent_dir, filename)
        # to exclude the subdir:
        if os.path.isfile(f):
            with open(f, "r", encoding="UTF-8") as json_file:
                grammars = json.load(json_file)["grammars"]
                utt_no = 0
                for group in grammars:
                    for utt_record in group["data"]:
                        if utt_record["locale"] == selected_locale:
                            utt_no += 1
                            utt = utt_record["utterance"]
                            params_dict = dict()
                            for param in utt_record["params"]:
                                param_values = list(param.values())
                                param_pair = {str(param_values[0]): param_values[1]}
                                params_dict.update(param_pair)
                            param_slots = re.findall("#{([^}]*)}", utt)
                            for slot in param_slots:
                                slot_padded = "#{"+ slot +"}"
                                #todo: KeyError here after
                                #python extract_utts.py -t csv -l fr
                                utt = utt.replace(slot_padded, params_dict[slot])
                            rows.append([filename, str(utt_no), utt, utt_record["utterance"]])
    return(sorted(rows))

def export_rows(rows):
    with open(csv_file, "w") as f:
        # adds a header as 1st row
        rows.insert(0, ["filename", "utt number", "utt filled", "utt with gaps"])
        csv.writer(f, delimiter=",").writerows(rows)
        print(f"✓ Great success! {len(rows)-1} utterances exported to {f.name}.")

def import_rows(filepath):
        rows = []
        with open(filepath, "r") as f:
            reader = csv.reader(f, delimiter=",")
            #skip the csv header:
            next(reader, None)
            for row in reader:
                row = [row[0], [int(row[1])-1, row[3]]]
                rows += [row]
            rows = sorted(rows)
            utts_by_intent = {}
            #group utts by intent as dict values
            current_intent = None
            for row in rows:
                intent = row[0]
                if intent != current_intent:
                    current_intent = intent
                    utts_by_intent[current_intent] = []
                utts_by_intent[current_intent] += row[1:]
            return(utts_by_intent)

def embed_utts(utts_by_intent, dir, selected_locale):
    utt_total = 0
    intent_total = 0
    for intent in utts_by_intent:
        intent_total += 1
        f = intent_dir + "/" + intent
        if os.path.isfile(f) == False:
            print(f"⚠ File \"{intent}\" not found in \"{intent_dir}\"")
        else:
            with open(f, "r", encoding="UTF-8") as json_file:
                json_content = json.load(json_file)
                utt_no = 0
                for group in json_content["grammars"]:
                    for utt_record in group["data"]:
                        if utt_record["locale"] == selected_locale:
                            utt_record["utterance"] = utts_by_intent[intent][utt_no][1]
                            utt_no += 1
                            utt_total += 1
            with open(f, "w", encoding="UTF-8") as json_file:
                json.dump(json_content, json_file, ensure_ascii = False, indent = 4)

    print(f"✓ Great success! {utt_total} utterances inserted into {intent_total} json files.")

if __name__ == "__main__":
    intent_dir = "sample-dir"
    data_dir = "."
    if os.listdir(intent_dir) == []:
        print(f"⚠ {intent_dir} is an empty directory. Your csv export would be empty!")
        quit()

    target_format, selected_locale, csv_file = prepare_input()
    if target_format == "csv":
        if os.path.isfile(csv_file) == True:
            print(f"Overwriting \"utts-{selected_locale}.csv\"...")
        else: print(f"Creating \"utts-{selected_locale}.csv\"...")
        export_rows(extract_utts(intent_dir, selected_locale))
    elif target_format == "json":
        if os.path.isfile(csv_file) == False:
            print(f"⚠ \"utts-{selected_locale}.csv\" source file not found. After your edits, the csv file must still be named \"utts-{selected_locale}.csv\" and live in \"data\" dir next to this script (in bhp-intent-resource-data/tools/extractUtterances/data/).")
            quit()
        utts_by_intent = import_rows(csv_file)
        embed_utts(utts_by_intent, intent_dir, selected_locale)