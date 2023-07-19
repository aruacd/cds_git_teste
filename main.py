def gather_data():
    n1 = int(input("Primeiro valor: "))
    n2 = int(input("Segundo valor: "))
    op = input("Operação: ")

    return n1, n2, op

def main():
    n1, n2, op = gather_data()

    print(eval(n1+op+n2))

    return none

if __name__ == "__main__":
    main()