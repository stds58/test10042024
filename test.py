# Задание в Python:
# 1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.

def list_unique(L:list):
    try:
        summa = sum(L)
        if isinstance(summa, int):
            result = list(set(L))
        else:
            result = 'в списке есть дробные числа'
    except TypeError:
        result = 'в списке есть строки либо числа отформатированные как строки'
    return result

L = [1,2,0,0,1,1,2,]
result = list_unique(L)
print(result)

# 2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.

def get_diapazon(int1, int2):
    L=[]
    if isinstance(int1, int) and isinstance(int2, int):
        for i in range(int1, int2+1):
            L.append(i)
        result=L
    else:
        result = 'одно либо два числа не являются целыми числами'
    return result

result = get_diapazon(4,16)
print(result)

# 3. Создать класс Point, который представляет собой точку в двумерном пространстве.
# Класс должен иметь методы для инициализации координат точки,
# вычисления расстояния до другой точки, а также для получения и изменения координат.

class Point():
    def __init__(self, x, y):
        self.x = self.set_value(x)
        self.y = self.set_value(y)

    def set_value(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = None
        return self.value

    def get_length(self, x2, y2):
        coord1 = abs(self.x - x2)
        coord2 = abs(self.y - y2)
        length = (coord1**2 + coord2**2)**0.5
        return length

k1 = Point(-1,-1)
k2 = Point(1,1)
length = k1.get_length(k2.x, k2.y)
print('length1',length)
k2.x = 3
length = k1.get_length(k2.x, k2.y)
print('length2',length)


# 4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.

def list_sort(L:list):
    result = sorted(L,key=len)
    result_reverse = sorted(L, key=len, reverse=True)
    return result, result_reverse

L = ['dd', 'f', 'dddd', 'dde']
result,result_reverse = list_sort(L)
print(result,result_reverse)