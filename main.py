def main():
    filename = "./books/frankenstein.txt"
    file_contents = read_text(filename)
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    char_count.sort(reverse=True, key=sort_on)
    print("--- Begin report of {0}---".format(filename))
    print("{0} words found in the document".format(word_count))
    for c in char_count:
        if c["char"].isalpha():
            print(
                "The '{0}' character was fount {1} times".format(c["char"], c["count"])
            )
    print("--- End report ---")


def sort_on(dict):
    return dict["count"]


def count_words(text):
    words = text.split()
    return len(words)


def read_text(filename):
    with open(filename) as f:
        file_contents = f.read()
        return file_contents


def count_characters(text):
    lowercase = text.lower()
    character_count = {}
    for char in lowercase:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return convert_dict_to_list(character_count)


def convert_dict_to_list(dict):
    list = []
    for k, v in dict.items():
        list.append({"char": k, "count": v})
    return list


main()
