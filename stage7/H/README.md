# Составление числа

*Ограничения: время – 2s/4s, память – 32MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод*

> $N$ карточек были пронумерованы числами от $0$ до $N−1$. Несколько карточек положили в ряд, чтобы получилось число. Напишите программу, которая из оставшихся карточек составит такое же число.
>
> Ввод
>
> В первой строке входного файла содержатся два целых числа, разделенных пробелом – количество карточек $N$ $(10 ≤ N ≤ 1000)$ и количество отобранных карточек $K$ $(1 ≤ K ≤ 10)$. Во второй строке входного указано $K$ различных целых чисел в диапазоне от $0$ до $N−1$, разделенных пробелами – номера на отобранных карточках.
>
> Вывод
>
> В выходной файл в первой строке вывести число M – количество карточек, взятых для составления такого же числа. Во второй строке вывести, разделяя пробелом, номера на этих карточках. Если существует несколько вариантов, можно вывести любой из них. Если составить такое же число невозможно, то в первой строке вывести число –1 .

**Пример ввода**
```
1000 3
11 45 99
```
**Пример вывода**
```
2
114 599
```
