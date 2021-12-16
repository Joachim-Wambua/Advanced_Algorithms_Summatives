# Q1: Program to find sum of first n numbers
# Author: Joachim Wambua

def add_sequential_nos(n):
    # Create variable to hold sum of n numbers
    sum = 0
    # Loop through the numbers adding them to sum
    while n > 0:
        sum += n
        n -= 1
    # Return Final Sum
    return sum


# Main Flow
if __name__ == '__main__':
    print('----FIND SUM OF N NUMBERS---- ')
    user_input = int(input('Enter a positive number: '))

    result = add_sequential_nos(user_input)
    print('Total sum of first ' + str(user_input) + ' numbers is: ' + str(result))
