# ICQ

Ограничения: время – 250ms/500ms, память – 64MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод

>В школе №100 у каждого школьника есть свой личный номер ICQ. В школе распространено мнение, что чем меньше значение номера ICQ, тем более продвинутым является школьник. Известен список всех школьников с номерами ICQ. Требуется вывести список $K$ самых продвинутых школьников.
>
> В первой строке ввода содержится количество учеников в школе $N$ $(1 ≤ N ≤ 100)$ и число $K$ $(1 ≤ K ≤ N)$. Далее следует $N$ строк, в каждой строке содержится фамилия школьника (без пробелов, содержит не более 20 строчных латинских букв) и через пробел номер $ICQ$ $(1 ≤ ICQ ≤ 109)$. Номера ICQ и фамилии у школьников различны.
>
> Вывести фамилии $K$ самых продвинутых школьников в лексикографическом порядке (по алфавиту). Каждая фамилия выводится на отдельной строке.

**Пример ввода**
```
3 2
ivanov 170
semenova 320
antonov 201
```
**Пример вывода**
```
antonov
ivanov
```