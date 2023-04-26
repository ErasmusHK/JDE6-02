import random
import string

#path = '../JDE6-02//news.txt'
#f = open(path, "r", encoding="utf-8")
#content = f.read()
#f.close()

with open('./news.txt', 'r', encoding="utf-8") as f:
    content = f.read()

# Task-1 - count the total number of words in the prargraph that contains vowel characters(a, e, i, o u)
def erasmus_task1(text):
    count = 0
    for character in text:
        if character in ["a", "e", "i", "o", "u"]:
            count += 1
    return count

# Task-2 - encode the paragraph by shifting the position of each character by a variable value e.g. I am a boy (1) -> J bn b cpz
def erasmus_task2(text):
    encoding_list = string.ascii_letters+"a"
    encode_list = []
    for character in text:
        if character in encoding_list:
            encode_list.append(encoding_list[encoding_list.index(character)+1])
        else:
            encode_list.append(character)
    return "".join(encode_list)

# Task-3 - Reverse the entire paragraph line by line e.g. I am a boy -> yob a ma I
def erasmus_task3(text):
    reverse_line_list = [i[::-1] for i in text.splitlines()]
    return "".join(reverse_line_list)

# Task-4 - Reverse the order of character of each word e.g. I am a boy -> I ma a yob
def erasmus_task4(text):
    reverse_word_list = [i[::-1] for i in text.split()]
    return " ".join(reverse_word_list)

if __name__ == "__main__":

    print(erasmus_task1(content))
    print(erasmus_task2(content.splitlines()[1]))
    print(erasmus_task3(content.splitlines()[1]))
    print(erasmus_task4(content.splitlines()[1]))