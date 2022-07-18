





"""

print("Welcome to Python")


# Python Variables ....

age = 20 # integer declaration ..

name = "#########    MITHUN    ############" # String  declaration ..

print(age)

print(name)

purchasevalue = 20.3



# Type Casting ....

a = str(10)
print (a)

b = float(5)

print (b)


name , school , roll = "Mithun", "DAV Model", 10



# Indentation

def addtwonumbers(): 
    return 5+3



from operator import truediv


x = 1j
print(type(x))

x = True

print(type(x))

x = ["MITHUN", "RAVI","PYTHON"]

print(type(x))


x = ("MITHUN", "RAVI","PYTHON")

print(type(x))


# Python Operators ???


# Python Arithmatic Operators ..

print(1+1)
print(1-1)
print(1*1)
print(1/1)
print(10%1)


# Python Assignment Operators ..


# = , +=

# a+=4

# Python Comparison Operators ..

# == , != , >  ,<


# Python logical Operators ..

# and , or , not



# Python EF - ELSE




a = 5
b = 2
c = 0
z = 5

# IF

if a > b and c < b and a > c:
    print("All Conditions are OK")


# IF .. ELSE

if a < b:
    print("a is greater than b")

else:
    print("a is less than b")  



# IF ...ELSEIF .... ELSE


if a < b:
    print("a is greater than b")

elif z ==a and c > a:    
    print("a ========  Z")
else:
    print("a is less than b") 


a = "Welcome to Python"

print(a)

print(a[2])

print(len(a))

if "Python1" not in a:
    print("Pytho1n word is not present in your text")




from re import A


a = "Welcome to Python"
# For Loop in Python ....

for x in a:
    print(x)




# Check whether "Microsoft" is present in your List a?

a = ["Cognzant" , "IBM" , "Microsoft" , "Facebook" , "Meta"]

for z in a:
    print(z)
    if z == "IBM":
        break



a = 10

for i in range(a):
    print(i)


a = 50

for i in range(5, a , 10):
    print(i)



def addtwonum(a,b):
    return a+int(b)


def addtwoString(lang):
    print("Welcome to"+" "+str(lang))   



def addtwonum2():
    print("This is my first method .....")  


#print(addtwonum(100,"100"))

#print(addtwoString(10))

M =  "10,000"
P = "2#000"
W = "500"

EX = 12500

TotalNum = int(M.replace("," , ""))+ int(P.replace("#" , "")) + int(W.replace("," , ""))

if EX == TotalNum:
    print("Cart pricing Calculation is correct .......... PASS")


"""

testDict = {
    "Name":"MITHUN",
    "Company":"Wipro",
    "Age":30
}    


#print(testDict)
#print(testDict["Company"])

testDict["Company"] = "Google"
testDict.update({"Status":"Still Working"})

print(testDict)

for a in testDict:
    print(a)









