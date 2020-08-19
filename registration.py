from os import system, name
import collections
import csv

Student = collections.namedtuple('Student', ['name', 'rollNo', 'semester', 'course'])
Course = collections.namedtuple('Course', ['id', 'name'])
studentList = []
courseList = {1: [], 2: [], 3: [], 4: []}
courseInfo = {}
rollNoList = []


def clear():
    if name == 'nt':
        __ = system('cls')
    else:
        __ = system('clear')


def main():
    # read course file and save it in a list
    with open("C:\\Users\\Tanishq\\Documents\\notepad++\\courseInfo.txt", "r") as courseFile:
        csv_reader = csv.reader(courseFile, delimiter=",")
        for row in csv_reader:
            courseList[int(row[0][2])].append(Course(row[0], row[1]))
            courseInfo.__setitem__(row[0], row[1])

    # get student info
    flag = "y"
    while flag == "y":
        print("------------------------------------------")
        print("Welcome to the course registration process")
        print("------------------------------------------\n")
        valid = True
        name = input("Enter Student's Name:- ")
        while valid:
            rollNo = input("Enter Student's Roll no.:- ")
            if len(rollNo) == 7 and (rollNo[0:3] == "CS1" or rollNo[0:3] == "EC1") and rollNo not in rollNoList:
                valid = False
                rollNoList.append(rollNo)
            else:
                print("Invalid roll no. Please re-enter.")

        valid = True
        while valid:
            sem = input("Enter current semester:- ")
            if sem < '1' or sem > '8':
                print("Invalid semester. Please re-enter.")
            else:
                valid = False

        studentList.append(Student(name, rollNo, sem, []))

        print("The following courses are offered to you:- ")
        sem = int(sem)
        year = int((sem + 1) / 2)
        for i in courseList[year]:
            if i.id[0:2] == rollNo[0:2]:
                print(i.id + " " + i.name)

        for i in range(1, 4):
            valid = True
            while valid:
                course = input("Enter course id " + str(i) + ":- ")
                if course not in studentList[-1].course and Course(course, courseInfo.get(course)) in courseList[year]:
                    valid = False
                    studentList[-1].course.append(course)
                else:
                    print("Invalid course entered. Re-enter")

        opt = input("Do you want any more courses[y/n]?")
        while opt == "y":
            valid = True
            while valid:
                course = input("Enter course id " + str(len(studentList[-1].course) + 1) + ":- ")
                if course not in studentList[-1].course and Course(course, courseInfo.get(course)) in courseList[year]:
                    valid = False
                    studentList[-1].course.append(course)
                else:
                    print("Invalid course entered. Re-enter")

            opt = input("Do you want any more courses[y/n]?")

        print("You are successfully registered for the following courses:- ")
        print(studentList[-1].course)
        flag = input("\nAny more students to register?[y/n]")
        clear()

    courseFile = open("C:\\Users\\Tanishq\\Documents\\notepad++\\student course information.txt", "a")
    for item in studentList:
        courseFile.write(item.name + "\t" + item.rollNo + "\t" + item.semester + "\t")
        for i in item.course:
            courseFile.write(i + "-" + courseInfo[i] + ",")
        courseFile.write("\n")

    courseFile.close()
    print(open("C:\\Users\\Tanishq\\Documents\\notepad++\\student course information.txt", "r").read())


if __name__ == '__main__':
    main()
