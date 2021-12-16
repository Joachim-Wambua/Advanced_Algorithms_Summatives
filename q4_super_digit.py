# Question 4 Super Digit Function
#  Author: Joachim Wambua

# Recursive function to calculate the super sum of a digit
def super_digit(x, k):
    # Initialising necessary variables
    num_string = str(x)
    p = int(num_string*k)
    p_str = str(p)
    digit_len = len(str(p))
    total_sum = 0
    final_sum = 0
    _sum = 0

    # If number has one digit
    if digit_len == 1:
        # Return the single digit
        return x
    else:
        # Loop through numbers array adding the elements to total sum
        for index in range(0, digit_len):
            total_sum = (total_sum + int(p_str[index]))

        # If the total sum is > 10 i.e a 2 digit number
        if total_sum >= 10:
            y = str(total_sum)
            for i in y:
                final_sum = final_sum + int(i)
            if final_sum >= 10:
                z = str(final_sum)
                for j in z:
                    _sum = _sum + int(j)
                return _sum
            else:
                return final_sum
        elif total_sum < 10:
            return total_sum


if __name__ == '__main__':
    n = 75757575
    k = 3
    print('Value of n = ' + str(n))
    print('Value of k = ' + str(k))
    print('Super Digit = ' + str(super_digit(n, k)))
    # print(super_digit(9875, 4))
    # print(super_digit(25, 2))
    # print(super_digit(75, 3))
