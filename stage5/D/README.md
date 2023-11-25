# Желуди

Ограничения: время – 2s/4s, память – 2MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод

> На плоскости расположены $m$ свиней и $n$ желудей. Каждая из свиней хочет съесть как можно больше желудей. Для этого они пользуются таким алгоритмом:
> - Изначально каждая свинья устремляется по прямой к ближайшему желудю. Если таких желудей несколько, то она выбирает желудь с наименьшим номером.
> - Как только какая-то свинья съедает выбранный желудь (т.е. оказывается в точке с координатами, равными координатам желудя), так сразу она снова выбирает ближайший желудь, и так далее, пока все желуди не будут съедены.
> - Если в какой-то момент оказалось, что желудь, к которому шла какая-то свинья, съеден, то эта свинья сразу же выбирает ближайший из оставшихся желудей, исходя из ее нынешнего положения.
> - Когда сразу несколько свиней одновременно приходят к одному и тому же желудю, то желудь достается свинье, у которой номер больше, чем у остальных. После этого все свиньи опять выбирают ближайшие желуди и идут их есть.
> - Если свинья в момент выбора ближайшего желудя уже находится в точке, в которой есть один или несколько желудей, то она их съедает. Если в этой точке несколько свиней, то все эти желуди съедает свинья с наибольшим номером.
>
> Вам необходимо сосчитать, сколько желудей съест в конце концов каждая свинья. Все свиньи двигаются с одинаковой скоростью и строго прямолинейно.
>
> В первой строке ввода записаны числа $m$ и $n$ $(1 ≤ m ≤ 300, 1 ≤ n ≤ 300)$. В последующих $m$ строках записаны начальные положения каждой из свиней $xp_i$ и $yp_i$. Далее следуют $n$ строк с координатами желудей $xa_i$ и $ya_i$. Все координаты – целые числа в пределах от –10000 до 10000.
>
> Вывести $m$ чисел – количество желудей, съеденых каждой свиньей. Каждое число выводится на отдельной строке.

**Пример ввода**
```
2 3 
0 0 
100 100 
0 0 
-1 -1 
50 50
```
**Пример вывода**
```
2 
1 
```

*Источник: http://neerc.ifmo.ru/school/archive/*