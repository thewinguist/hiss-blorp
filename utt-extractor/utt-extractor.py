import json
import os
import re
import csv

# def prepare_input(operation, locale)

def extract_utts(selected_locale, dir):
    rows = []
    for filename in os.listdir(dir):
        f = os.path.join(dir, filename)
        # to exclude subdirs (currently 1):
        if os.path.isfile(f):
            with open(f, "r", encoding='UTF-8') as json_file:
                grammars = json.load(json_file)['grammars']
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
                            #print(params_dict)
                            param_slots = re.findall('#{([^}]*)}', utt)
                            for slot in param_slots:
                                slot_padded = '#{'+ slot +'}'
                                utt = utt.replace(slot_padded, params_dict[slot])
                            #rows.append(f + "\t" + str(utt_no)+ "\t" + utt +  "\t" + utt_record["utterance"])
                            rows.append([filename, str(utt_no), utt, utt_record["utterance"]])
    return(sorted(rows))
           
# def export_rows(rows):
#     with open('sample.csv', 'w') as f:
#         # adds a header before everything else
#         rows.insert(0, ['filename', 'utt number', 'utt filled', 'utt with gaps'])
#         csv.writer(f, delimiter=',').writerows(rows)

def import_rows(filepath: str):
        rows = []
        with open(filepath, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            #skip the csv header:
            next(reader, None)
            for row in reader:
                #restore utt numbering from 0 and remove column [2] of human-friendly utts
                row = [row[0], int(row[1])-1, row[3]]
                rows += [row]
            rows = sorted(rows)
            rows_by_intent = {}
            #group utts by intent as dict values
            current_intent = None
            for row in rows:
                intent = row[0]
                if intent != current_intent:
                    current_intent = intent
                    rows_by_intent[current_intent] = []
                rows_by_intent[current_intent].append(row[1:])

            return(rows_by_intent)

def import_utts(utts_by_intent: dict, dir: str):
    for intent in utts_by_intent:
        #print(key, "->", utts_by_intent[key])
        if intent in os.listdir(dir):
            print("it's a match! - " + intent)

if __name__ == "__main__":
    locale = "fr-FR" #just 1 string pls
    dir = './sample-dir'
    #rows = extract_utts('fr-FR', DIR)
    # export_rows(rows)
    utts_by_intent = import_rows('sample.csv')
    import_utts(utts_by_intent, dir)