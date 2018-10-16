Международный классификатор болезней МКБ10 и МКБ-О
==================================================

Установка
---------

..  code:: shell

  git clone git@github.com:ak04nv/mkb10.git
  cd mkb10
  ./init_db.sh
  virtualenv -p python3 --prompt="(mkb10) " .env
  . .env/bin/activate
  pip install -r requirements.txt
  export FLASK_ENV=development
  flask run

Приложение будет доступно по адресу http://localhost:5000

API для построения дерева
-------------------------

URL
  /api
Response
  ..  code:: javascript

    // Список классов
    [
      {
        "id": 1,
        "name": "НЕКОТОРЫЕ ИНФЕКЦИОННЫЕ И ПАРАЗИТАРНЫЕ БОЛЕЗНИ (A00-B99)"
      },
      // ...
    ]

URL
  /api/:id
Args
  :id: Идентификатор класса
Response
  ..  code:: javascript

    // Список блоков класса
    [
      {
        "id": 2,
        "name": "КИШЕЧНЫЕ ИНФЕКЦИИ (A00-A09)"
      },
      // ...
    ]

URL
  /api/:id/group
Args
  :id: Идентификатор блока
  :all: Вывести все коды (включая неактуальные). Аргумент необязательный.
Response
  ..  code:: javascript

    // Список групп блока
    [
      {
        "actual": true, // Параметр доступен только при указании аргумента 'all'
        "code": "A00",
        "id": "3",
        "has_subgroup": true, // есть ли у группы подргуппа
        "name": "Холера"
      },
      // ...
    ]

URL
  /api/:code/subgroup
Args
  :code: Код группы
  :all: Вывести все коды (включая неактуальные). Аргумент необязательный.
Response
  ..  code:: javascript

    // Список подргуппы заданной группы
    [
      {
        "actual": true, // Параметр доступен только при указании аргумента 'all'
        "code": "A00.0",
        "id": "4",
        "name": "Холера, вызванная холерным вибрионом 01, биовар cholerae"
      },
      {
        "actual": true, // Параметр доступен только при указании аргумента 'all'
        "code": "A00.1",
        "id": "5",
        "name": "Холера, вызванная холерным вибрионом 01, биовар eltor"
      },
      {
        "actual": true, // Параметр доступен только при указании аргумента 'all'
        "code": "A00.9",
        "id": "6",
        "name": "Холера неуточненная"
      }
    ]

URL
  /api/icdo/block
Response
  ..  code:: javascript

    // Список блоков справочника МКБ-О
    [
      {
        "id": 1,
        "name": "800 Новообразования, БДУ"
      },
      {
        "id": 15,
        "name": "801—804 Эпителиальные  новообразования, БДУ"
      },
      // ...
    ]

URL
  /api/icdo/block/:id
Args
  :id: Идентификатор блока
Response
  ..  code:: javascript

    // Список болезней блока
    [
      {
        "code": "8140/0",
        "id": "107",
        "name": "Аденома БДУ"
      },
      {
        "code": "8140/1",
        "id": "108",
        "name": "Аденома бронхиальных желез БДУ (D38.1)"
      },
      // ...
    ]


Примеры
  |  http://localhost:5000/api
  |  http://localhost:5000/api/3773
  |  http://localhost:5000/api/4161/group?all
  |  http://localhost:5000/api/I84/subgroup?all
  |  http://localhost:5000/api/icdo/block
  |  http://localhost:5000/api/icdo/block/106

API для поиска и разрешения имён
--------------------------------

URL
  /api/lookup
  /api/icdo/lookup
Args
  :q: Строка поиска (обязательный аргумент). Если аргумент начинается на [a-z], то поиск осуществляется по кодам, иначе по названию
  :limit: Ограничение на количество выдаваемых кодов. Значение по-умолчанию: 50
Response
  ..  code:: javascript

    // http://localhost:5000/api/lookup?q=i&limit=1
    [
        {
          "code": "I00",
          "name": "Ревматическая лихорадка без упоминания о вовлечении сердца"
        }
    ]

URL
  /api/fetch
  /api/icdo/fetch
GET
  :codes: Список кодов через запятую
POST
  :[]: JSON-список кодов (пример ниже)
Response
  .. code:: javascript

    // Оба запроса вернут одинаковый ответ
    // curl http://localhost:5000/api/fetch?codes=A00,A01
    // curl -H "Content-Type: application/javascript;X-Requested-With: XMLHttpResponse" -X POST -d '["A00","A01"]' http://localhost:5000/api/fetch

    [
      {
        "code": "A00",
        "name": "Холера"
      },
      {
        "code": "A01",
        "name": "Тиф и паратиф"
      }
    ]

Дополнительно
-------------

- ``mkb10.csv`` Файл кодов МКБ10
- ``mkbo.csv`` Файл кодов МКБ-O
- ``init_db.sh`` Скрипт для создания базы данных
