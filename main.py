'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
    '''
    Programul verifica daca un numar este prim
    :param n: int, numarul despre care vrem sa stim daca este prim
    :return: True, daca numarul este prim
             False, daca numarul nu este prim
    '''


    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
                break
        else:
            return True

    # Daca numarul introdus este mai mic sau egal cu 1, acesta nu este prim

    else:
        return False

assert is_prime(7) == True
assert is_prime(11) == True
assert is_prime(13) == True
assert is_prime(63) == False



'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    '''
            Calculeaza produsul a n numere din lista
            :param lst: se va lua ca punct de pornire o lista de numere, al caror produs vrem sa il determinam
            :return: produsul numerelor
            '''

    # Se inmultesc elementele din lista unul cate unul

    # Initializam rezultatul cu 1

    p = 1
    for i in range(0,len(lst)):
        p = p * lst[i]
    return p


assert get_product([1, 2, 3]) == 6
assert get_product([3, 2, 4]) == 24




'''
Returneaza CMMDC al doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
        '''
        Determina CMMDC al doua numere x si y
        :param x : int, primul numar
        :param y : int, al doilea numar
        :return: CMMDC al doua numere
        '''
        while (x != y):
            if (x > y):
                x = x - y
            else:
                y = y - x
        return x

assert get_cmmdc_v1(12, 4) == 4
assert get_cmmdc_v1(45, 30) == 15
assert get_cmmdc_v1(24, 126) == 6



'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
        '''
        Determina CMMDC al doua numere x si y
        :param x : int, primul numar
        :param y : int, al doilea numar
        :return: CMMDC al doua numere
        '''

        rest = 0
        while (y != 0):
            rest = x % y
            x = y
            y = rest
        return x

assert get_cmmdc_v2(12, 4) == 4
assert get_cmmdc_v2(45, 30) == 15
assert get_cmmdc_v2(24, 126) == 6



def print_menu():
    print("1.Număr prim")
    print("2.Produsul a n numere")
    print("3.CMMDC al două nr. x și y folosind primul algoritm")
    print("4.CMMDC al două nr. x și y folosind al doilea algoritm")
    print("x.Ieșire")

def main():
    while True:
        print_menu()
        option=input("Alege opțiunea:")
        if option =="1":
            n = int(input("Introduceți un număr:"))

            if is_prime(n):
                print(n, "este număr prim")
            else:
                print(n, "nu este număr prim")
        elif option =="2":
            n = int(input("n="))
            lst = []
            for i in range(0,n):
                i= int(input())
                lst.append(i)
            print(lst)
            print(len(lst))
            print('Produsul este =',get_product(lst))
        elif option =="3":
            x = int(input("x="))
            y = int(input("y="))
            print('CMMDC este:',get_cmmdc_v1(x,y))
        elif option =="4":
            x=int(input("x="))
            y = int(input("y="))
            print('CMMDC este:',get_cmmdc_v2(x,y))
        elif option =="x":
            break
        else:
            print("Opțiune invalidă")

main()

