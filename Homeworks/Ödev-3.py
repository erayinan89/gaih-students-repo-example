def prime_first():
    for sayi in range(0,500):
        if sayi > 1:
            for i in range(2,sayi):
                if (sayi % i) == 0:
                    break
            else:
                print(sayi)


def prime_second():
    for sayi2 in range(500,1000):
        for i in range(2,sayi2):
            if (sayi2%i) == 0:
                break
        else:
                print(sayi2)

prime_first()
prime_second()


