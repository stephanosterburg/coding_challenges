import os
from statistics import mean

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = mean(self.scores)
        if 90 <= avg <= 100:
            return "O"
        elif 80 <= avg < 90:
            return "E"
        elif 70 <= avg < 80:
            return "A"
        elif 55 <= avg < 70:
            return "P"
        elif 40 <= avg < 55:
            return "D"
        else:
            return "T"

if __name__ == '__main__':
    pwd = os.getcwd()
    filename = open(pwd + "/inheritance-testcases/input/input00.txt", 'r')

    line = list(map(str, filename.readline().split()))
    firstName = line[0]
    lastName = line[1]
    idNum = int(line[2])
    numScores = int(filename.readline())  # not needed for Python
    scores = list(map(int, filename.readline().split()))

    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
