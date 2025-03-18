def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    word_count = number_of_words(text)
    print(f"{word_count} words found in the document")

def get_book_text(book_path):
    with open(book_path) as f:
        book_content = f.read()
        return book_content

def number_of_words(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    main()
