'''
Name: Maddox Monterisi
Date: 2/20/26
Description: creates a data dictionary of the most common words in Macbeth and Romeo and Juliet
Bugs: none
Version 1.0
'''
import string #used to remove punctuation
import matplotlib.pyplot as plt #used to create the pie chart

fname = input('Enter the file name: ')
#prompts user to enter a file name
try:
    fopen = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
#uses a try/except block to prevent crashing if the file cannot be opened
word_counts = dict()
for line in fopen: 
    #reads each line of file
    line = line.rstrip()
    #first two parameters are empty strings
    line = line.translate(line.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    #removes punctuation, converts text to lowercase, splits the line into words, counts how many times each word appears using a dictionary.
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1   #adds one to count
order = {k: v for k, v in sorted(word_counts.items(), key = lambda item: item[1], reverse = True)}
#sorts the dictionary in descending order based on word frequency
word_removal = ["hath", "o", "thy","the", "and", "to", "of", "was", "a", "in", "that", "is", "it", "for", "with", "as", "his", "he", "be", "on", "not", "by", "this", "but", "from", "at", "or", "an", "which", "you", "were", "her", "all", "she", "there", "would", "their", "we", "him", "been", "has", "had", "do", "will", "no", "if", "i", "my", "so", "what", "are", "me", "your", "our", "they", "them", "us", "shall", "should", "could", "would", "must", "may", "can", "yet", "upon", "thee", "thou"]
#Contains common words
for word in word_removal:
    if word in order:
        del order[word]
#removes them from the sorted dictionary to focus on meaningful words
actual_dictionary = dict()
count = 0
limit = 15
#prints and stores only the top 15 most frequent words after filtering
for key, value in order.items():
    if count < limit:
        print(f"{key}:{value}")
        actual_dictionary.update(({key: value}))
        count += 1
    else:
        break

    data = []
    labels = []

    for key,value in actual_dictionary.items():
        labels.append(key)
        data.append(value)

plt.pie(data, labels = labels)

plt.title("Most common words in Romeo and Juliet or Macbeth")

plt.show()
#displays a pie chart of the top 15 most common words
