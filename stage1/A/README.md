# Серое королевство

Ограничения: время – 200ms/500ms, память – 64MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод

> В Сером королевстве запрещены все цвета. Жители королевства могут использовать только варианты серого цвета от черного до белого. Если рассмотреть цвет с использованием модели RGB, где каждый из трех каналов принимает значение от 0 до 255, то в Сером королевстве разрешены только цвета, у которых разница между значениями в любой паре каналов не превышает 25.
>
> Напишите программу, которая определяет для цвета, заданного в модели RGB, является ли он разрешенным в Сером королевстве.
>
> Первая строка ввода содержит три целых числа в диапазоне от 0 до 255 — значения в каналах R, G и B.
>
> Вывести сообщение `ALLOWED`, если цвет является разрешенным в Сером королевстве, иначе выведите сообщение `FORBIDDEN`.

**Пример ввода 1**
```
120 145 135
```
**Пример вывода 1**
```
ALLOWED
```
**Пример ввода 2**
```
100 140 135
```
**Пример вывода 2**
```
FORBIDDEN
```