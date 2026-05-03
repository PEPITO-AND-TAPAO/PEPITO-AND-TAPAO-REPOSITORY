try:
    with open("diary.txt", "x") as file:
        file.write("Welcome to your personal diary system!\n")
except FileExistsError:
    print("Diary file already exists.\n")