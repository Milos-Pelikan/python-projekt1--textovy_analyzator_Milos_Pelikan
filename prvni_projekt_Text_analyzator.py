# projekt_1.py: Text Analyzer project for Engeto Online Python Academy
# author: miloš pelikán
# email: milos.pelikan@gymbeam.com
# discord: Miloš P. #4629

# User authentication
registered_users = {'bob': '123',
                    'ann': 'pass123',
                    'mike': 'password123',
                    'liz': 'pass123'}

# separator chart title
separator = "-" * 40
chart_title = "LEN|  OCCURENCES  |NR."

# Texts to analyze
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

username = input("username: ")
password = input("password: ")

print(separator)

if username in registered_users and registered_users[username] == password:
    print("Welcome to the app, " + username)
else:
    print("unregistered user, terminating the program..")
    exit()

print("We have", len(TEXTS), 'texts to be analyzed.')

print (separator)


# Choose text to analyze
text_num = int(input("Enter a number btw. 1 and 3 to select: "))

print(separator)

if text_num not in [1, 2, 3]:
    print("Invalid text number.")
    exit()

# Calculate statistics for selected text
text = TEXTS[text_num-1]
words = text.split()
word_count = len(words)
capitalized_word_count = 0
uppercase_word_count = -1
lowercase_word_count = 0
number_count = 0
number_sum = 0

for word in words:
    if word[0].isupper():
        capitalized_word_count += 1
    if word.isupper():
        uppercase_word_count += 1
    if word.islower():
        lowercase_word_count += 1
    if word.isdigit():
        number_count += 1
        number_sum += int(word)

print("There are", word_count, "words in the selected text.")
print("There are", capitalized_word_count, "titlecase words.")
print("There are", uppercase_word_count, "uppercase words.")
print("There are", lowercase_word_count, "lowercase words.")
print("There are", number_count, "numeric strings.")
print("The sum of all the numbers", number_sum)

print(separator)
print(chart_title)
print(separator)

# calculation data for bar chart, combine all texts into one string

import collections


# count the frequency of each word length
words = [word.strip(",.") for word in words]
word_lengths = [len(word) for word in words]
word_length_counter = collections.Counter(word_lengths)

# sort the word lengths by their frequency
sorted_word_lengths = sorted(word_length_counter.items(), key=lambda x: x[0])

# print the results
for length, count in sorted_word_lengths:
    print(" {:2}|{:<15}|{}".format(length, "*" * count, count))


