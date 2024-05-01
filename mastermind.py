from random import randint

def checkInput(input):
    inputCorrect = False
    for i in range(0, len(input)):    
        try:
            val = int(input[i])
            inputCorrect = True
        except ValueError:
            inputCorrect = False
            break
    return inputCorrect

def mastermind():
    nums = [randint(1,5), randint(1,5), randint(1,5), randint(1,5)]
    print(*nums)
    print('Welcome to mastermind! The computer has generated 4 random numbers in a row. Can you guess all correctly? You have 10 attempts. Good luck!')
    attempt = 1
    while(attempt <= 10):
        inputNums = []
        for i in range(1,5):
            inputNums.append(input('Input number ' + str(i) + ': '))       
        if(checkInput(inputNums) == False):
            print('input error')
            break
        for i in range(0,4):
            inputNums[i] = int(inputNums[i])
        print('Inputted values:')
        print(*inputNums)
        matching = 0
        correct = 0
        for i in range(0, len(nums)):
            if(nums[i] == inputNums[i]):
                matching += 1
                correct += 1
            else:
                for y in range(0, len(inputNums)):
                    if(nums[i] == inputNums[y]):
                        correct += 1
                        inputNums[y] = 0 #eliminate the input so it cannot be used multiple times
                        break
                
        print('Total correct numbers: ' + str(correct))
        print('Total matching position numbers: ' + str(matching))
        if(correct == 4 and matching == 4):
            print('You won!')
            break
        elif(attempt == 10):
            print('You lost!')
        attempt += 1
        
mastermind()