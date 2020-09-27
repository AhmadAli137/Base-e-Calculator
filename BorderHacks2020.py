import math #library for math operation such as factorials

print("==============================================")
print("Welcome to the Exponent-Base-e Calculator:")
print("----------------------------------------------")
print("              by Ahmad Ali                ") #Prompts
print("           (BorderHacks 2020)             ")
print("----------------------------------------------")

exp = float(input("         Enter your exponent: "))
sd = int(input(" Enter number of correct significant digits: ")) #User input
print("----------------------------------------------")

n = 1
sol = 1
Es = (0.5*10**(2-sd)) #formula to calculate error tolerance given number of significant digits
print("Error Tolerance: "+str(Es)+"%")


#Loop represents algorithm for a numerical calculation which
#                  becomes increasingly accurate with each iteration

# This calculation is only approximate to analytical calculation which has an infinite process
                                                       
Repeat = True
while Repeat == True:
	solOld = sol
	sol = 1
	n = n + 1
	for i in range(n):
		sol += (((exp)**(i+1))/(math.factorial(i+1)))

	Ea = 100*(sol - solOld)/sol #Calculating approximation error between interations

	if Ea < Es: 
		Repeat = False #loop ends once approximation error is below error tolerance

exponent_base_e = sol
print("Answer: "+str(exponent_base_e))
print("[correct to at least "+str(sd)+ " significant digits] ") #User Output
print("==============================================")


