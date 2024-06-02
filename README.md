# Проект по анализу данных 2024

**Выполнили: Ловягин Егор, Мадиван Тунва, Овчинникова Мария**

**План**
- [Шаг 1. Выбор темы и парсинг](https://github.com/marusyaOV/andan-project24/tree/main#шаг-1-выбор-темы-и-многострадальный-парсинг-данных)
- [Шаг 2. Составление гипотез](https://github.com/marusyaOV/andan-project24/tree/main?tab=readme-ov-file#шаг-2-составление-гипотез)
- [Шаг 3. Анализ данных и визуализация](https://github.com/marusyaOV/andan-project24/tree/main#шаг-3-анализ-данных-и-визуализация)
- [Шаг 4. Машинное обучение](https://github.com/marusyaOV/andan-project24/tree/main#шаг-4-машинное-обучение-идея)
- [Шаг 5. Выводы](https://github.com/marusyaOV/andan-project24/tree/main#шаг-5-выводы)

## Шаг 1: Выбор темы и многострадальный парсинг данных

Предметом анализа нашего проекта стала музыка. Нам всегда было интересно почему в жарких странах люди слушают одну музыку, а в более северных - на первый взгляд, другую. Одним из главных вопросов, который впоследствие мы сформулировали в нескольких наших гипотезах, заключался в том, действительно ли в жарких странах люди слушают более энергичную, веселую музыку, а в странах с суровым холодным климатом - спокойную, медленную, “душевную”?

Для ответа на все вопросы нами было решено найти данные о том, какие песни слушают в разных странах мира, каким-то образом сформулировать их количественные характеристики. 
Пойдя дальше, мы решили придумать, с помощью каких объективных числовых признаков можно было бы широкими мазками описать любую страну. Поскольку, как мы считаем, во многом, культурные особенности влияют на музыкальные предпочтения, то было бы здорово придумать такие факторы, которые влияют на эти культурные особенности. Это особенно важно и нужно, т.к. нет ни одного числового признака, с помощью которого можно было бы описать разные страны мира, и таким образом их отождествить.
Именно поэтому выбор пал на географические, климатические, демографические и социальные признаки: плотность населения; среднегодовое число осадков; среднегодовая температура; а также индекс человеческого капитала (как универсальной метрики для оценки знаний и навыков населения).

## Сбор данных 

В качестве основного источника данных о музыке был выбран Spotify API, поскольку Spotify - стриминговый сервис, занимающих более половины рынка в мире, а значит, так или иначе, практически во всех странах слушают музыку в Spotify. Источника, для того чтобы собрать агрегированные данные, лучше и быть не может. Немного покопавшись в документации и изрядно намучившись с токенами доступа, нам удалось: имея список из стран(для которых редакция Spotify представляла чарт “Top 50 - {Название страны}”, содержащий в себе самые популярные треки среди слушателей страны), мы нашли для каждой из них такой плейлист, после чего достали из каждого из плейлистов все 50 содержащихся в нем песен (трек, ID трека). Затем, используя ID трека мы нашли всю необходимую информацию о каждой конкретной песни, и составили на основе всего полученного датафрейм. Покопавшись в документации Spotify API, мы нашли все основные метрики: 
1) **Акустичность (Acousticness)**: Показывает вероятность того, что трек является акустическим. Числовое значение от 0.0 до 1.0, где 1.0 означает высокую вероятность акустического звучания.
2) **Танцевальность (Danceability)**: Оценивает, насколько трек подходит для танцев на основе комбинации музыкальных элементов, включая темп, стабильность ритма, силу ударов и общую регулярность. 
Числовое значение от 0.0 до 1.0.
3) **Энергичность (Energy)**: Мера от 0.0 до 1.0, отражающая интенсивность и активность трека. Высокие значения означают более энергичный трек.
4) **Громкость (Loudness)**: Средняя громкость трека в децибелах (dB). Чем выше значение, тем громче трек.
5) **Речевой контент (Speechiness)**: Определяет, содержит ли трек много разговорного текста. Значения выше 0.66 обычно указывают на треки, состоящие в основном из произнесённых слов.
6) **Инструментальность (Instrumentalness)**: Предсказывает, содержит ли трек вокальные партии. Значения ближе к 1.0 означают большую вероятность того, что трек не содержит вокала.
7) **Живость (Liveness)**: Определяет, был ли трек записан в живой обстановке. Высокие значения (ближе к 1.0) указывают на то, что трек, вероятно, был записан в живую.
8) **Валентность (Valence)**: Мера от 0.0 до 1.0, описывающая музыкальную позитивность, передаваемую треком. Высокие значения означают более позитивное и веселое звучание.
9) **Темп (Tempo)**: Темп трека в ударах в минуту (BPM). Описывает скорость трека.
10) **Тональность (Key)**: Основная тональность трека, представлена в виде числового значения, где каждое число соответствует определённой ноте.
11) **Мажорность/минорность** (Mode): Индикатор мажорности или минорности трека, где 1 означает мажор, а 0 — минор.
12) **Длительность** (в ms).


Затем мы приступили к сбору страновых характеристик. Это заняло гораздо меньше времени, чем работа с Spotify API. Здесь мы просто нашли и спарсили готовые таблицы из открытых источников. На данном этапе мы не объединили эти признаки в один, причисляя каждому весовые коэффициенты, поскольку данный признак потребуется лишь на финальной стадии проекта, при машинном обучении. Модель должна будет ответить на вопрос, имея какую-либо страну, а также имея вышеперечисленные страновые признаки: какую музыку слушают жители этой страны?

