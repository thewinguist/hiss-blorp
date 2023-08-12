s = "stringifier"

#string
#rtsng

#stringi
#rtsngi
#strgn

#stringifier
#rtsngifier
#gnstrfier
#frtsnger

# j = -1
# for char in s:
#     j += 1
#     if char == 'i':
#         #s = s[j-1::-1] + '*' + s[j+1:]
#         #Y U NO WORK?
#         s = s[j-1::-1] + s[j+1:]
# print(s)

result = ""
for char in s:
    if char == "i":
        #reverse already accumulated result
        result = result[::-1]
        continue
    #add new char that isn't "i"
    result += char
print(result)
