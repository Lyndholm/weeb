# 1. Цель проекта

Цель проекта — разработать социальный фотохостинг для фанатов японской мультипликации (далее — Система). Пользователи Системы смогут загружать изображения, делиться ими, просматривать чужие изображения, комментировать их, добавлять в избранное, а также создавать коллекции изображений. Помимо этого в Системе будет реализован публичный API для разработчиков, который облегчит взаимодействие сторонних приложений с Системой.

# 2. Описание системы

Система состоит из следующих основных функциональных блоков:

1. Регистрация, аутентификация и авторизация
2. Функционал для пользователей
	1. Загрузка изображений и последующие манипуляции с ними
	2. Создание коллекций изображений
	3. Добавление изображений в «Избранное» (а-ля "лайк" картинке)
	4. Комментирование изображений
3. Функционал главной страницы (ленты изображений)
4. Функционал тегов изображений
5. Функционал публичного API


## 2.1 Типы пользователей

Система в первой своей версии предусматривает 2 типа пользователей:
1. Рядовой пользователь
	1. Может загружать изображения, редактировать и удалять свои изображения, создавать коллекции, в которых могут быть изображения других пользователей, а также добавлять изображения в «Избранное».
2. Администратор
	1. Обладает правами рядового пользователя, а также он может удалять любые изображения в Системе и блокировать пользователю доступ к Системе.

В последующих версиях возможно добавление новых типов пользователей. Например, тип «Редактор». Редактор сможет изменять изображения всех пользователей системы (менять название, описание, теги) для корректности данных.

Изменение типов пользователя должно быть доступно ограниченному кругу лиц.


## 2.2 Регистрация 

Для регистрации и аутентификации пользователей можно использовать стандартный функционал Django, который включает в себя возможность регистрации через email или социальные сети (OAuth).

Процесс регистрации пользователей должен быть реализован в интерфейсах Системы. При регистрации пользователя должны быть запрошены следующие поля:

* email — обязательное поле
* никнейм — обязательное поле
* отображаемое имя — опциональое поле
* пароль — опциональное поле

После отправки формы регистрации, пользователю на email приходит
письмо с ссылкой для подтверждения создания аккаунта.

Аутентификация в первой версии Системы будет происходить по паролю. В последующих версиях возможно повышение безопасности аутентификации в аутентификации по разовым кодам, приходящим на email.

Ещё один метод аутентификации — аутентификация через OAuth. Для этого пользователю необходимо будет связать аккаунт Системы с аккаунтом соответствующего провайдера OAuth.

Возможные платформы для привязки аккаунта:
* Google
* Discord
* VK

В первой версии Системы интеграция с провайдерами OAuth не планируется.


## 2.3 Профили пользователей

Каждый пользователь Системы имеет профиль, на котором отображается информация о нём. Профиль пользователя доступен для просмотра всем пользователям Системы.

В профиле пользователя должна быть доступна следующая информация:
- отображаемое имя
- аватар
- количество загруженных изображений
- количество созданных коллекций

На странице профиля также должны быть доступны изображения, загруженные пользователем, и его коллекции.

В настройках профиля пользователь может редактировать информацию о себе — email, никнейм, отображаемое имя, аватар, привязанные платформы.

Должна быть возможность изменения пароля с, возможно, подтверждением действия по email.


## 2.4 Изображения и манипуляции с ними

Пользователи Системы должны иметь возможность загружать изображения на сервер. Для загрузки изображений используется интерфейс Системы.

При загрузке изображения пользователь должен иметь возможность добавить к изображению название, описание и теги.

Система должна поддерживать наиболее распространенные форматы изображений: JPEG/JPG, PNG, TIFF, BMP, GIF. Система должна проверять формат и размер загружаемых изображений, и в случае неподходящих параметров должна выводить соответствующие сообщения об ошибке.

При загрузке изображения пользователь может указать ссылку на источник изображения в соответствующем поле. Источник может быть использован для отображения информации о правах на изображение или для ссылки на оригинальный источник изображения. Данное поле может быть опциональным, если пользователь не желает указывать источник.

После загрузки изображения, пользователь может производить следующие манипуляции с ним:
- редактирование — пользователь может изменять название, описание изображения и его теги
- удаление — пользователь может удалять свои изображения

Изображения должны храниться на S3 подобном хранилище и иметь уникальное имя, которое будет генерироваться при загрузке.

Для обеспечения быстрой загрузки изображений и уменьшения нагрузки на сервер и сеть, можно "сжимать" оригинальное изображение. Иначе говоря, возможно хранение нескольких экземпляров изображения. Например, на превью в ленте отображается уменьшенная копия изображения, а на странице самого изображения оно отображается в исходном размере.  

Пользователи Системы должны иметь возможность просматривать изображения других пользователей, но манипулировать разрешено только своими собственными.

При открытии персональной страницы конкретного изображения в интерфейсе должны отображаться: само изображение, название, описание, теги, автор, количество просмотров и "лайков", а внизу страницы комментарии.


## 2.5 Коллекции изображений

Коллекции изображений — это наборы изображений, созданные пользователями Системы. Пользователи могут создавать свои коллекции и добавлять в них изображения из общей базы изображений. Коллекции могут быть открытыми (доступны для всех пользователей) или закрытыми (доступны только автору).

Каждая коллекция имеет следующие поля:
* название — обязательное поле
* описание — опциональное поле
* обложка-превью — опциональное поле

