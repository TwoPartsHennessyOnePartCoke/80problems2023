# Доктор Дулитл

Ограничения: время – 1s/2s, память – 64MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод

> Доктор Дулитл ведет прием пациентов с восьми утра до пяти вечера, с перерывом на обед с полудня до часу дня. Пациенты заранее звонят доктору, указывают время, когда они смогут прийти, а доктор Дулитл назначает им время приема. На каждого пациента он тратит 10 минут, поэтому рабочее время он поделил на временные слоты по 10 минут и записывает пациентов на 8:00am, 8:10am, 8:20am, …, 11:50am, 1:00pm, 1:10pm, …, 4:40pm, 4:50pm. Доктору требуется программа, которая принимает звонки и сообщает время приема. Если есть несколько свободных слотов, начало которых попадает в указанный пациентом диапазон времени, то программа должна выбирать самый ранний из свободных.
>
> В первой строке ввода содержится одно целое число $N$ $(1≤N≤50)$ – количество звонков. В следующих N строках содержится диапазоны времени, указанные в звонках. Диапазоны перечисляются в порядке поступления звонков. Начальное время диапазона меньше конечного, начальное время может быть не ранее 8 утра, а конечное – не позднее 5 вечера. Время задается в формате `h:m am/pm`, где `h` принимает значения от 1 до 12, а `m` – от 00 до 59, до 12:00 указывается суффикс **am**, а начиная с 12:00 – суффикс **pm**.
>
> Вывести для каждого звонка назначенное время приема или сообщение `N/A`, если в заданный диапазон времени доктор будет занят.

*Пример ввода*
```
4
11:51am 1:00pm
12:35pm 1:05pm
1:00pm 2:00pm
8:00am 8:30am
```
**Вывод для примера**
```
1:00pm
N/A
1:10pm
8:00am
```