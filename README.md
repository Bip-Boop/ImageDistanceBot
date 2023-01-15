# ImageDistanceBot
@image_similarity_bot
класс ImageMath является фасадом (Facade) для взаимодействия с разными стратегиями (паттерн Strategy) векторизации VGGClassifier и InceptionClassifier, которые реализуют интерфейс ImageClassifier. Фасад ImageMath нужен для того, чтобы можно было подавать на вход сразу две картинки и получать результат подсчётов, он также позволяет загружать на машине только те стратегии, которые были выбраны. Взаимодействия с Telegram происходит (на уровне кода) по паттерну Command. В updater.dispatcher добавляются функции-команды (механизм делегирования рассматривает функции как инкапсулированные в объект), которые API вызывает после получения определённых сообщений от пользователя.

В ответ на две фотографии бот отвечает двумя значениями. Similarity (в процентах) - то, на сколько, собственно, похожи фотографии, если смотреть по полному результату работы моделей через пространство imagenet. Distance (в единицах) - более абстрактый показатель, т.к. используется предпоследний слой модели, он показывает более общую атмосферу, образ фотографии. Изучая эти два параметра, можно судить о схожести фотографий по мнению модели (в категориальном и абстрактном смысле). 
![Screenshot_20230115-192434__01](https://user-images.githubusercontent.com/62621659/212571427-01f32692-0bd4-4284-980f-221b57affaf1.jpg)
![Screenshot_20230115-192416__01](https://user-images.githubusercontent.com/62621659/212571434-09138ae6-7c69-4036-9c43-58f71775ebef.jpg)
