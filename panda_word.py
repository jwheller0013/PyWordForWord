import pandas as pd
import os
import re

#word_freq and letter_freq tables

class TextProcessing():
    def __init__(self):
        pass

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

    def pan_word(self, text):
        sentclean = re.sub(r'[^\w\s]', '', text).lower()
        sentcleansplit = sentclean.split()
        word_counts = pd.Series(sentcleansplit).value_counts().reset_index()
        word_counts.columns = ['Word', 'Frequency']
        return word_counts

    def pan_letter(self, text):
        sentclean = re.sub(r'[^a-zA-Z]', '', text).lower()
        letter_counts = pd.Series(list(sentclean)).value_counts().reset_index()
        letter_counts.columns = ['Letter', 'Frequency']
        return letter_counts

test = TextProcessing()

x =test.file_to_string('/testdata/testdata4.txt')

print(test.pan_word(x))

print(test.pan_letter(x))