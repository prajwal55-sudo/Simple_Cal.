print (" ")
print ("Loading Simple_Cal... ") #Start
print (" ")

name = str(input("ENTER YOUR NAME : "))
print ("Welcome" , name.capitalize() , "to Simple_Cal.")

print (" ")
print ("Loading Complete! ")

input ("Press Enter to Continue...")

print (" ")

print (r"                         Welcome To Simple_Cal.  (⁠•⁠‿⁠•⁠)               ")

print (" ")
print ("Version    : 1.0.0")
print ("Coded by   : Prajwal_Kadlag")
print ("Date       : 2026-02-04") #YYYY-MM-DD
print ("Project    : 01 - Python Project") #Project number
print (" ")

input ('Press Enter to "SKIP" to the good part...  :) ')
print (" ")

print ("Description: This is a simple calculator that can perform basic calculations. \n             This calculator can perform Addition,Subtraction,Multiplication\n             and Division.Yeah!!That's it..")
print (" ")

print(r"             Enjoy using Simple_Cal ¯\(ツ)/¯     ")

print (" ")
print ("             {By the way try doing 0*1 It will be Fun!!}")
print (" ")
print ("Note       : This is a Playful version of calculator made for One of my \n             Workshop sessions.")
print (" ")

input ("Press Enter for Confirmation...")
Restart = 2

while Restart ==2: 

    print (" ") 
    print ("                                 1   2   3  \n                                 4   5   6  \n                                 7   8   9  \n                                 *   0   # ")


    a= float(input("Enter the First number.."))
    b= float(input("Enter the Second number.."))
    Method = input("Enter what you have to do with these numbers ( + ,- , * , / ,% ,**) :")
    
    
    if (Method == "+" or Method == "add" or Method == "Add" or Method == "ADD" or Method == "addition" or Method == "Addition" or Method == "ADDITION"):
        print (" ")
        print ("The Addition of", a ,"and",b ,"is:", a+b)
    elif (Method == "-" or Method == "subtract" or Method == "Subtract" or Method == "SUBTRACT" or Method == "subtraction" or Method == "Subtraction" or Method == "SUBTRACTION"):
        print (" ")
        print ("The Subtraction of", a ,"and",b ,"is:", a-b)
    elif (Method == "*" or Method == "multiply" or Method == "Multiply" or Method == "MULTIPLY" or Method == "multiplication" or Method == "Multiplication" or Method == "MULTIPLICATION"):
        print (" ")
        if (a==0 or b==0):
            print ("You sure ?? You passed elementary school.. \nJust kidding.. The answer is zero (0)!! \nAnything multiplied by 0 is a 0...!!")
        else:
            print ("The Multiplication of", a ,"and",b ,"is:", a*b)
    elif (Method == "/"or Method == "divide" or Method == "Divide" or Method == "DIVIDE" or Method == "division" or Method == "Division" or Method == "DIVISION"):
        print (" ")
        print ("The Division of", a ,"and",b ,"is:", a/b)
    elif (Method == "%" or Method == "remainder" or Method == "Remainder" or Method == "REMAINDER" or Method == "modulus" or Method == "Modulus" or Method == "MODULUS"):
        print(" ")
        print ("The Remainder of", a ,"and",b ,"is:", a%b)
    elif (Method == "**" or Method == "power" or Method == "Power" or Method == "POWER"):
        print(" ")
        print ("The Power of", a ,"and",b ,"is:", a**b)    
    else:
        print(" ")
        print ("Error..!! Invalid operation..!!")  
    print (" ")

    print("Thank you" ,name.capitalize(),"for using Simple_Cal. :) ")

    Restart -=1 #Condition unmatches here
    
    value=input("Press R to Calculate again...")
    if (value=="R" or value=="r"):
        Restart +=1 #Condition matches here
    else:
        input("Press Enter to exit...!!") #Exit 
 