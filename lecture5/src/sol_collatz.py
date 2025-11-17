def collatz(n):
    print(n)
    while n != 1:
        if n%2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
        
if __name__ == '__main__':
    init_val = 3
    collatz(init_val)
    