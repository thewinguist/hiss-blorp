import json
import os
import re

LOCALE = "fr-FR" #just 1 string pls
DIR = './sample-dir/'

for (root, directories, files) in os.walk(DIR):
    for file in sorted(files):
        file = DIR + file
        with open(file, "r", encoding='UTF-8') as json_file:
            grammars = json.load(json_file)['grammars']

        filename = os.path.basename(json_file.name)
        #print('-----------' + filename + '-----------')

        utt_no = 0
        for group in grammars:
            for d in group["data"]:
                if d["locale"] == LOCALE:
                    utt_no += 1
                    utt = d["utterance"]
                    #print(str(utt_no)+".\n" + utt)
                    params_dict = dict()
                    for param in d["params"]:
                        param_values = list(param.values())
                        param_pair = {str(param_values[0]): param_values[1]}
                        params_dict.update(param_pair)
                    #print(params_dict)
                    param_slots = re.findall('#{([^}]*)}', utt)
                    #print(param_slots)
                    for ps in param_slots:
                        ps_padded = '#{'+ ps +'}'
                        #re.search(ps_padded)
                        utt = utt.replace(ps_padded, params_dict[ps])
                    #print(utt)
                    row = filename + "\t" + str(utt_no)+ "\t" + utt +  "\t" + d["utterance"]
                    print(row)
    break #prevents os.walk() from another iteration = looking into a subdir and throwing error