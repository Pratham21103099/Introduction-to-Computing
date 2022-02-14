# ***Q1***

string1=input("Enter Any String: ")
list1=[]
list2=string1.split()    #To split all the elements of string in a list
length=len(list2)
d=dict()                 #Creating An Empty Dictionary
if length==1:            #When The User Enters Only 1 Word
    for i in string1:    
        list1.append(i) 
    for j in list1:      
        if j in d:       
            d[j]=d[j]+1  
        else:
            d[j]=1
    print(d)        

else:                    #When More Than 1 Word Is Entered
    for i in list2:      
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    print(d)
print("\n")

# ***Q2***

Day = int(input("Enter the Day: "))
Month = int(input("Enter the Month: "))
Year = int(input("Enter the Year: "))

# Below we are using a 'for' loop of single iteration to check whether the entered date is within our desired range or not And To print the desired output
# for i in range(1):
if Year in range(1800,2026):
    if Month in (1, 3, 5, 7, 8, 10):                                # As days in these months are equal
        if Day > 31 or Day < 0:
            print("Your Entered Day Cannot Exist")
        elif 0 < Day <= 30:
            Day += 1
            print("Next Date Is: ",Day,"/",Month,"/",Year)
        else:
            Day = 1
            Month +=1
            print("Next Date Is: ",Day,"/",Month,"/",Year)
    if Month in (4, 6, 9, 11):                                      # As days in these months are equal
        if Day > 30 or Day < 0:
            print("Your Entered Day Cannot Exist")
        elif 0 < Day <= 29:
            Day += 1
            print("Next Date Is: ",Day,"/",Month,"/",Year)
        else:
            Day = 1
            Month +=1
            print("Next Date Is: ",Day,"/",Month,"/",Year)
    if Month == 2:
        if (Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0:  # To Check For Leap Year
            if Day == 28:
                Day += 1
                print("Next Date Is: ",Day,"/",Month,"/",Year)
            elif Day == 29:
                Day = 1
                Month += 1
                print("Next Date Is: ",Day,"/",Month,"/",Year)
            else:
                print("Your entered Date is invalid")
        else:
            if Day > 28 or Day < 0:
                print("This Day cannot exist")
            elif 0 < Day <= 27:
                Day += 1
                print("Next Date Is: ",Day,"/",Month,"/",Year)
            else:
                Day = 1
                Month += 1
                print("Next Date Is: ",Day,"/",Month,"/",Year)
    if Month == 12:
        if Day > 31 or Day < 0:
            print("You entered Day cannot exist")
        elif 0 < Day <= 30:
            Day += 1
            print("Next Date Is: ",Day,"/",Month,"/",Year)
        else:
            Day = 1
            Month = 1
            Year += 1
            print("Next Date Is: ",Day,"/",Month,"/",Year)
    if Month > 12 or Month < 0:
        print("Your entered Month is invalid,Please enter a valid Month")
else:
    print("Year Should be >=1800 And <=2025")
print("\n")

# ***Q3***

Input = input("Enter The Desired Elements Followed By A Space: ")
userlist = Input.split()
# Print List
print("List: [", Input,"]")
# Converting each item to int type
for i in range(len(userlist)):
    userlist[i] = int(userlist[i])
squarelist =[(userlist[i], userlist[i]**2) for i in range(len(userlist))]
print(squarelist)

print("\n")

# ***Q4***

Grade_points=int(input("Enter Your Grade Points: "))
if(Grade_points==4):
    print("Performance: Poor")
    print("Letter Grade: D")
elif(Grade_points==5):
    print("Performanc: Below Average")
    print("Letter Grade: C")
elif(Grade_points==6):
    print("Performance: Average")
    print("Letter Grade: C+")
elif(Grade_points==7):
    print("Performance: Good")
    print("Letter Grade: B")
elif(Grade_points==8):
    print("Performance: Very Good")
    print("Letter Grade: B+")
elif(Grade_points==9):
    print("Performance: Excellent")
    print("Letter Grade: A")
elif(Grade_points==10):
    print("Performance: Outstanding")
    print("Letter Grade: A+")
else:
    print("Error, The Grade Point Is Out Of Range")

print("\n")

# ***Q5***

x = 6
for i in range(x):
    # printing spaces
    for j in range(i):
        print(' ', end='')
    # printing alphabet
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')  #ASCII VALUE OF A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75
    print()
print("\n")

# ***Q6***

dictionary ={}   # empty dictionary to store data entered by user

while True:
    user_choice = input("Enter 'Y' if you want to enter more data ,else enter 'N' : ")


    if user_choice.upper() == 'N':
        break
    if user_choice.upper() == 'Y':
        name = input("Enter your name :")
        sid = int(input("Enter your sid : "))
        dictionary[sid] = name
    else:
        print("Your enter  invalid choice,Please enter valid choice")   # case when user enter his choice other than 'Y'  and 'N'

# part (a)--------
print("part (a)")
print(dictionary)

#part (b)---------

print("part (b)")
print({i:j for i,j in sorted(dictionary.items(), key = lambda a:a[1])})   # here we sort the dictionary by name using inbuilt lambda function

#part (c)---------

print("Part (c)")
print({i:j for i,j in sorted(dictionary.items())})   # here we sort the dictionary sid-wise

#part (D) ---------
print("part(d)")
sid=int(input("Please enter a sid which you want to search>>"))
print("your searched student name is >>",dictionary[sid])

print("\n")

# ***Q7***

first_term=int(input("Give a number: "))
second_term=int(input("Give a number: "))
#now it will keep on printing the sequence till you say y and to stop it say n
sum=first_term+second_term
series=[first_term,second_term]
n="y"
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("Give y to contnue and n to stop going further: ")
print("Now we got a list having a fibonacci series: ")
print(series)

#now lets find average of the resultant fibonacci series
sum=0
for i in series:
    sum=sum+i
print("Average of the sequence: ")
print(sum/len(series))

print("\n")

# ***Q8***

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# part a
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("<a>", Part_A_Set)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("<b>", Part_B_Set)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("<c>",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("<d>", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("<e>", Part_E_Set)
