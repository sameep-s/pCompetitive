t= int(input(''))

for i in range(t):
#These are the variables.
    i1 = 0
    i2 = 0
    stra = input('')
    strb = input('')
    deletions = 0
    acount = dict()
    bcount = dict()

#here we store each word into individual letter count.
    for letter in stra:
        letter = stra[i1]
#        print(letter)
        acount[letter] = acount.get(letter, 0) + 1
        i1 = i1 + 1
    for letter in strb:
        letter = strb[i2]
        bcount[letter] = bcount.get(letter, 0) + 1
        i2 = i2 + 1

 #For compairing   
    for d in range(97, 126):
        if chr(d) in acount and chr(d) in bcount:
            if acount[chr(d)] != bcount[chr(d)]:
                deletions = deletions + abs(acount[chr(d)] - bcount[chr(d)])
        elif chr(d) in acount:
            deletions = deletions + acount[chr(d)]
        elif chr(d) in bcount:
            deletions = deletions + bcount[chr(d)]
    
    print('The number of letters to be deleted are: ',deletions)

    































'''
#very easy sample code
t = int(input())
for i in range(t):
    a = input()
    b = input()
    c = 0
    for i in range(97,123):
        first = a.count(chr(i))
        second = b.count(chr(i))
        c = c+abs(first-second)
    print('c', c)
'''