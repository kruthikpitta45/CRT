def Ticket_Pricing(n: int) -> int:
    if n<5:
        print("Free")
    elif  n>=5 and n<=17:
        print(10)   
    elif n>=18 and n<=64:
        print(20)
    else:
        print(15)


if __name__ == '__main__':
    n = int(input())
    print(Ticket_Pricing(n))
