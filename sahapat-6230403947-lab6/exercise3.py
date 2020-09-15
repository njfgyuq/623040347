file_name = input("Enter a filename: ")
with open(file_name, 'r', encoding='utf-8') as file:
    print(file.read())