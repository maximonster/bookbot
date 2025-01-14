def word_count(words):
    wc = words.split()
    return len(wc)

def character_count(text):
    character_counts = {}
    lower_text = text.lower()
    characters = list(lower_text)
    for char in characters:
        if (char in character_counts):
            character_counts[char]+=1
        else:
            character_counts[char]=1
    return character_counts

def sort_on(d):
    return d["num"]

def Report(path,word_count, char_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the book")
    sorted_chars =[]
    for ch in char_count:
        sorted_chars.append({"char":ch, "num": char_count[ch]})
    sorted_chars.sort(reverse=True, key=sort_on)
    for chars in sorted_chars:
        if not chars["char"].isalpha():
            continue
        print(f"The '{chars["char"]}' character was found {chars["num"]} times")
    print("End of report")
    pass

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    Report(book_path,word_count(text),character_count(text))


main()