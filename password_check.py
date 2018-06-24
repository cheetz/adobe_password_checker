#!/usr/bin/env python
#Quick Script to Check for Password Hash/Hint Matches
#Combined list hint+passwords from:
#https://github.com/morontt/symfobrute/blob/master/adobe-top100.txt
#http://web.mit.edu/zyan/Public/adobe_sanitized_passwords_with_bad_hints.txt

hashcheck = open('hashlist.txt','r')
hashlist = open('foundpw.csv','r')

hashcheck_list = []

for x in hashcheck:
    x = x.strip()
    x = x.split('-|-')
    try:
        hashcheck_list.append(x[2]+","+x[3])
    except:
        pass
for y in hashlist:
    for x in hashcheck_list:
        hash_split = x.split(',')
        if hash_split[1]:
            if hash_split[1] in y.strip():
                print "Matches[+]: " + hash_split[0] + " : " + y.strip() 