**Практическое применение**
Полученное (модель, берущая на вход страновые характеристики и выдающая на выходе конкретный набор из музыкальных характеристик/рекомендаций) является очень сильным результатом не только для учебного проекта, но и для бизнеса. 
Несложно представить ситуацию, когда какой-либо стриминговый сервис выходит в новую страну со своим продуктом и хочет сразу выдавать определенные рекомендации своим слушателям, еще до того момента как рекомендательные алгоритмы подстроятся под личные вкусы каждого слушателя. Таким образом, имея в распоряжении значительное количество данных и сумев точно описать страну с помощью объективных числовых признаков, можно приблизиться к решению вышеописанной проблемы. 

## Шаг 2: Составление гипотез

В ходе нашей работы мы составили несколько гипотез 0_0

- 1)Чем ближе страна находится к экваториальному тропическому поясу, тем песня более веселая и энергичная(мы взяли для анализа к-т оптимизма, он будет описан более подробно в
  более подробно в самом файле с анализом)

- 2)Чем ниже в стране температура, тем более спокойную (тихую) музыку люди предпочитают слушать (параметр громкость, живость и длительность)

- 3)В топ-5 плейлиста каждой страны в среднем в песнях больше слов и лирики( к примеру речевой контент + инструментальность

- 4)Чем больше в стране плотность населения, тем выше в ней все параметры для песен кроме длительности

- 5)Чем в стране больше дождей (кол-во осадков), тем больше минорных треков в топ-50 плейлисте.

- 6)Чем ниже ср.температура в стране тем меньше в песнях слов (речевого контента)


## Шаг 3: Анализ данных и визуализация
Так как файл, который спарсили практически не требовал корректировок, нами было принято решение отдельно рассмотреть
общий файл, а потом подробно проанализировать каждую из предложенных нами гипотез.

Все гипотезы были рассмотрены(или там сейчас раскидан примерный план) и проверены (загружены в файл [Visualization_and_analysis.ipynb)](Visualization_and_analysis.ipynb )

## Шаг 4: Машинное обучение (идея)

Мы можем внедрить в работу ML. Модель должна предсказывать какое-либо измерение настроения (например, позитивное/негативное) или предпочтительный жанр музыки на основе погодных данных.
Для нашего проекта могут подойти: линейная регрессия,  lasso-регрессия, решающее дерево + выбрать регрессор.

Для этого необходимо:
1) Разделить данные на обучающий и тестовый наборы.
2) Масштабировать признаки через библиотеку scikit-learn:

- Стандартизация (Z-масштабирование):

Этот метод центрирует данные путем вычитания среднего значения из каждого признака, а затем делит на стандартное отклонение.
Это гарантирует, что каждый признак имеет среднее значение 0 и стандартное отклонение 1.
Стандартизация особенно полезна, когда распределение признаков неизвестно или может меняться между различными странами.

- Нормализация:

Этот метод масштабирует каждый признак так, чтобы значения находились в диапазоне от 0 до 1.
Это особенно полезно, когда данные имеют разные шкалы или разные единицы измерения, а нужно, чтобы все признаки были на одной шкале.

3) Выбрать целевую переменную, например настроение музыки в странах
4) После обучения оценить производительность на тестовом наборе данных: для регрессии это может быть коэффициент детерминации (R^2), средняя квадратическая ошибка (MSE)

## Шаг 5. Выводы:
В результате нашего анализа, проведенного на основе датасета, связанного с музыкальными предпочтениями, мы пришли к следующим выводам. Проведенная работа позволила тщательно проверить наши гипотезы, касающиеся различных аспектов популярности музыкальных композиций. Однако, несмотря на глубокий анализ и тщательное исследование, большинство из выдвинутых гипотез не нашли своего подтверждения. Это свидетельствует о сложной и многогранной природе факторов, влияющих на популярность музыки.

Тем не менее, нам удалось подтвердить одну из наших гипотез, которая оказалась весьма значимой. Эта гипотеза касалась содержания речевого контента и лирики в самых популярных песнях в различных музыкальных чартах. Наше исследование показало, что именно этот аспект играет существенную роль в определении популярности музыкальных композиций. Такие результаты подчеркивают важность текстового содержания песен и его влияние на восприятие слушателей. Таким образом, наше исследование внесло ценный вклад в понимание факторов, определяющих популярность музыки.

На основании проведенного анализа и построенных линейных моделей для различных характеристик музыкальных треков, мы выявили влияние ряда факторов (среднегодовая температура, годовые осадки, плотность населения и индекс человеческого капитала) на эти характеристики:

Длительность треков: Сильно зависит от температуры и плотности населения, увеличиваясь с их ростом.

Громкость: Осадки и индекс человеческого капитала положительно влияют на громкость, тогда как плотность населения – отрицательно.

Энергичность: Отрицательно коррелирует с температурой и плотностью населения, что указывает на менее энергичные треки в таких условиях.

Танцевальность: Слабо зависит от факторов, с отрицательной корреляцией с температурой и индексом человеческого капитала.

Акустичность: Положительно зависит от температуры, популяризуя акустические треки в теплых регионах.

Инструментальность: Слабо зависит от всех факторов.

Живость: Положительно коррелирует с температурой, но отрицательно – с осадками и плотностью населения.

Валентность: Положительно зависит от осадков, но отрицательно – от плотности населения и индекса человеческого капитала.

Речевой контент: Слабо зависит от всех факторов.

Темп: Значимо зависит от индекса человеческого капитала, указывая на более быстрый темп в развитых регионах.

Эти выводы дали нам понимание того, как различные экологические и социальные факторы могут влиять на музыкальные предпочтения и характеристики треков, что может быть полезным для дальнейших исследований в области музыкальной индустрии и маркетинга.



