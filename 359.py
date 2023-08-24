words = ["alice","oboob","charlie"]
s = "abcde"

def is_acronym (words, s):
    if len(words) != len(s):
        return False
    else:
        if ''.join([x[0] for x in words]) == s:
            return True
        else: return False
        
print(is_acronym(words, s))

#efficient solution ffr:
result = ""
for i in words:
    result = result + i[0]
    if result == s:
        print("uhuh")#returnTrue 
    else:
        print("uh-uh")#returnFalse