''' Create a summary.txt of https://www.whitehouse.gov/briefings-statements/remarks-president-trump-state-union-address-3/

Use following statistics: word count, character count, average word length
average sentence length, word distribution of all words ending in 'ly', list of top 10 longest words'''

# count the words in summary.txt
file = open("summary.txt")
summary = file.read()
words = summary.split()

print('Total word count :', len(words))

# total character count
file = open("summary.txt")
summary = file.read()
number_of_characters = len(summary)
print('Number of characters in text file :', number_of_characters)

# calculate average word length
file = open("summary.txt")
words = summary.split()
average = sum(len(word) for word in words) / len(words)
print('The average word length is :', average)

# calcualte average sentence length

    

# word distribution of all words ending in "ly"




# list of the top longest words
def longest_words(summary):
    with open(summary, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_words('summary.txt'))
