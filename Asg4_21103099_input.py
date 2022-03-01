# ***Q1***

 #Tower Of Hanoi , We Have 3 Disks And 3 Rods (A,B,C).
 #Rules: 1)Only One Disk Can Be Moved At A Time
 #       2)A Disk Can Only Be Moved If It Is The Uppermost Disk On A Stack
 #       3)No Disk May Be Placed On Top Of A Smaller Disk  
def TowerOfHanoi(n , Start, Goal, In_Between):
	if n == 0:
		return
	TowerOfHanoi(n-1, Start, In_Between, Goal)
	print("Move Disk",n,"From Rod",Start,"To Rod",Goal)
	TowerOfHanoi(n-1, In_Between, Goal, Start)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
print('\n')

# ***Q2***

from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle '))

print("USING FOR LOOP")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #for spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	# for new line
print("\n\n")

print("USING WHILE LOOP")

i=0
while(i<n):
    z=n-i+1
    while(z>0):
        print(end=" ")
        z-=1
    y=0
    while(y<i+1):
        print(factorial(i) // (factorial(y) * factorial(i - y)), end=" ")
        y+=1
    i+=1
    print()
print("\n\n")

print("USING RECURSSIONS")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")


# ***Q3***

a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
quotient=a//b
remainder=a%b
# Part (a) 
print(("Part (A)"))
print("Quotient  Is Callable: " ,callable(quotient))   # Checking Whether Quotient And Remainder Are Callable Or Not
print("Remainder Is Callable: " ,callable(remainder))
# Part (b)
print(("Part (B)"))
if remainder==0:
    print("Remainder is zero")
if quotient ==0:
    print("quotient is zero")
elif remainder!=0 and quotient!=0:
    print("All values are non zero")
# Part (c) 
lst=[]   # vacant list to store the value
lst1=[quotient+4, remainder + 4, quotient +5, remainder+5, quotient+6, remainder+6]
for value in lst1:
    if (value>4):
        lst.append(value)
print("Part (C)")
print("The values greater than 4 is contained in this list ",lst)
# Part (d) 
set1=set(lst)  # Converting Into Set Datatype
print("Part (D)")
print("Set Is: " ,set1)
# Part (e)
immutable = frozenset(set1)           # we use a inbuilt function " frozenset" to make set immutable
print("Part (E)")
print("Immutable Set: ",immutable)
# Part (f) 
print("Part (F)")
print("The Required Hash Value Of Maximum Valued Element Of Set Is: ",hash(max(immutable)))

print("\n")

# ***Q4***

class Student:
    def __init__(self, student,sid):
        self.name = student
        self.sid = sid    
    def __del__(self):
        print("Object Destroyed!")
student1 = Student("Pratham Bansal", 21103099)  #Creating Object
print("Object created")
print(f"The Name Of The Student: {student1.name} and SID: {student1.sid}.")  #Printing The Assigned Values
del student1  #Deleting Object

print("\n")

# ***Q5***

class employees :
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

# Creating The Objects
emp1=employees('Mehak',40000)
emp2=employees('Ashok',50000)
emp3=employees('Viren',60000)

emp1.salary='70000'         # Updating Salary Of Mehak/Employee1
print("Part (a)")
print(f"The New Salary Of {emp1.name} Is: {emp1.salary}")
print("\nPart (b)")
del emp3            # Deleting Record Of Employee Viren
print("The Employee Record Of Viren Has Been Deleted")

print("\n")

# ***Q6***

 #Using Concept Of Anagrams
def anagram(word):
    if len(word)==1:
        return [word];
    Partial_Words=anagram(word[1:])
    char=word[0]
    result=[]
    for perm in Partial_Words:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result        


George_word=input("Enter Your Word: ")
Possible_words=anagram(George_word)
Barbie_word=input("Your Reply Word: ")
print("Possible Words-",Possible_words)
print("If Barbie's Word Lies In The List,Then Their Friendship Is Real.")

if Barbie_word in Possible_words:
    print("Friendship is Real.")
else:
    print("Friendship is Fake.")
