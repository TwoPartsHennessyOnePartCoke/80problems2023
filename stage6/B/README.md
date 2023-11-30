# Аттракцион

Ограничения: время – 1s/2s, память – 10MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод

> Однажды известный автор головоломок С.Лойд, прогуливаясь со своим приятелем по ярмарке, набрел на забавный аттракцион. На полках были расставлены десять кукол, на каждой из которых было обозначено число очков (25, 27, 3, 12, 6, 15, 9, 30, 21, 19). Требовалось попасть в них небольшими мячиками. Зазывала объяснял:
>
> - Бросайте мячики столько раз, сколько захотите, по центу за каждый бросок и подходите к куклам так близко, как пожелаете. Складывайте очки на сбитых вами куклах, и, как только сумма окажется равной 50, не больше и не меньше, вы получите великолепную сигару с золотым ободком стоимостью 25 центов.
>
> Большинство игравших проигрывали деньги, не получая сигары. Но для программиста не будет сложной задачей написать программу, которая определит, какие куклы надо сбить.
>
> В первой строке входного файла – число кукол $N$ $(2 ≤ N ≤ 15)$ и сумма очков $S$ $(−10 000 000 ≤ S ≤ 10 000 000)$, которую нужно получить, во второй строке – число очков на каждой кукле. Число очков может быть в диапазоне от $−1 000 000$ до $1 000 000$.
>
> В выходной файл вывести на одной строке очки на куклах, которые надо сбить. Куклы указываются в том же порядке, как они перечислены во входном файле. Предполагается, что решение существует всегда и оно единственное.

**Пример ввода**
```
10 50
25 27 3 12 6 15 9 30 21 19
```
**Пример вывода**
```
25 6 19
```