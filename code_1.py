def sqrt(a,b):
    try:
        a = float(a)
        b = float(b)
        if (a + b) < 0:
            return ('Компл область')
        else:
            n = (((a+b)**3)/((a-b)**2)) ** (1/2)
    except ZeroDivisionError:
        return 'Не дели блет на 0'
    except (TypeError, ValueError):
        return ('А нормально ввести можно было')
    else:
        return round(n, 4)


def main():
    try:
        usr_a = float(input())
        usr_b = float(input())
    except (TypeError, ValueError):
        print ('А нормально ввести можго было')
    else:
        print(sqrt(usr_a,usr_b))


if __name__ == '__main__':
    main()






