def main():
    sentence = input("Enter a sentence to log: ")

    try:
        with open("activity.log", "a", encoding="utf-8") as log_file:
            log_file.write(sentence + "\n")

        with open("activity.log", "rb") as src, open("activity_backup.log", "wb") as dst:
            dst.write(src.read())
            print("Backup complete!")

    except IOError as err:
        print(f"File operation failed: {err}")

if __name__ == "__main__":
    main()