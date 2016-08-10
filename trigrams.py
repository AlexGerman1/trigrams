# -*- coding: utf-8 -*-
import io


def split_string(f):
    f = io.open('text.txt', encoding='utf-8')
    text_data = f.read()
    f.close()
    split_string.lst = text_data.split(" ")
    return split_string.lst


def main(f, n):
    split_string(f)
    for i in split_string.lst:
        words = {}
        words = (split_string.lst[0] + " " + split_string.lst[int(1)],
                 split_string.lst[2])
        print words
    return words


main('one two three', 1)
