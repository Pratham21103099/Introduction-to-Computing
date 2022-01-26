# ***QUESTION 1***
string1="Python is a case sensitive language" #String1
print("<A> The Length Of The String Is: ",len(string1)) #Function to Find Length Of String
print("<B> The Reversed String Is: ",string1[-1::-1])
string2=string1[10:26] #STORED 'a case sensitive' IN A NEW STRING
string2.replace("a case sensitive","object oriented") #REPLACED "a case sensitive" With "object oriented"
print("<E> The Index Of Substring 'a' Is: ",string1.find('a'))
print("<F> The Original String After Removing Whitespace Is: ",string1.replace(" ",""))
print("\n")

# ***QUESTION 2***
Name=input("Enter Your Name: ")
Sid=int(input("Enter Your SID: "))
Department=input("Enter Your Department: ")
Cgpa=float(input("Enter Your CGPA: "))
print("\n Hey, %s Here!" %Name)
print("My SID is %d" %Sid)
print("I am from %s" %Department,"department and my CGPA is %.1f" %Cgpa)
print("\n")

# ***QUESTION 3***
a=56
b=10
print("a. ",a&b)
print("b. ",a|b)
print("c. ",a^b)
print("Left shift both a and b with 2 bits respectively are :",a<<2 ,b<<2)
print("Right shift a with 2 bits and b with 4 bits respectively are : ",a>>2,b>>4)
print("\n")

# ***QUESTION 4***
N1=float(input('Enter 1st Number: '))
N2=float(input('Enter 2nd Number: '))
N3=float(input('Enter 3rd Number: '))
if N1>N2:
    if N1>N3:
        print('\n',N1,' Is The Greatest Number')
    else:
        print('\n',N3,' Is The Greatest Number')
else:
    if N2>N3:
        print('\n',N2,' Is The Greatest Number')
    else:
        print('\n',N3,' Is The Greatest Number')
print("\n")

# ***QUESTION 5***
string=input("Enter A String: ")
if 'name' in string:
    print("Yes, The Word 'name' Is Present In The String")
else:
    print("No, The Word 'name' Is Not Present In The String")
print("\n")

# ***QUESTION 6***
p=int(input("Enter First Side Of Triangle: "))
q=int(input("Enter Second Side Of Triangle: "))
r=int(input("Enter Third Side Of Triangle: "))
if((p+q)>r and (q+r)>p and (r+p)>q and p>0 and q>0 and r>0): #All sides should be positive and sum of two sides should be greater than third side
    print("\n Yes, A Triangle Can Be Formed With These Sides")
else:
    print("\n No, A Triangle Can Not Be Formed With These Sides")
