# Отпуск программиста

*Ограничения: время – 1s/2s, память – 16MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод*

> После многих лет беспрерывной работы программист собрался наконец-то взять $N$ дней отпуска. Во время отпуска он решил сходить в поход продолжительностью $L$ дней.
>
> Программист нашёл интернет-сайт с прогнозом погоды и выяснил для каждого дня отпуска прогнозируемую вероятность дождя $a_i$. Он решил выбрать для похода такие дни, что в день выхода и в день возвращения наверняка будет солнечно (вероятность дождя равна нулю), а сумма вероятностей дождя в промежуточные дни будет минимальной.
>
> Требуется определить оптимальный период для похода или выяснить, что сходить в поход не удастся. Если существует несколько оптимальных вариантов, следует вывести тот, который начинается раньше.
>
> Ввод
>
> Входной файл содержит числа $N$ $L$, за которыми следует $N$ целых чисел $a_i$ – вероятности дождя в процентах.
>
> Вывод
>
> В выходной файл должно быть выведено единственное число – номер первого дня похода, либо `−1`, если поход невозможен.
>
> *Ограничения*
> $1 ≤ L ≤ N ≤ 31$, $0 ≤ a_i ≤ 100$

**Пример ввода 1**
```
4 2
50 0 0 10
```
**Пример вывода 1**
```
2
```
**Пример ввода 2**
```
7 3
0 75 64 30 0 0 100
```
**Пример вывода 2**
```
-1
```
**Пример ввода 3**
```
10 4
0 0 1 2 0 3 4 0 100 0
```
**Пример вывода 3**
```
2
```

*Источник: А. Кленин, ДВГУ, Весенний турнир, 2005*
