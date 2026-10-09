def is_Even(number):
	if(number % 2 == 0):
		return True
	else:
		return False
	



def is_prime(number):
	if number <= 2:
		return False
	
	for index in range(2, number):
		if(number % index == 0):
			return False

	return True
	



def subtract(numberOne, numberTwo):
	if(numberOne > numberTwo):
		return numberOne - numberTwo
		
	else:
		return numberTwo - numberOne
		



def divide(numberOne, numberTwo):
	if(numberTwo == 0):
		return 0
	else:
		return numberOne / numberTwo
		

def factor_of(number):
	count = 0
	for index in range(1, number + 1):
		if(number % index == 0):
			count = count + 1
	return count
	


def is_square(number):
	if number < 0:
		return false
	for index in range(0, number):
		if(index * index == number):
			return True
	else:
		return False
			

def is_palindrome(number):
	original = number
	reverse = 0
	
	while number > 0:
		digit = number % 10
		reverse = reverse * 10 + digit
		number = number // 10
	if original == reverse:
		return "its a palindrome"
	else:
		return "its not a palindrome"
	
	
	
def factorial_Of(number):
    result = 1
    for index in range(1, number + 1):
        result = result * index

    return result



def square_of(number):
	return number * number
