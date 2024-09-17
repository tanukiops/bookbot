def main():
    file_contents = read_text("./books/frankenstein.txt")
    print(count_words(file_contents))


def count_words(text):
    words = text.split()
    return len(words)


def read_text(filename):
    with open(filename) as f:
        file_contents = f.read()
        return file_contents


main()
