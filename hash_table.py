
hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

#To prove whether a number is a prime number, first try dividing it by 2, and see if you get a whole number. If you do, it can't be a prime number. 
#A whole number is simply any positive number that does not include a fractional or decimal part.

    for i in range(2, n//2):
        if n % i == 0:
            return 0
    return 1

def getPrime(n):
    if n % 2 == 0:
        n += 1

    while not checkPrime(n):
        n += 2

    return n

def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity

def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = 0

insertData(123, "apple")
insertData(432, "aporn")
insertData(213, "aped")
insertData(654, "ape")

print(hashTable)






#Hash tables are implemented where

    #constant time lookup and insertion is required
    #cryptographic applications
    #indexing data is required

