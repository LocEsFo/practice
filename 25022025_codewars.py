def fibonacci_recursive(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def product_fib(_prod):
    proiz = 0
    mass = []
    i = 0
    while proiz <= _prod:
        proiz = fibonacci_recursive(i) * fibonacci_recursive(i + 1)
        if proiz == _prod:
            mass.append(fibonacci_recursive(i))
            mass.append(fibonacci_recursive(i+1))
            mass.append(True)
            return mass
            break
        elif proiz > _prod:
            mass.append(fibonacci_recursive(i))
            mass.append(fibonacci_recursive(i+1))
            mass.append(False)
            return mass
            break
        i +=1
        
        
