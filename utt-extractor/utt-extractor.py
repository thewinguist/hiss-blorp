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
        utts_by_intent = {}
        with open(filepath, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            #skip the header:
            next(reader, None)
            for row in reader:
                row = [row[0], int(row[1])-1, row[3]]
                utts_by_intent[row[0]] = row[1::]
                print(row)
                
            print(utts_by_intent)
            #sort the dictionary by intent filenames (just in case)
            # filenames = list(utts_by_intent.keys())
            # filenames.sort()
            # utts_by_intent = {i: utts_by_intent[i] for i in filenames}
        # return(utts_by_intent)

# def import_utts(utts_by_intent: dict):
#     for key in utts_by_intent:
#         print(key, "->", utts_by_intent[key])


if __name__ == "__main__":
    LOCALE = "fr-FR" #just 1 string pls
    DIR = '../../intents/'
    #rows = extract_utts('fr-FR', DIR)
    # export_rows(rows)
    import_rows('sample.csv')
    # import_utts(utts_by_intent)