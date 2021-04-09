def nomer3():
    bawah = 10
    batas = 25

    for num in range(bawah, batas):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print(num, 'bukan bilangan prima')
                    break
            else:
                print(num, 'bilangan prima')

nomer3()