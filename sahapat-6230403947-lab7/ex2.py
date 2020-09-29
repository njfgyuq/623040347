class Student:
    university_name = "Khon Kean University"

    def __init__(self, name, *ids):
        self.name = name
        self.ids = ids

    def print(self):
        print(f"{self.name} registered courses {self.ids}")


if __name__ == '__main__':
    manee = Student("Manee", "842004")
    mana = Student("Mana", "842004", "842005", "813701")
    chujai = Student("Chujai", "842004", "842005")
    manee.print()
    mana.print()
    chujai.print()
    print(f"These students are in {Student.university_name}")
