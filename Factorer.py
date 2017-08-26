
print ("**Welcome to the factorer**\n\n")
number = int( input("Enter a number to factor\n:"))
while number <=1:
    number = int( input("Please enter a positive integer\n:"))

initialNumber = number

factors = []
primeList = []
'''
# creates list primeList that contains all primes such that the largest prime squared is smaller than the number to factor
def GeneratePrimeList (number, primeList):
    currentPrime = 2
    # finds primes such that largest prime squared is smaller than number
    while number >= currentPrime**2:
        isPrime = 1
        for i in primeList:
            # checks if number is prime
            if currentPrime%i == 0:
                # number isn't prime
                isPrime = 0
                break
        if isPrime == 1:
            primeList.append(currentPrime)
        currentPrime += 1

GeneratePrimeList(number, primeList)

while ____:
    for i in primeList:
        if number%i == 0:
            factors.append(i)
            number = number/i
'''


currentPrime = 2
# finds primes such that largest prime squared is smaller than number
while number >= currentPrime**2:
    isPrime = 1
    for i in primeList:
        # checks if number is prime
        if currentPrime%i == 0:
            # number isn't prime
            isPrime = 0
            break
    if isPrime == 1:
        primeList.append(currentPrime)
        while number%currentPrime == 0:
            factors.append(currentPrime)
            number = number/currentPrime
    currentPrime += 1



if number == 1:
    print ("\n\nYour number, {0}, has the following factors:".format(initialNumber))
    for i in factors:
        print (i)
else:
    try:
        print ("\n\nYour number, {0}, has the following factors".format(initialNumber))
        for i in factors:
            print (i)
        print (int(number))
    except IndexError:
        print("Your number, {0}, is prime".format(int(number)))





# check if number has a factor of prime numbers
#while number > primeFactorCheck**2:
    #while primeFactorCheck