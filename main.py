def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1
    
num = 1500

init = open(str(num) + '.csv', 'x')
init.write(str(num))
filename = num
while num != 1:
    num = collatz(num)
    print(num)
    out = open(str(filename) + '.csv', 'a')
    out.write(',\n' + str(num))
