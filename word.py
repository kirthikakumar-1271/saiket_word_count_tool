from collections import Counter
import string

def analyze_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

        # Count characters
        char_count = len(content)

        # Count lines
        line_count = len(content.splitlines())

        # Remove punctuation and convert to lowercase
        cleaned_text = content.lower().translate(
            str.maketrans('', '', string.punctuation)
        )

        # Count words
        words = cleaned_text.split()
        word_count = len(words)

        # Word frequency
        word_freq = Counter(words)

        print("\n===== TEXT FILE ANALYSIS =====")
        print(f"Total Lines      : {line_count}")
        print(f"Total Words      : {word_count}")
        print(f"Total Characters : {char_count}")

        print("\n===== TOP 10 MOST COMMON WORDS =====")

        for word, count in word_freq.most_common(10):
            print(f"{word:<15} {count}")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Main Program
filename = input("Enter file name: ")
analyze_file(filename)