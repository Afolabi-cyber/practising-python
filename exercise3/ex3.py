from argparse import ArgumentParser
import os

def read_file(filepath):
    if not os.path.exists(filepath):
        print("Error: file not found")
        return

    with open(str(filepath), "r", encoding="utf-8") as f:
        text = f.read()
        return text
    
def count_words(text):
    line_count = len(text.splitlines())
    word_count = len(text.split())

    return word_count, line_count

def most_common_words(text, n=4):
    words_dict = {}
    freq = []
    words = [word for word in text.split(" ")]
    for i in words:
        words_dict[i] = words_dict.get(i, 0) + 1
    for wd, num in words_dict.items():
        if num >= n:
            freq.append((wd, num))
    return freq

def display_result(stats):
    out = []
    for x, y in stats:
        out.append(f'{x}: {y}')
    return out

def main():
    parser = ArgumentParser(description="A simple command-line program.")

    parser.add_argument("filename", help="The name of the bloody file to work on")
    args = parser.parse_args()
    file_path = args.filename
    print(f"File analyzed: {file_path}")

    print("-----------------------------")
    text = read_file(file_path)

    count, lines = count_words(text)
    print(f"Lines: {lines}")
    print(f"Words: {count}")

    words = most_common_words(text)
    result = display_result(words)

    print(f"The common words: \n")
    print("\n".join(result))
    print("-----------------------------")

if __name__ == "__main__": 
    main()