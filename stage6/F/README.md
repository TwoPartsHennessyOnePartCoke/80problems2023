# Шушанчики и кроссворд

*Ограничения: время – 2s/4s, память – 64MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод*

> Одно из любимых развлечений шушанчиков – разгадывание кроссвордов. Однажды им на глаза попался обрывок журнальной страницы, содержащий вопросы к кроссворду. Весь день они потратили на разгадывание слов. И лишь на следующий день им удалось найти вторую часть страницы, на которой была изображена схема кроссворда.
>
> Схема кроссворда задается прямоугольной таблицей символов шириной $W$ и высотой $H$. Пустые клетки, в которые следует вписывать буквы, обозначаются символом '`#`' (ASCII 35). Остальные клетки обозначаются символами '`.`' (ASCII 46).
>
> Загаданное слово в кроссворде представляется в виде последовательности из трёх или более символов '#', идущих подряд слева направо или сверху вниз, ограниченной в начале и в конце либо краями кроссворда, либо символами '`.`'.
>
> Загаданные слова на схеме не пронумерованы. Вместо этого они упорядочиваются следующим образом. Слова по горизонтали перечисляются перед словами по вертикали. Слова одного направления отсортированы по положению первых букв в кроссворде: сначала по номеру строки (сверху вниз), затем, при равенстве номеров строк, по номеру столбца (слева направо).
>
> Теперь шушачики хотят проверить, правильно ли они решили кроссворд.
>
> Напишите программу, которая по заданному кроссворду определяет, является ли заданный набор слов его корректным решением. Слово в решении является корректным, если оно совпадает по длине с соответствующим загаданным словом и содержит в клетках, общих с ранее вписанными словами, те же самые буквы, что и предыдущие слова.
>
> Ввод
>
> В первой строке входного файла содержатся числа $W$ и $H$. Следующие $H$ строк по $W$ символов каждая описывают кроссворд.
>
> В $(H + 2)$-й строке находится число слов $N$, за которым по одному в строке следуют слова, составляющие предполагаемое решение кроссворда в порядке, соответствующем загаданным словам.
>
> Вывод
>
> В единственной строке выходного файла должна содержаться строка CORRECT, если кроссворд решен правильно, или первое в порядке перечисления в файле слово, на котором нарушается корректность решения – в противном случае.
>
> Ограничения
>
> $3 ≤ W, H ≤ 500, 1 ≤ N ≤ 30000$.
>
> Длина любого слова в кроссворде и в его решении – от 3 до 250 символов. Слова состоят только из маленьких латинских букв. Число слов $N$ совпадает с числом загаданных слов в кроссворде.

**Пример ввода 1**
```
8 7
..#.#...
#######.
..#.#...
..#####.
..#.#...
..#.#...
..#.####
5
program
table
math
contest
problem
```
**Пример вывода 1**
```
CORRECT
```
**Пример ввода 2**
```
8 7
..#.#...
#######.
..#.#...
..#####.
..#.#...
..#.#...
..#.####
5
program
table
math
cantest
problem
```
**Пример вывода 2**
```
cantest
```

*Источник: И. Бураго, ДВГУ, Весенний турнир, 2007*
