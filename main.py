def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1
    
num = 150

init = open('outputs/' + str(num) + '.csv', 'x')
init.write(str(num))
filename = num
init.close()

while num != 1:
    num = collatz(num)
    print(num)
    out = open('outputs/' + str(filename) + '.csv', 'a')
    out.write(',\n' + str(num))
    out.close()
