# Форматирование таблиц

*Ограничения: время – 1s/2s, память – 32MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод*

> Некоторую информацию требуется представить в виде таблицы, при этом информация в колонках таблицы может быть выровнена влево, вправо или по центру. Ширина каждой колонки определяется ее содержимым.
>
> Входной файл содержит описание одной таблицы. Описание начинается со строки, описывающей выравнивание колонок в таблице. Количество символов в строке равно числу колонок в таблице. Символ '`<`' означает выравнивание информации в колонке влево, символ '`>`' – вправо, а символ '`=`' – по центру. Других символов в этой строке не может быть. Следующая строка содержит непустые заголовки колонок, разделенные символом '`&`'. Количество заголовков также соответствует числу колонок. Далее идет от 1 до 20 строк, содержащих данные для таблицы. Каждая строка соответствует одной строке таблицы, данные разделены символом '`&`' и их количество соответствует числу колонок таблицы. Пробелы могут появляться внутри элемента данных (заголовка), но никогда перед или после элемента (заголовка). Тексты заголовков и данные не содержат символов '`&`', '`<`', '`>`', '`=`' и '`*`'. Строка с символом '`*`' завершает описание таблицы.
>
> В выходной файл вывести таблицу по ее описанию, как показано в примере. При этом:
> - Общая ширина готовой таблицы не превысит 79 символов.
> - Для изображения горизонтальных линий нужно использовать символ '-' (минус). Символ '@' должен стоять во всех четырех внешних углах таблицы. Символ '+' (плюс) появляется только на пересечении линий только в строке, отделяющей заголовок от тела таблицы. Для изображения границ колонок нужно использовать символ '|' (вертикальная черта, на клавиатуре иногда изображается с разрывом).
> - Самый длинный элемент данных (заголовок) в колонке таблицы должен быть отделен от обеих границ колонки точно одним пробелом.
> - Если центрируемый элемент данных (заголовок) не может быть точно центрирован, дополнительный пробел добавляется справа от элемента данных (заголовка).
> - Не должно быть пробелов в начале или в конце строки. Символы табуляции нельзя использовать.

**Пример ввода**
```
<>=>
TITLE&VERSION&OPERATING SYSTEM&PRICE
Slug Farm&2.0&FreeBSD&49.99
Figs of Doom&1.7&Linux&9.98
Smiley Goes to Happy Town&11.0&Windows&129.25
Wheelbarrow Motocross&1.0&BeOS&34.97
*
```
**Пример вывода**
```
@-----------------------------------------------------------------@
| TITLE                     | VERSION | OPERATING SYSTEM |  PRICE |
|---------------------------+---------+------------------+--------|
| Slug Farm                 |     2.0 |     FreeBSD      |  49.99 |
| Figs of Doom              |     1.7 |      Linux       |   9.98 |
| Smiley Goes to Happy Town |    11.0 |     Windows      | 129.25 |
| Wheelbarrow Motocross     |     1.0 |       BeOS       |  34.97 |
@-----------------------------------------------------------------@
```

*Источник: ACM ICPC MCRC, 2002*
