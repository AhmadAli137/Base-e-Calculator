import math

print("==========================================")
print("Welcome to the Exponent-Base-e Calculator:")
print("------------------------------------------")
print("              by Ahmad Ali                ")
print("           (BorderHacks 2020)             ")
print("------------------------------------------")

exp = float(input("         Enter your exponent: "))
Es = float(input("    Enter your error tolerance: "))
print("------------------------------------------")

n = 1
sol = 1
Repeat = True
while Repeat == True:
	solOld = sol
	sol = 1
	n = n + 1
	for i in range(n):
		sol += (((exp)**(i+1))/(math.factorial(i+1)))

	Ea = 100*(sol - solOld)/sol #approximation error

	if Ea < Es: 
		Repeat = False

exponent_base_e = sol
print("Answer: "+str(exponent_base_e))
print("==========================================")


