# -*- coding: utf-8 -*-
import io


def load_words(file_path):
    file_path = io.open('text.txt', encoding='utf-8')
    text_data = file_path.read()
    file_path.close()
    return text_data.split()


def build_table(words):
    words_dict = {}
    # words = load_words(file_path)
    for i in range(len(words) - 2):
        a_key = (words[i], words[i + 1])
        a_value = words[i + 2]
        words_dict.setdefault(a_key, []).append(a_value)
    return words_dict


print(build_table('one two three four one five one two five'.split()))
