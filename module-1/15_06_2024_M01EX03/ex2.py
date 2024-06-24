from abc import ABC, abstractmethod
from enum import Enum


class Job(Enum):
    Student = 1
    Teacher = 2
    Doctor = 3


class Person(ABC):
    def __init__(self, name: str, yob: int, job: Job) -> None:
        self.__name = name
        self.__yob = yob
        self.__job = job.name

    def get_name(self) -> str:
        return self.__name

    def get_yob(self) -> int:
        return self.__yob

    def get_job(self) -> str:
        return self.__job

    @abstractmethod
    def describe(self) -> None:
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str) -> None:
        super().__init__(name, yob, Job.Student)
        self.__grade = grade

    def describe(self) -> None:
        print(f"{self.get_job()} - Name: {self.get_name()} - YoB: {self.get_yob()} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str) -> None:
        super().__init__(name, yob, Job.Teacher)
        self.__subject = subject

    def describe(self) -> None:
        print(f"{self.get_job()} - Name: {self.get_name()} - YoB: {self.get_yob()} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str) -> None:
        super().__init__(name, yob, Job.Doctor)
        self.__specialist = specialist

    def describe(self) -> None:
        print(f"{self.get_job()} - Name: {self.get_name()} - YoB: {self.get_yob()} - Specialist: {self.__specialist}")


class Ward:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__people = []
        self.__jobs = {}

    def add_person(self, person: Person) -> None:
        self.__people.append(person)
        self.__jobs[person.get_job()] = self.__jobs.get(
            person.get_job(), []
        )
        self.__jobs[person.get_job()].append(person)

    def count_doctor(self) -> int:
        return len(self.__jobs.get(Job.Doctor.name, []))

    def sort_age(self) -> None:
        self.__people.sort(key=lambda x: x.get_yob())

    def compute_average(self) -> float:
        teachers = self.__jobs.get(Job.Teacher.name, [])
        total_yob = 0

        for teacher in teachers:
            total_yob += teacher.get_yob()

        return total_yob / len(teachers)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for person in self.__people:
            person.describe()


if __name__ == '__main__':
    # 2a
    s1 = Student(name="studentA", yob=2010, grade="7")
    s1.describe()

    t1 = Teacher(name="teacherA", yob=1969, subject="Math")
    t1.describe()

    d1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    d1.describe()

    # 2b
    t2 = Teacher(name="teacherB", yob=1995, subject="History")
    d2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

    ward1 = Ward(name="Ward1")
    ward1.add_person(s1)
    ward1.add_person(t1)
    ward1.add_person(t2)
    ward1.add_person(d1)
    ward1.add_person(d2)
    ward1.describe()

    # 2c
    print(f"\nNumber of doctors: {ward1.count_doctor()}")

    # 2d
    print("\nAfter sorting Age of Ward1 people")
    ward1.sort_age()
    ward1.describe()

    # 2e
    print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
