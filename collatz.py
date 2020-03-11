def collatz(number):
    if(number % 2 == 0):
        print(int(number / 2))
    else:
        print(3 * number + 1)

print('Please enter a number...')

try:
    number = int(input())
    collatz(number)  
except ValueError:
    print('Please enter an integer!')
  

        
