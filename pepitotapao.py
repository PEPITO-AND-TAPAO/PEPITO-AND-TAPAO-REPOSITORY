try:
    with open("diary.txt", "x") as file:
        file.write("Welcome to your personal diary system!\n")
except FileExistsError:
    print("Diary file already exists.\n")

while True:
    print("1. Write a new entry")
    print("2. Read all entries")
    print("3. Count all lines in the diary")
    print("4. Search date or keyword")
    print("5. Delete an entry")
    print("6. Exit")

    try:
        option = int(input("Choose an option: "))

        if option == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            print(f"Diary entry for {date}")
            
            with open("diary.txt", "a") as file:
                file.write(f"Date: {date}\n")
            
            entry = input("Write your diary entry: ")
            with open("diary.txt", "a") as file:
                file.write(entry + "\n\n")
            print("Entry added successfully!\n")

        elif option == 2:
            with open("diary.txt", "r") as file:
                print("\n--- Your Diary ---")
                print(file.read())
                print("------------------\n")

        elif option == 3:
            with open("diary.txt", "r") as file:
                lines = file.readlines()
                print(f"Total lines in diary: {len(lines)}\n")

        elif option == 4:
            keyword = input("Enter date or keyword to search: ")
            with open("diary.txt", "r") as file:
                found = False
                for line in file:
                    if keyword in line:
                        print(f"Found: {line.strip()}")
                        found = True
                if not found:
                    print("No matches found.\n")

        elif option == 5:
            print("Delete functionality requires overwriting the file.")
            # Note: Deleting specific entries in a text file usually involves 
            # reading all lines and writing back everything except the target.

        elif option == 6:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

    except ValueError:
        print("Please enter a valid number.")
    
    