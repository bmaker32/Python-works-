from difflib import get_close_matches
import json


x=open('./data.json')
dic=json.load(x)

exit=False

def output(word):
    if word==None:
        print("not found in the dictionary")
    else:
        if type(word)==list:
            for item in word:
                print(item,end="\n-")
        else:
            print(word)

def if_exist(word):
    word=word.lower()
    if word in dic:
        return dic[word]
    elif word.title() in dic:
        return dic[word.title()]
    elif word.upper() in dic:
        return dic[word.upper()]
            
while exit==False:
    to_se=input("Enter the search: ")

    output(if_exist(to_se)) #checks whether the word is in the dictionary and fetch the data 
    print("close matches ", get_close_matches(to_se,dic.keys(),5))
    x=input("to exit press 0 ")
    if x=="0":
        exit=True
