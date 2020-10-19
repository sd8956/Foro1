"""
Process to find the values of x so that a
third degree function is equal to 0
"""

def get_divisors(number):
    """Get the divisors of a number"""
    divisors = set()

    for i in range(1, abs(number) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(i * -1)

    return divisors


def get_possible_values(p, q):
    """Get the posible values to examine"""
    pq = set()
    for i in q:
        for j in p:
            pq.add(j / i)

    return pq


def synthetic_division(pq, coef):
    """Make the synthetic division"""
    values = set()

    first_coef = coef.pop(0)

    for i in pq:
        temp_product = i * first_coef
        results = []
        for j in coef:
            stay = j + temp_product
            results.append(stay)
            temp_product = i * stay

        if results[-1] == 0:
            values.add(i)
            
    return values


def get_values(ind_term, max_coef):
    """Get the values of X so that f(x) is equal to 0"""
    p = get_divisors(ind_term)
    q = get_divisors(max_coef)

    pq = get_possible_values(p, q)
    return pq


if __name__ == "__main__":

    print("Ingrese el valor del termino independiente: ")
    ind_term = int(input())

    print("Ingrese el valor del coeficiente principal / termino de mayor exponente: ")
    max_coef = int(input())

    pq = get_values(ind_term, max_coef)
    
    print("Ingrese los coeficientes en orden descendente de la ecuación separados por comas")
    coefs = list(map(int, input().split(","))) 
    
    values = synthetic_division(pq, coefs)
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Los valores para que la funcion sea igual a 0 son: ", values)
    print("--------------------------------------------------------------------------------------------------------------------------")
