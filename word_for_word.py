import os
import re

class TextProcessing():
    def __init__(self):
        pass
        # self.characters = 0
        # self.num_words = 0
        # self.num_lines = 0


    #reads the contents of a file, line by line, and creates a String object
    #making sure all the newlines are preserved.
    def file_to_string(self, filename):
        # pass
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        try:
            file_path = absolute_path + filename
            with open(file_path, 'r') as file:
                result_string = file.read()
            return result_string
        except FileNotFoundError:
            return f"File '{filename}' not found."
        except IOError as e:
            return f"Error reading file: {e}"


    #count the number of characters in a file, number of words, number of lines
    #Returns an tuple with the number of lines, words and characters
    def wc(self, str: input):
        pass
        str_chars = len(str)
        str_words = len(str.split())
        str_lines = str.count('\n')

        return (str_chars, str_words, str_lines)

    #word count. words in the string, produce a dictionary with (str word, int numOfTimes)
    def word_frequency(self, sent: str):
        pass
        word_freq = {x: sent.split().count(x) for x in set(sent.split())}
        return word_freq

    #collects the frequency of each letter within the input
    #dictionary with letters as the key, number of occurences as value.
    def letter_frequency(self, char, sent):
        pass
        count = 0
        for x in sent:
            if x == char:
                count += 1
        return count

    #numberOfOccurences / totalNumberOfWords
    def frequency(self, word, total_words, sent):
        pass
        count = 0
        sentclean = re.sub(r'[^\w\s]', '',sent)
        sentcleansplit = sentclean.split()
        for x in sentcleansplit:
            if x == word:
                count += 1
        freq = count/total_words
        return freq


test = TextProcessing()

x =test.file_to_string('/testdata/testdata4.txt')
# print(x)

tup = test.wc(x)
print(tup)

d = test.word_frequency(x)
print(d)

e = test.letter_frequency('q', x)
print(e)

f = test.frequency('of', tup[1], x)
print(f)