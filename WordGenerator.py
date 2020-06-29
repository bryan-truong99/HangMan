import random
import csv

def word_gen(min):
    if min<4 or min>16:
        raise IndexError("Please choose a number \
        greater than 3 and less than 17")
    #Open CSV file and convert it to a list
    with open(r"C:\Users\bryan\Documents\Python\HangMan\words.csv",newline='') as f:
        reader=csv.reader(f)
        words=list(reader)

    #Find index and store words in temp array
    index=min-4
    temp=[]
    for word in words[index:]:
        temp.append(word)

    #Pick a random item in the array
    temp=random.choice(temp)
    temp=random.choice(temp)

    return temp
