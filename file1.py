# 1)Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
n=int(input())
l = [i for i in range(1, n+1)]
random.shuffle(l)
print(l)
g = list(filter(lambda x: not x%2, l))
print(l, g, sum(g))

# 2) Вычислить число π c заданной точностью d.

# Первый вариант
import math
n=input()
p = str(6*math.atan(1/(3**(1/2))))
for i, x in enumerate(p):
    if x == '.':
        f1=len(p[i+1:])
for j, y in enumerate(n):
    if y == '.':
        f2=len(n[j+1:])
print(p[:f2-f1:])

# Второй вариант (можно через индексы, так компактнее)
import math
n=input()
p = str(6*math.atan(1/(3**(1/2))))
f1=len(n[n.index('.')+1:])
f2=len(p[p.index('.')+1:])
print(p[:f1-f2:])


# 3) Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
def h(j):
   return l.count(j)==1
l = [str(random.randint(1,10)) for i in range(1, 30)]
r = list(filter(h, l))
print(r)

# 4) Реализуйте алгоритм перемешивания списка (Ранее задача была решена через random.shuffle. В этот раз сделала примитивным способом)
n = int(input())
l = [i for i in range(1, n+1)]
g = [i for i in range(1, n+1) if i%2==0]
t = [i for i in range(1, n+1) if not i%2==0]
res = [x for y in zip(g, t) for x in y]
print(res)

# 5) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (ранее данное задание не было выполнено)

def main():
    rle = "WWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    encoded = encode(rle)
    decoded = decode(encoded)

    print(rle)
    print(formatOutput(encoded))
    print(decoded)

def encode(seq_elements):
    check = 1
    res = []
    for x, item in enumerate(seq_elements):
        if x == 0:
            continue
        elif item == seq_elements[x - 1]:
            check += 1
        else:
            res.append((seq_elements[x - 1], check))
            check = 1
    res.append((seq_elements[len(seq_elements) - 1], check))

    return res

def decode(seq_elements):
    res = []
    for item in seq_elements:
        res.append(item[0] * item[1])

    return "".join(res)

def formatOutput(seq_elements):
    res = []
    for item in seq_elements:
        if (item[1] == 1):
            res.append(item[0])
        else:
            res.append(str(item[1]) + item[0])

    return "".join(res)

if __name__ == "__main__":
    main()


