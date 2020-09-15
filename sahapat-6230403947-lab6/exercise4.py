f = open('kku.txt', encoding='utf-8')
fs = open('kku2.txt', 'a', encoding='utf-8')

for n in f.read():
    fs.write(n)

fs.write("Motto: วิทยา จริยา ปัญญา\n")
fs.write("Motto in English: Knowledge, Virtues, Wisdom")

f.close()
fs.close()

with open('kku2.txt', 'r', encoding='utf-8') as file:
    print(file.read())