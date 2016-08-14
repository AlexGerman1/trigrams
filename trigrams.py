# -*- coding: utf-8 -*-
import io
import random
TEXT = "text.txt"


def load_words(file_path):
    file_path = io.open(TEXT, encoding='utf-8')
    text_data = file_path.read()
    file_path.close()
    split_words = text_data.split()
    return split_words


def build_table(words):
    words_dict = {}
    for i in range(0, len(words) - 2):
        a_key = (words[i], words[i + 1])
        a_value = words[i + 2]
        words_dict.setdefault(a_key, []).append(a_value)
    return words_dict


def main(words_dict, word_limit):
    story_words = words_dict
    new_story = []
    start_key = random.choice(list(story_words.keys()))
    start_value = story_words[start_key]
    start_key = ' '.join(start_key)
    new_story.append(start_key)
    new_story.append(' '.join(start_value))
    new_story = ' '.join(new_story)
    new_story = new_story.split()
    new_key = ()
    print('NEW KEY BEFORE LOOP', new_key)
    for new_key in new_story:
        while len(new_story) < word_limit:
            new_key = (new_story[-2], new_story[-1])
            print('FOR LOOP NEW KEY', new_key)
            if new_key in story_words:
                new_value = ' '.join(story_words[new_key])
                new_story.append(new_value)
    new_story = ' '.join(new_story)
    print(new_story)


def call_all():
    main(build_table(load_words(TEXT)), 9)


call_all()

# if __name__ == '__main__':
#     call_all()
