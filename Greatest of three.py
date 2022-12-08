#Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
x, y,z= [int(x) for x in input("Enter Three values: ").split()] 
if(x>y>z):
        print(x,"is the greatest ")
elif(y>z>x):
        print(y,"is the greatest")
else:
    print(z,"is the greatest")
