if __name__ == '__main__':
    print("Введите число:")
    n = int(input().strip())

if n % 2 != 0:              #проверка на чётное
    print("Weird")
else:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")