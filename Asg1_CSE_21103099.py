#<<<<Question 1>>>>
# This is a program to find average of three numbers entered by the user
N1=int(input("Enter Number 1: "))
N2=int(input("Enter Number 2: "))
N3=int(input("Enter Number 3: "))
print("Average Of The Three Numbers Is: ",(N1+N2+N3)/3)

print("\n")

#<<<<Question 2>>>>
#This is a program to compute a person's income tax
#All The Incomes Are in Dollar($)
Standard_Deduction=int(10000)
Gross_Income=float(input("Enter Your Gross Income: "))
Number_of_Dependent=int(input("Enter Number Of Dependents(If Any): "))
Tax_Rate=float(20/100) 
Dependent_Deduction=int(3000) #For each dependent, a taxpayer is allowed an additional $3,000 deduction
Taxable_Income=float(Gross_Income - Standard_Deduction - (Dependent_Deduction)*(Number_of_Dependent))
Tax=Taxable_Income*Tax_Rate
print("Your Income Tax Is: ",Tax)

print("\n")

#<<<<Question 3>>>>
#This is a program to store different data type values into a list
SID = int(input("Enter your SID: "))
Name = input("Enter your name: ")
Gender = input("Enter your gender, Use Gender values: ‘F’, ‘M’, ‘U’(For Unknown): ")
Course_Name = input("Enter your course name: ")
CGPA = float(input("Enter your CGPA: "))
Student = [SID, Name, Gender, Course_Name, CGPA] #For Creating List
print("\n",Student)

print("\n")

#<<<<Question 4>>>>
#This is a program to enter marks of 5 students into a list and display them in sorted manner
Student1 = int(input("Enter marks of 1st Student: "))
Student2 = int(input("Enter marks of 2nd Student: "))
Student3 = int(input("Enter marks of 3rd Student: "))
Student4 = int(input("Enter marks of 4th Student: "))
Student5 = int(input("Enter marks of 5th Student: "))

Markslist = [Student1, Student2, Student3, Student4, Student5]
Markslist.sort() #For Sorting The Marks
print(Markslist)

print("\n")

#<<<<Question 5>>>>
Color = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
Color.remove("Black") #Removing 4th Element
print(Color)

Color1 = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
Color1[3:5] = ['Purple'] #For Replacing Black And Pink From The List With Purple
print(Color1)           
