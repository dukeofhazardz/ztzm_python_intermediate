def main():
    path = input("Enter the path to a text file: ")

    try:
        with open(path, "r", encoding="utf-8") as f:
            line_count = 0
            word_count = 0
            char_count = 0

            for line in f:
                line_count += 1
                word_count += len(line.split())
                char_count += len(line)

                print("\n--- File Statistics ---")
                print(f"Lines : {line_count}")
                print(f"Words : {word_count}")
                print(f"Characters : {char_count}")

    except FileNotFoundError:
        print("Error: That file does not exist.")

    except PermissionError:
        print("Error: You don’t have permission to read that file.")

if __name__ == "__main__":
    main()