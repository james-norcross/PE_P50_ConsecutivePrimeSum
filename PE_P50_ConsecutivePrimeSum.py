## Author: James Norcross
## Date: 2/28/15
## Description: Finds the number closest to 1M that is the sum of the greatest
## number of consecutive primes

from math import sqrt

## a prime sieve function
def makePrimeSieve(max):
    sieve = []
    
    ## initialize to true
    for i in range(max):
        sieve.append(True)
        
    ## make sieve
    sieve[0] = False
    sieve[1] = False
    sieve[2] = True
    
    imax = int(sqrt(max)) + 1
    
    for i in range(2,imax):
        if(sieve[i]):
            for j in range(2*i, max, i):
                sieve[j] = False

    return sieve

## creates a list from sieve
def listFromSieve(sieve):
    
    myList = []
    
    for i in range(0, len(sieve)):
        if (sieve[i]):
            myList.append(i)

    return myList

maxNumber = 1000000

## initialize prime sieve and list
isPrime = makePrimeSieve(maxNumber)
primes = listFromSieve(isPrime)

## minIndex and maxIndex keep track of position in primes list, primeSum tracks
## the sum of consecutive primes and answer is the maximum of primeSum obtained so far
minIndex = 0
maxIndex = 0
answer = 0
primeSum = 0
answerMinIndex = 0

## terminates when the sum of n terms primeSum is greater than the max number allowed,
## note primeSum has been adjusted appropriately at end of loop for next iteration
while(primeSum < maxNumber):
    currentPrimeSum = primeSum

    ## sum consecutive primes starting at maxIndex until sum is greater than
    ## max number, note max index at end of loop points at next prime beyond
    ## sum
    while(primeSum < maxNumber):
        primeSum += primes[maxIndex]
        maxIndex += 1

    ## make maxIndex point at last prime in sum
    maxIndex -= 1

    ## decrement sum and max index, checking for prime result, if reach point where
    ## prime sum is less than current prime sum have got to smaller number of consecutive 
    ## primes so reset prime sum to current prime sum and increase max index so that it points
    ## to last prime in current prime sum, if instead reach prime first then that needs to be
    ## compared to answer to see if it is larger and answer reset if appropriate
    while(True):
        primeSum -= primes[maxIndex]
        maxIndex -= 1
        if(primeSum < currentPrimeSum):
            primeSum = currentPrimeSum
            maxIndex += 1
            break
        elif(isPrime[primeSum]):
            if(primeSum > answer):
                answer = primeSum
                answerMinIndex = minIndex
            break

    ## continue searching for numbers closer to max number that are
    ## sums of at least this many elements by subtracting prime at minIndex
    ## from prime sum and adding next element at max end, increment minIndex and
    ## maxIndex so they point at beginning of new sum and first term to be added
    ## and repeat while loop
    primeSum = primeSum - primes[minIndex] + primes[maxIndex + 1]
    minIndex += 1
    maxIndex += 2

print "The prime closest to %d which is the sum of the most consectutive primes is %d" % (maxNumber, answer)
print "This is the result of summing %d primes starting at %d" % (maxIndex - minIndex, primes[answerMinIndex])

