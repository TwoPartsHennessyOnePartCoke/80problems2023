# Потерянное место

*Ограничения: время – 1s/2s, память – 32MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод*

> Когда файлы сохраняются на диске, они хранятся в кластерах, имеющих фиксированный размер. Фактическое место, занимаемое файлом на диске, всегда кратно размеру кластера. Так, если кластер имеет размер 100 байт, а файл – 185 байт, то файл занимает 200 байт на диске, и 15 байт на диске являются потерянными.
>
> Напишите программу, выполняющую расчет потерянного места на диске для каждой папки с файлами.
>
> В первой строке входного файла содержатся три целых числа, разделенных пробелами – количество папок на диске $N$ $(0 < N ≤ 50)$, количество файлов на диске $M$ $(0 ≤ M ≤ 1000)$ и размер кластера $S$ $(0 < S ≤ 1000000)$. Далее следует $M$ строк, в каждой строке содержатся два целых числа, разделенных пробелом – номер папки $F$ $(0 ≤ F < N)$, в которой находится файл, и размер файла $Z$ $(0 ≤ Z ≤ 1000000)$. Папки нумеруются от $0$ до $N−1$.
>
> В выходной файл вывести $N$ строк. В $i$-й строке выводится одно целое число – сумма потерянного места при размещении файлов $(i−1)$-ой папки (для $i$ от $1$ до $N$).

**Пример ввода**
```
3 3 50
0 55
0 47
1 86
```
**Пример вывода**
```
48
14
0
```

Примечание к примеру: так как в папке с номером 2 файлов нет, то и потери равны 0.
