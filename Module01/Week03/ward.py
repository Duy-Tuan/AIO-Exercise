from abc import ABC, abstractmethod
from datetime import datetime


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass

    def get_age(self):
        return datetime.now().year - self._yob

    def get_yob(self):
        return self._yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def describe(self):
        print(
            f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def describe(self):
        print(
            f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def describe(self):
        print(
            f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__person_list = []

    def add_person(self, person):
        self.__person_list.append(person)

    def describe(self):
        print(f"Ward name: {self.__name}")
        for p in self.__person_list:
            p.describe()

    def count_doctor(self):
        number_of_doctor = 0
        for p in self.__person_list:
            if isinstance(p, Doctor):
                number_of_doctor += 1
        return number_of_doctor

    def sort_age(self):
        self.__person_list.sort(key=lambda p: p.get_age())

    def compute_average(self):
        total_teacher_age = [p.get_yob()
                             for p in self.__person_list if isinstance(p, Teacher)]
        return sum(total_teacher_age) / len(total_teacher_age)


if __name__ == "__main__":
    # Exercise 5
    print("Exercise 5")
    print("-"*20)
    student1 = Student(name="studentZ2023", yob=2011, grade="6")
    assert student1._yob == 2011
    student1.describe()

    # Exercise 6
    print("\nExercise 6")
    print("-"*20)
    teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
    assert teacher1._yob == 1991
    teacher1.describe()

    # Exercise 7
    print("\nExercise 7")
    print("-"*20)
    doctor1 = Doctor(name="doctorZ2023", yob=1981,
                     specialist="Endocrinologists")
    assert doctor1._yob == 1981
    doctor1.describe()

    # Exercise 8
    print("\nExercise 8")
    print("-"*20)
    student1 = Student(name="studentA", yob=2010, grade="7")
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    print(ward1.count_doctor())
