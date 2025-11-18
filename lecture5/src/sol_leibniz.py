import math

def leibniz(num_terms):
    total = 0
    for i in range(num_terms):
        if i%2 == 0:
            total = total + 1/(2 * i + 1)
        else:
            total = total - 1/(2 * i + 1)
    return 4.0 * total

# 以下のように書いても良い
def leibniz_if(num_terms):
    total = 0
    for i in range(num_terms):
        total = total + (-1)**i/(2 * i + 1)
    return 4.0 * total

if __name__ == '__main__':
    num_terms = 100
    error = leibniz(num_terms) - math.pi
    print(leibniz(num_terms))
    print(error)
