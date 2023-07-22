#!/usr/bin/python3

str1 = 'leArning is hard, bUt if You appLy youRself ' \
    'you can achieVe success'

new = []
final = []
for i in str1.split():
    for j in range(len(i)):
        if i[j].isupper():
            new.append(i)
for i in new:
    final.append(i[:: -1])

print(final)
