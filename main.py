# задание 1

def uniqueNumbers(n):
    n = set(n)
    return len(n)

n = input("Введите числа через пробел: ")
list = list(map(int, n.split(' ')))

result = uniqueNumbers(list)
print("Количество различных чисел:", result)

# задание 2
def subset(set1, set2):
    if set1 == set2:
        return False
    else:
        return set1.issubset(set2)

n1 = input("Введите элементы первого множества через пробел: ")
set1 = set(map(int, n1.split(' ')))

n2 = input("Введите элементы второго множества через пробел: ")
set2 = set(map(int, n2.split(' ')))

result = subset(set1, set2)
print(result)

# задание 3
def checkCity(cities, pastCities):
    if currentCity in pastCities:
        return "REPEAT"
    else:
        pastCities.add(currentCity)
        return "OK"

n = int(input("Введите количество названных городов: "))

print("Введите названный город или города: ")
pastCities = [input() for i in range(n)]

currentCity = input("Введите новый город: ")
result = checkCity(pastCities, currentCity)
print(result)
