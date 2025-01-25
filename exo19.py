def unique_word_counter():
    unique_words = set()
    total_words = 0

    print("Enter words. The program will stop when a duplicate word is entered.")

    while True:
        word = input("Enter a word: ").strip()
        total_words += 1

        if word in unique_words:
            print(f"\nYou typed in {len(unique_words)} unique words.")
            print(f"Total words entered: {total_words}")
            print(f"Unique words (alphabetically): {sorted(unique_words)}")

            save = input("Would you like to save the unique words to a file? (yes/no): ").strip().lower()
            if save == "yes":
                with open("unique_words.txt", "w") as file:
                    file.write("\n".join(sorted(unique_words)))
                print("Unique words saved to 'unique_words.txt'.")
            break

        unique_words.add(word)

if __name__ == "__main__":
    unique_word_counter()
