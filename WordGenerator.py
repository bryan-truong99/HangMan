import random
import csv

with open(r"C:\Users\bryan\Documents\Python\HangMan\words.csv",newline='') as f:
    reader=csv.reader(f)
    words=list(reader)

print(words)
