# Замена скобок: выполнение алгоритма

Ограничения: время – 1s/2s, память – 64MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод

> Рассмотрим последовательность из открывающихся и закрывающихся круглых скобок. Назовём такую последовательность скобочной.
>
> Рассмотрим следующий алгоритм: на каждом шаге выбирается подстрока скобочной последовательности и все скобки в ней заменяются на противоположные, т.е. все символы '`(`' в этой подстроке заменяются на '`)`', а все символы '`)`' – на '`(`'.
>
> Требуется написать программу, которая по входной скобочной последовательности длиной $L$ и описанию алгоритма из $N$ шагов выведет результат его выполнения.
>
> Ввод
>
> В первой строке входного файла содержится исходная последовательность.
>
> Во второй строке содержится число $N$.
>
> В каждой из последующих $N$ строк содержится по два числа $l_i$ $r_i$, задающих позиции первого и последнего символа подстроки, в которой на $i$-ом шаге меняются скобки.
>
> Вывод
>
> В выходном файле должна содержаться единственная строка – результат работы алгоритма.
>
> Ограничения
>
> $1 ≤ N, L ≤ 10^5$, $1 ≤ l_i ≤ r_i ≤ L$

**Пример ввода 1**
```
(((((
1
1 5
```
**Пример вывода 1**
```
)))))
```
**Пример ввода 2**
```
((())(()
3
1 8
2 6
4 7
```
**Пример вывода 2**
```
)(((()((
```

*Источник: А. Жуплев, ДВГУ, Весенний турнир, 2007*