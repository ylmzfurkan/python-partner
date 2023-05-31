def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = ''.join(text.split())
    return len(letters)

def main():
    text = input("Metni girin: ")

    word_count = count_words(text)
    letter_count = count_letters(text)

    print("Metindeki kelime sayısı:", word_count)
    print("Metindeki harf sayısı:", letter_count)

main()
