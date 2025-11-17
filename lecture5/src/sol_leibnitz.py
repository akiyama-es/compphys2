import math

def leibnitz(num_terms):
    total = 0
    for i in range(num_terms):
        if i%2 == 0:
            total = total + 1/(2 * i + 1)
        else:
            total = total - 1/(2 * i + 1)
    return 4.0 * total

# 以下のように書いても良い
def leibnitz_if(num_terms):
    total = 0
    for i in range(num_terms):
        total = total + (-1)**i/(2 * i + 1)
    return 4.0 * total

if __name__ == '__main__':
    num_terms = 100
    error = leibnitz(num_terms) - math.pi
    print(leibnitz(num_terms))
    print(error)
