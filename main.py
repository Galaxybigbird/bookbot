def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha() or char == ' ':
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    return char_count

def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        word_count = get_word_count(file_contents)
        char_count = get_char_count(file_contents)
        
        # Create the report
        print(f"--- Begin report of {path} ---")
        print(f"{word_count} words found in the document\n")
        
        # Sort characters by count in descending order
        sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
        
        # Print counts for alphabet characters only
        for char, count in sorted_chars:
            if char.isalpha():
                print(f"The '{char}' character was found {count} times")
                
        print("--- End report ---")

if __name__ == "__main__":
    main()
