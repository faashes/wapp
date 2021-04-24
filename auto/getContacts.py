"""
Instruction for use:

1) inspect element on whatsapp group
2) go to title of group where you can see the contacts, inspect, get string of numbers in text format as given below
3) run the program, you will have a suitable list of numbers then.
"""
text = '+91 712224 1384, +91 74482 79912, +91 81080 00038, +91 86230 45977, +91 91759 44475, +91 93731 02765, +91 94048 95480, +91 94228 28416, +91 94239 78455, +91 96895 52056, +91 98196 97838, +91 98200 59580, +91 98220 52661, +91 98225 55279, +91 98230 66222, +91 98347 71371, +91 98499 81761, +91 98675 67567, +91 98900 36009, +91 99220 18370, +91 99231 75886, +91 99232 05886, +91 99606 54441, +91 99701 29198'
test = text.split(',')

print(test)

pno = []

for t in test:
    t = t.split()
    t.pop(0)
    t= t[0] + t[1]
    pno.append(t)

str1 = ''

for p in pno:
    str1 = str1 + p + ','

print(str1)

