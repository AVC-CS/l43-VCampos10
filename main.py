def main():
    num = []
    i = 0; total = 0
    while(i<5):
        num = int(input('Enter your number here: '))
        total += num
        i += 1
    print(total)

    return total


if __name__ == '__main__':
    main()
