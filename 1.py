def fibonacci_recursive(n):
    """Рекурсивная функция для вычисления n-го числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

_prod = 5895
proiz = 0
mass = []
i = 0
while proiz <= _prod:
    proiz = fibonacci_recursive(i) * fibonacci_recursive(i + 1)
    if proiz == _prod:
        mass.append(fibonacci_recursive(i))
        mass.append(fibonacci_recursive(i+1))
        mass.append(True)
        break
    elif proiz > _prod:
        mass.append(fibonacci_recursive(i))
        mass.append(fibonacci_recursive(i+1))
        mass.append(False)
        break
    i +=1
print(mass)
        
        
