# Дождь

*Ограничения: время – 1s/2s, память – 32MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод*

> Капля дождя падает вертикально вниз с большой высоты на землю. На пути у капли могут встретиться препятствия, которые изменяют ее путь к земле.
>
> Будем рассматривать двумерный вариант (на плоскости) этой задачи. Пусть препятствия – это наклонные непересекающиеся отрезки, а капля имеет точечные размеры. Капля падает вертикально вниз из точки, расположенной выше любого из препятствий. Если капля при падении соприкасается с отрезком-препятствием, то она стекает по отрезку вниз, пока не упадет вертикально вниз с меньшего по высоте конца отрезка. Напишите программу, которая по координате $X_0$ точки появления капли над землей вычисляет координату X точки соприкосновения капли с землей $(Y = 0)$.
>
> Во входном файле в первой строке содержатся два целых числа через пробел – координата $X_0$ точки появления капли $(0 < X_0 < 10000)$ и количество отрезков-препятствий $N$ $(0 ≤ N ≤ 100)$. Далее следует $N$ строк, каждая из которых содержит четыре разделенные пробелами числа $x_1$, $y_1$, $x_2$, $y_2$ – координаты левого и правого концов отрезка-препятствия (все числа целые и находятся в диапазоне от 0 до 10000, $x1 < x2, y1 ≠ y2$). Отрезки не пересекаются и не соприкасаются.
>
> В выходной файл вывести одно целое число – координату $X$ точки соприкосновения капли с землей.
>
> ![](https://ipc.susu.ru/7824.gif)

**Пример ввода**
```
30 4
25 35 40 30
1 32 20 30
33 22 50 29
18 10 33 19
```
**Пример вывода**
```
18
```
