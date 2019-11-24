n=int(input())
k=int(input())

def printPattern(n, k, currentNumber, direction):
    if (currentNumber == n and direction == -1):
        print (currentNumber, end='')
    else :
        print (currentNumber, end=', ')
        if (currentNumber <= 0 ) :
            printPattern(n, k, currentNumber + (direction * k), -direction)
        else :
            printPattern(n, k, currentNumber - (direction * k), direction)

printPattern(n, k, n, 1)
