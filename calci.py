print("Basic calculator")
print("1.Addition","2.Subraction","3.Multiplication","4.Division")
while True:
	operation = int(input("Enter your choice of operation::"))
	num1 = int(input("Enter the value1::"))
	num2 = int(input("Enter the value2::"))
	if operation ==1:
		print(num1+num2)
	elif operation ==2:
		print(num1-num2)
	elif operation == 3:
		print(num1*num2)
	elif operation == 4:
		print(num1/num2)
	else:
		print("Invalid number")
	break