Для создания коллекции пользователь должен выбрать в меню пункт «Создать коллекцию», после чего он будет перенаправлен на страницу создания коллекции. Здесь пользователь может ввести название и описание коллекции, а также выбрать обложку, которая будет отображаться на странице коллекции.

После создания коллекции пользователь может добавлять в неё изображения. Для этого пользователь должен перейти на страницу изображения и выбрать пункт «Добавить в коллекцию». После этого пользователю будет предложено выбрать из списка свои коллекции, в которые он хочет добавить изображение.

Также пользователь может просмотреть список изображений, добавленных в его коллекции, а также редактировать и удалять коллекции и изображения в них.


## 2.6 «Избранное»

Пользователи могут добавлять изображения в свой список «Избранное», что позволяет им быстро находить их в будущем. Пользователи могут просматривать свой список «Избранное», удалять изображения из списка.

Пользователи Системы могут добавлять изображения в список «Избранное», что позволит им легко находить интересные изображения позже.

Для добавления изображения в «Избранное» пользователь должен нажать на соответствующую кнопку рядом с изображением. Если пользователь уже добавил изображение в список «Избранное», кнопка будет отображаться в активном состоянии. Если нажать на кнопку, находящуюся в активном состоянии, изображение будет удалено из «Избранного».

Пользователи могут просматривать свой список «Избранное» на своей странице профиля. В этом списке пользователи могут удалить изображения из «Избранного».

Возможно, пользователи должны иметь возможность получать уведомления, когда кто-то добавляет их изображения в «Избранное».

Кроме того, на главной странице Системы, вомзожно, стоит сделать раздел «Популярное», в котором будут отображаться изображения, наиболее часто добавляемые в «Избранное».


## 2.7 Лента изображений

На главной странице Системы отображается лента изображений, которая позволяет пользователям просматривать (по умолчанию) последние добавленные изображения.

Изображения в ленте могут быть отсортированы по различным критериям (по дате загрузки, количеству лайков, по количеству просмоторов). В интерфейсе также должен быть поиск по тегам, названию и описанию изображений, авторам.

На главной странице должен быть реализован функционал пагинации, который позволит загружать изображения порциями, а не все сразу.

Кроме того, для обеспечения лучшей производительности, следует использовать кэширование ленты изображений.

Для обеспечения безопасности и контроля за содержимым, а также борьбы со спамом, следует реализовать функционал модерации ленты изображений. Модерация в первой версии системы будет ручной, в будщем стоит реализовать автоматическую модерацию.


## 2.8 Теги изображений

Теги в Системе будет использоваться для удобства поиска изображений. Пользователи могут добавлять теги к своим изображениям, чтобы описать их содержание, а другие пользователи могут использовать эти теги для поиска подходящих изображений.

Теги будут общие для всех пользователей Системы и не будут разделяться на категории. Пользователи могут добавлять один или несколько тегов к каждому изображению, а также редактировать или удалять их.

При добавлении тегов пользователи смогут выбирать уже существующие теги из списка, а также создавать новые теги. Для удобства поиска, при создании нового тега, Система будет проверять наличие схожих тегов и предлагать пользователю использовать уже существующие теги.

На странице поиска изображений, пользователи смогут вводить тег для поиска, и Система будет отображать все подходящие изображения. Пользователи смогут также использовать несколько тегов для более точного поиска изображений.

Возможно, теги также будут использоваться для отображения связанных изображений в карточках изображений и при поиске похожих изображений. Например, если изображение содержит тег "maid", то Система может предложить пользователю посмотреть другие изображения с тегом "maid".

## 2.9 Публичный API

Для взаимодействия сторонних приложений с Системой необходимо реализовать публичный API. API должно предоставлять возможность взаимодействия со всеми сущностями Системы. 

Все запросы к API должны содержать токен аутентификации, который будет выдаваться пользователям при авторизации в Системе.

## 2.10 Комментирование

В первой версии Системы комментариев не будет. На момент написания документа идеи по комментариям таковы:
* Пользователи могут комментировать изображения и коллекции.
* Пользователи могут отвечать на комментарии друг друга.
* Древовидное отображение комментариев.
* У каждого комментария должен быть рейтинг, который можно либо увеличить, либо уменьшить по нажатию на соответствующие кнопки.
* Комментарии могут быть отсортированы по дате написания или по рейтингу.

# 3. Предлагаемый стек технологий

Для реализации системы предлагается следующий стек технологий:

- В качестве основного языка программирования используется Python.
- Для веб-приложения используется фреймворк Django и Django REST Framework для создания API.
- Для хранения данных используется база данных PostgreSQL.
- Redis для кэширования.
- Docker контейниризации приложения.
- Kubernetes для оркестрации контейнерами и лёгкого мастштабированием.
- NGINX в качестве веб-сервера.

Хранение файлов и изображений, загружаемых пользователями, должно осуществляться
в S3-совместимом хранилище.

Стоит использовать CDN для хранения и распределения статических файлов, включая изображения.

## 3.1 Нефункциональные требования

- Масштабируемость: Система должна быть масштабируемой, чтобы обеспечить работу с большим количеством пользователей и изображений.
- Производительность: Система должна быть быстрой и отзывчивой, чтобы обеспечивать хороший пользовательский опыт.
- Надежность: Система должна быть надежной и отказоустойчивой, стремление к максимально возможному uptime.

# 4. Требования к дизайну

Минимализм, лаконичность, акцент на контент. Тёмные расслабляющие цвета. На странице, скорее всего в шапке, должен присутствовать логотип Системы. Логотип надо разработать в рамках работы над проектом.
