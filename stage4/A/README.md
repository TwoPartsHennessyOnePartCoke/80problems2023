# Гистограмма

*Ограничения: время – 2s/4s, память – 64MiB Ввод: input.txt или стандартный ввод Вывод: output.txt или стандартный вывод*

> Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать, какие символы в секретных зашифрованных посланиях употребляются чаще других. Для удобства изучения Вовочка хочет получить графическое представление встречаемости символов. Поэтому он хочет построить гистограмму количества символов в сообщении. Гистограмма — это график, в котором каждому символу, встречающемуся в сообщении хотя бы один раз, соответствует столбик, высота которого пропорциональна количеству этих символов в сообщении.
>
> Ввод
>
> Входной файл содержит зашифрованный текст сообщения. Он содержит строчные и прописные латинские буквы, цифры, знаки препинания ("`.`", "`!`", "`?`", "`:`", "`-`", "`,`", "`;`", "`(`", "`)`"), пробелы и переводы строк. Размер входного файла не превышает $10^4$ байт. Текст содержит хотя бы один непробельный символ. Все строки входного файла не длиннее 200 символов.
>
> Вывод
>
> Для каждого символа $c$ кроме пробелов и переводов строк выведите столбик из символов `#`, количество которых должно быть равно количеству символов $c$ в данном тексте. Под каждым столбиком напишите символ, соответствующий ему. Отформатируйте гистограмму так, чтобы нижние концы столбиков были на одной строке, первая строка и первый столбец были непустыми. Не отделяйте столбики друг от друга. Отсортируйте столбики в порядке увеличения кодов символов.

**Пример ввода 1**

Hello, world!
**Пример вывода 1**
```
     #   
     ##  
#########
!,Hdelorw
```
**Пример ввода 2**
```
Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.
```
**Пример вывода 2**
```
         #              
         #              
         #              
         #              
         #              
         #         #    
         #  #      #    
      #  # ###  ####    
      ## ###### ####    
      ##############    
      ##############  ##
#  #  ############## ###
########################
,.;ADTabdeghilmnorstuvwy
```

*Источник: XII командный чемпионат школьников Санкт-Петербурга по программированию.*
