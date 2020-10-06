class ComEnStudent:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

    def __str__(self):
        return f'{self.name} has taken courses: {self.courses}'

    def take_courses(self, *courses):
        self.courses.extend(courses)


class CoEStudent(ComEnStudent):
    def __init__(self, name, courses):
        super().__init__(name, courses)


class DMEStudent(ComEnStudent):
    def __init__(self, name, courses):
        super().__init__(name, courses)

    def __str__(self):
        return f'{super().__str__()} ' \
               f'\nspecialized in creating content type:{self.content}'

    def make_content_type(self, content):
        self.content = content


if __name__ == '__main__':
    com_students = []
    manee = CoEStudent("Manee", ["EN813701"])
    mana = DMEStudent("Mana", ["EN842004"])
    manee.take_courses("EN813702", "EN811301", "EN811302")
    mana.take_courses("EN842005")
    mana.make_content_type("Infographics")
    com_students.append(manee)
    com_students.append(mana)
    for com_students in com_students:
        com_students.take_courses("SC401206")
        print(com_students)
