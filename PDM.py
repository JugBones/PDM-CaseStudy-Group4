def calculate_salary():
    x = 0
    y = 0
    #inputing the numbers
    while x<=0:
        x = int(input("input number of overtime: "))
        if x > 0 and x<=20:
            break
        print("Should be an integer between 0 and 21")
    while y<=0:    
        y = int(input("input level of allowance: "))
        if y > 0 and y<=3:
            break
        print("Should be an integer between 0 and 4")

    #finding how many percent
    if y == 1:
        percent = 5
    if y == 2:
        percent = 10
    if y == 3:
        percent = 15

    #counting the salary



        result = 110000 * x
        result = result + 3800000*percent/100 + 3800000

    def group(number):#Adding zero for Thousands
        s = '%d' % number
        groups = []
        while s and s[-1].isdigit():
            groups.append(s[-3:])
            s = s[:-3]
        return s + '.'.join(reversed(groups))

    print("Total Salary: {}".format(group(result)))

if __name__ == '__main__':
    calculate_salary()