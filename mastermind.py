from random import randint
import re
game = True
def checkInput(input):
    inputCorrect = False
    for i in range(0, len(input)):    
        try:
            val = int(input[i])
            inputCorrect = True
            if(val < 1 or val > 6):
                inputCorrect = False
                break
        except ValueError:
            inputCorrect = False
            break
    return inputCorrect

def mastermind():
    nums = []
    for i in range(0,4):
        num = randint(1,6)
        while num in nums:
            num = randint(1,6)
        nums.append(num)
    print('Welcome to mastermind! The computer has generated 4 random numbers in a row. Can you guess all correctly? You have 10 attempts. Good luck!')
    attempt = 10
    while(attempt > 0):
        print(*nums) #for debug 
        inputStr = input("Enter numbers separated by commas, spaces, or both: ")
        inputNums = re.split(r'[,\s]+', inputStr.strip())    
        if(checkInput(inputNums) == False or len(inputNums) != 4):
            print('input error')
            break
        for i in range(0,4):
            inputNums[i] = int(inputNums[i])
        print('\n Inputted values:')
        print(*inputNums)
        matching = 0
        correct = 0
        for i in range(0, len(nums)):
            if(nums[i] == inputNums[i]):
                matching += 1
                correct += 1
                continue
            elif(inputNums[i] in nums):
                correct += 1        
        print('Total correct numbers: ' + str(correct))
        print('Total matching position numbers: ' + str(matching))
        attempt -= 1
        if(correct == 4 and matching == 4):
            print('You won!')
            break
        elif(attempt <= 0):
            print('You lost!')
        print(str(attempt) + ' attempts left \n')
while game is True:
    mastermind()
    ans = input('Wanna play again? ')
    if(ans == 'y' or ans == 'yes' or ans ==''):
        game = True
    else:
        game = False