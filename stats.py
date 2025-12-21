def get_num_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")


def sort_character_count(characters):
    list = []
    for key in characters:
        dict = {}
        dict["name"] = key
        dict["num"] = characters[key]
        list.append(dict)
    list.sort(key=sort_helper, reverse=True)
    return list

def sort_helper(e):
    return e["num"]


def get_character_count(text):
    char_dict = {}
    for i in range(0, len(text)):
        char = text[i].lower()
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict
