Первая лабораторная посвящена предобработке текста (мы коротко говорили об этом на лекции).
Подробнее об этом можно почитать здесь:
https://github.com/mannefedov/compling_nlp_hse_course/blob/master/notebooks/preprocessing/Text_preprocessing.ipynb
Здесь есть описания всех библиотек, примеры и прочие полезные для выполнения лабы вещи.

В самой лабораторной три вопроса:

**1. Ошибки токенизации <br>**
Найдите 1 любой способ сломать токенизацию на предложения функцией sentenize из библиотеки razdel.
Придумайте (или найдите на каком-то корпусе) такое предложение (или несколько предложений), которое будет некорректно
разобрано
sentenize, но при этом будет грамматически верным.

**2. Токенизация Mystem vs razdel.tokenize<br>**
Токенизируйте текст (не менее 10 предложений, можно взять любую статью Вики) с помощью razdel и с помощью Mystem.
Найдите различия в токенизациях. Что, по вашему мнению, работает лучше на этом тексте?

**3. Лемматизация Mystem vs Pymorphy<br>**
Лемматизируйте текст с помощью mystem и pymorphy. Найдите различия в лемматизации. Что, по вашему мнению, работает
лучше на этом тексте?

**_Важно:_** для пайморфи используйте токенизацию из mystem, чтобы исключить влияние токенизации на результат.
Анализируйте
только значимые различия, а не технические особенности (не сравнивайте скорость работы и удобность интерфейса).

### Выполнение

1. sentinize сломался
   на [статье про БАК](https://ru.wikipedia.org/wiki/%D0%91%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9_%D0%B0%D0%B4%D1%80%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D0%BB%D0%BB%D0%B0%D0%B9%D0%B4%D0%B5%D1%80)
2. Mystem ошибается при лемматизации, например, `0,0001 сек` понял как глагол и выдал `сечь`. Также, к нему требуется
   постобработка как минимум от пробелов, т.к. считает их токенами. Часто ошибается в разделение на токены комбинации
   скобок. <br>
   _Я бы разделял на токены при помощи `razdel`, а потом бы приводил к леммам средствами `mystem`_
3. 