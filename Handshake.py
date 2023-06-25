def handshake(n):
    k = n-1
    return k*(k + 1)/2

if __name__ == "__main__":
    num = int(input("Enter number of people participating: "))
    print(handshake(num))
    