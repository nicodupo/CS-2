''''
name: Nico DuPont
description: this code sorts the words in a speach and counts ammount of difference words
log:  dictionary 1.0
sources: stackoverflow.com
'''
import csv 
import re #specifies a set of strings that match it
import string 
counts = dict() #creates an empty dictionary 
unnecessary_words = ['a', 'an','is','of','in', 'for', 'our','to','too','that','because','I', 'we', 'will', 'he', 'are', 'and', 'with', 'we', 'my', 'not', 'who', 'and','on','have', 'this','was','their','has','been','from','be','it','you','going','so','they','at','all','the','by','your','the'] #list of words that are not necessary to be printed
fhand = open('trump.txt') #opens the text file into your code
for line in fhand: #for loop for ammount of lines
    print('Line Count:', counts) #it returns your line count and puts in counts 
    words = line.split() #makes a list called words that includes every word as a seperate item
    line = line.lower() #makes all characters lowercase
    for word in words: #for words in the speech 
        word = re.sub(r'[^\w\s]', '',word) #removes unwanted punctuation and puts in back into word
        if word in unnecessary_words: #if the word in the the unnecessary words list
            continue #continue over it
        elif word not in counts: #if the word is not in the dctionary already
            counts[word] = 1 #put it in dictionary if it is not yet
        else: #if its already in the dictionary
            counts[word] += 1 #add one to word count


sorted_dict = dict(sorted(counts.items(), key=lambda item:item[1], reverse = True)) #sets sorted dictionary equal to the sorted version of the dictionary counts with in decending order
counter = 0 #sets counter to begin at 1
with open('dict.csv', 'w') as csv_file:  #allows you to open word count in sheets 
    writer = csv.writer(csv_file) #converts user data into delimiting string
    for key, value in sorted_dict.items(): #for loop for key and value pair
        if value >= 10 and counter <= 10: #if value is over ten make it print in the cvs
           counter += 1 #adds one to word count value
           writer.writerow([key, value]) #creating a row and writing to it

       