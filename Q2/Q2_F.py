def is_valid(n):
    if 6999 > n > 1000:
        sum_of_num = 0
        for i in str(n):
            sum_of_num += int(i)
        if sum_of_num % 7 == 0:
            return True
    return False


Id = int(input('enter your id number (e.g. 1234): '))
print(is_valid(Id))
