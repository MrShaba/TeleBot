
# # # #DATA TYPES - TIPU DANNIH
# # # int    #celie chisla
# # # float  #desyatichnie chisla
# # # str    #stroki                      
# # # bool   #logicheskiy tip dannih (True/False)
# # # list   #spisok
# # # tuple  #kortej
# # # set    #mnozhestvo
# # # dict   #slovar


# # # #STRING METHODS - METODI STROK
# # # # .upper()   #vse bukvi bolshie
# # # # .lower()   #vse bukvi malenkie
# # # # .strip()   #ubiraet probeli s nachala i konca
# # # # .replace() #menyaet odnu bukvu ili slovo na drugoe
# # # # .split()   #preobrazuet stroku v spisok
# # # # .join()    #preobrazuet spisok v stroku
# # # # .find()    #naxodit poziciu podstroki v stroke
# # # # .index()   #naxodit poziciu podstroki v stroke (vozvrashaet oshibku esli ne naideno)
# # # # .count()   #schitaet kol-vo vhozhdenii podstroki v stroke
# # # # .startswith() #proveryaet nachinaetsya li stroka s ukazannoi podstroki
# # # # .endswith()   #proveryaet zakanchivaetsya li stroka s ukazannoi podstroki

# # # #1. Num = 5: Задаем число, для которого строится таблица
# # # #2. multiplier = 1: Начинаем с множителя 1.
# # # #3. while True:: Бесконечный цикл.
# # # #4. result = multiplier * Num: Вычисляем произведение.
# # # #5. print(f"{multiplier}*{Num}={result}"): Печатаем строку в нужном формате.
# # # #6. multiplier += 1: Увеличиваем множитель на 1 для следующего шага.
# # # #7. if multiplier > 10: break: Условие выхода из цикла — когда множитель становится больше 10.



# # # # #LIST METHODS - METODI SPISKOV
# # # # .append()   #dobavlyaet element v konets spiska
# # # # .extend()   #dobavlyaet elementi iz drugogo spiska v konets spiska
# # # # .insert()   #dobavlyaet element v ukazannuyu poziciu
# # # # .remove()   #udalyaet pervoe vhozhdenie ukazannogo elementa
# # # # .pop()      #udalyaet element po ukazannomu indeksoi
# # # # .clear()    #ochishchaet spisok
# # # # .index()    #vozvrashaet indeks pervogo vhozhdeniya ukazannogo elementa
# # # # .count()    #schitaet kol-vo vhozhdenii ukazannogo elementa
# # # # .sort()     #sortiruet spisok na meste
# # # # .reverse()  #reversit poryadok elementov v spiske
# # # # .copy()     #sozdaet poverhnostnuyu kopiyu spiska
# # # # .self()     #sslka na konkretnui obuekt vnutri metodov
# # # # .


# # #  #args  #karej(1,2,3) #dopolnitelnie pozizionnue argumenti

# # # #kwargs #slovar(name="ivan",age=20) #dopolnitelnie imenovannue argumenti

# # # #return x vozvrashaet znachenie x

# # # #f(seg),g(**dict) #unpacking raspakovka spiska i slovara


# # #         # CTRL+N = NOVUI FAIL
# # #         # CTRL+O = OTKURUT FAIL
# # #         # CTRL+S = SOXRANIT
# # #         # CTRL+T = POKAZAT VSE SIMBOLU 
# # #         # CTRL+G = PREITI K STROKE
# # #         # CTRL+P = PREITI K FAILY
# # #         # CTRL+F = NAXODIT 
# # #         # CTRL+H = ZAMENIT
# # #         # CTRL+I = VUBRAIT TEKUSHUYU STROKU
# # #         # CTRL+W = ZAKRUT FAIL
# # #         # CTRL+D = VUBRAT SLOVO
# # #         # CTRL+X = VUREZAT VUDELENIE    
# # #         # 
# # #         # obstraksuy = obiekt delaet metod skrutno   


# # # #В программировании ООП (объектно-ориентированное программирование)
# # # #  — это стиль написания кода, где данные и функции объединяются в объекты.

# # # #Основные принципы ООП:
# # # #- Абстракция — выделение общего интерфейса.
# # # #- Инкапсуляция — скрытие деталей реализации.
# # # #- Наследование — создание новых классов на основе существующих.
# # # #- Полиморфизм — единый интерфейс для разных реализаций.

# # # #В Python ООП реализуется через классы и объекты.  
# # # #Пример:
# # # #class Animal:
# # # #    def make_sound(self):
# # # #        print("Животное издает звук")

# # # #a = Animal()
# # # #a.make_sound()





# # # #                                            ABSTRAKSIYA

# # # #  Абстракция в IT — это игнорирование ненужных деталей.
# # # #  Это принцип, при котором вы сосредотачиваетесь только на том,
# # # #  что делает объект, а не на том, как он это делает.


# # # #Простая аналогия:

# # # #Вы пользуетесь автомобилем. Вам не нужно знать, как работает двигатель, 
# # # # чтобы нажать на педаль газа и поехать.
# # # #  Педаль газа — это и есть абстракция, которая скрывает всю сложность под капотом.


# # # #Примеры в IT:

# # # #1. Кнопка на сайте. Вы нажимаете на нее, чтобы купить товар. 
# # # # Вам не нужно знать, какой код выполняется на сервере,
# # # #  чтобы произошла покупка.
# # # #2. Функция в коде. Вы вызываете функцию sortList(), 
# # # # чтобы отсортировать список. Вам не важно, какой алгоритм сортировки (быстрая,
# # # #  пузырьковая) используется внутри.

# # # #Главная цель абстракции — спрятать сложность,
# # # #  чтобы программист мог решать большие задачи, 
# # # # оперируя простыми понятиями.


# # #                                    #INKAPSULATSIYA

# # # #Инкапсуляция в IT — это объединение данных и методов в одной "капсуле" 
# # # # (классе) и защита их от неправильного использования.



# # # #Простая аналогия:

# # # #Таблетка в капсуле. Вы видите только саму капсулу и знаете, 
# # # # что она лечит (например, от головной боли). Вам не нужно знать, 
# # # # какой именно порошок внутри и как он работает. 
# # # # Главное — вы не можете его случайно рассыпать или испортить. 
# # # # Капсула защищает содержимое.


# # #                             #POLUFORMIZM

# # # #Полиморфизм в IT — это способность одного интерфейса работать с разными типами данных.

# # # #Проще говоря,-
# # # # - это когда одно и то же действие можно выполнить разными способами в зависимости от объекта.


# # # #Простая аналогия:

# # # #Кнопка «Пуск» на разных устройствах:

# # # #· На пульте — включает телевизор
# # # #· В автомобиле — заводит двигатель
# # # #· В стиральной машине — запускает стирку

# # # #Действие одно (нажатие на кнопку), - 
# # # # - но результат разный в зависимости от объекта.




# # #                                     #NASLEDOVANIE


# # # #Наследование в IT — это механизм, 
# # # # позволяющий создать новый класс на основе существующего, 
# # # # перенимая его свойства и методы.

# # # #Простая аналогия:

# # # #Ребенок наследует черты родителей.
# # # #  У него есть те же самые глаза, цвет волос,
# # # #  но при этом он может иметь и свои уникальные особенности.
# # # #  Родитель задает основу, а ребенок ее развивает и дополняет.

# # # #Наследование — это основа принципа «является» -
# # # # - (is-a): если Кот наследует Животное, то каждый кот является животным.



# # # #99999999999999999999999999999999999999999999999999


# # # # pygame.init()             ЗапускаетPygame
# # # # pygame.display.set_mode() создает окно
# # # # pygame.event.get()        обработка событий(нажатия клавиш, мыши, закрытие окна)
# # # # pygame.display.flip()     обновляет картину
# # # # while running:            главный цикл игры


# # # #00000000000000000000000000000000000000000000000000000000000000000



# # # 3. Проверяем установку:
# # # Открываем PowerShell или CMD и пишем:



# # # python --version
# # # pip --version



# # # Виртуальное окружение

# # # Чтобы проекты не мешали друг другу, создаём окружение.

# # # В консоли (например, в папке C:\Projects):

# # # python -m venv venv

# # # Активируем окружение:

# # # venv\Scripts\activate

# # # В консоли появится (venv) → значит, окружение работает.

# # # Отключить окружение:

# # # deactivate



# # # Установка Django

# # # В активированном окружении пишем:

# # # pip install django

# # # Проверяем версию:

# # # django-admin --version



# # # Первый проект Django

# # # 1. Создаём проект:



# # # django-admin startproject mysite
# # # cd mysite

# # # 2. Запускаем сервер:



# # # python manage.py runserver

# # # 3. В браузере открываем:
# # #  http://127.0.0.1:8000




# # # #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

# # # from abc import ABC, abstractmethod  

# # # class Animal(ABC):
    
# # #         def __init__ (self, name,age):
# # #                 self.__name = name
# # #                 self.__age = age

# # #         @abstractmethod
# # #         def make_sound(seif):
# # #                 pass

# # #         def eat(seif,food):
# # #                 print(f"{seif._name}est {food}.")

# # #         @property
# # #         def name(seif):
# # #                 return seif._name 
   
# # #         @property
# # #         def age(seif):
      
# # #           class lion(Animal):
# # #             def make_sound(seif):
# # #                print(f"{seif._name}ru4at:RRRRR!")
# # #         def hunt(self):
# # #                  print(f"{self._name} HUNTERing")
# # # class Elephant(Animal):
# # #         def make_sound(self):
# # #                   print(f"{self._name}tribut:tryyyy!")

# # #         def spray_water(self):
# # #                 print(f"{self._name} buruzgaet vodoi!")

# # # class Parrot(Animal):
# # #         def make_sound(self):
# # #                  print(f"{self._name}flu letat")

# # # class Zoo:
# # #         def init(self):
# # #                     self.animalss=[]
                

# # #         def add_animal(self,animal):
# # #                     self.animalss.append(animal)
# # #                     print(f"{animal.name}otpravlen v zoopark")
    

# # #         def show_all_animals(self):
# # #                     print("juvotnue v zooparke")
# # #                     for animal in self.animals:
# # #                         print(f"- {animal.name} {animal.name}, vozrast: {animal.age})")
                          

# # #         def make_all_sounds(self):
# # #                    print("vse juvotnue izdaut zvuki:")
# # #                    for animal in self.animalss:
# # #                         animal.make_sound()

# #                 #mak
# #                 #python3 -m venv venv
# #                 #source venv/bin/activate
# #                 #pip install django
# #                 #django-admin --version
# #                 #django-admin startproject (имя вашего проекта)
# #                   #cd mysite
# #                 #code.
# #                 #python manage.py runserver
# #         #Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
# #  #python —version
# # pip —version
# # python -m venv venv
# # venv\Scripts\activate
# # pip install django
# # django-admin —version
# # django-admin startproject (название проекта)
# # cd (название проекта)
# # code .

#                                           #02-10-2025

# # Объяснение для студентов:

# # · Клиент (браузер) отправляет запросы на сервер
# # · Сервер (Django) обрабатывает запрос, работает с базой данных
# # · Шаблоны рендерятся НА СЕРВЕРЕ - браузер получает готовый HTML
# # · Каждое действие пользователя = новый HTTP-запрос



# # Рекомендуемая структура коммитов:

# # · feat: - новая функциональность
# # · fix: - исправление ошибок
# # · docs: - обновление документации
# # · style: - форматирование, отсутствующие точки с запятой и т.д.
# # · refactor: - рефакторинг кода

# # Этот подход охватывает все указанные темы и дает студентам полное понимание разработки на 
# # Django от основ Python до промышленных практик работы с Git.



 
# # # #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa API

# #API (интерфейс прикладного программирования) — это набор правил,протоколов и определений,
# # которые позволяют разным программным приложениям взаимодействовать 
# # друг с другом и обмениваться данными,по сути,
# # выступая как посредник или "договор" между ними,
# # скрывая сложный внутренний код и предоставляя простой доступ к функциям и информации.





# # models.py = eto hranenie dannux
# #






# #                                       #TEST 1
# # 1. A
# # 2. B
# # 3. C
# # 4. C
# # 5. B
# # 6. B
# # 7. B
# # 8. B
# # 9. B
# # 10. B
# # 11. B
# # 12. A
# # 13. C
# # 14. A
# # 15. B
# # 16. B
# # 17. B
# # 18. A
# # 19. B
# # 20. A
# # 21. A
# # 22. B
# # 23. A
# # 24. C
# # 25. A


# # 26. B
# # 27. B
# # 28. B
# # 29. C
# # 30. A
# # 31. B
# # 32. B
# # 33. B
# # 34. C
# # 35. A
# # 36. B
# # 37. C
# # 38. B
# # 39. A
# # 40. A
# # 41. A
# # 42. B
# # 43. B
# # 44. B
# # 45. A
# # 46. C
# # 47. C
# # 48. A
# # 49. A
# # 50. B


# # 51. B
# # 52. B
# # 53. B
# # 54. C
# # 55. A
# # 56. A
# # 57. B
# # 58. A
# # 59. B
# # 60. C
# # 61. B
# # 62. A
# # 63. B
# # 64. B
# # 65. A
# # 66. B
# # 67. B
# # 68. A
# # 69. B
# # 70. C


#                                              #07.10.2025


# import psycopg2

# try:
#     connection = psycopg2.connect(
#         databasename="rest_api_db",
#         user="postgres",
#         password="12345",
#         host="127.0.0.1",
#         port="5432"
#     )

#     with connection:
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 SELECT table_name 
#                 FROM information_schema.tables
#                 WHERE table_schema='public';
#             """)
#             tables = cursor.fetchall()
#             print("Таблицы в базе данных PostgreSQL:")
#             for table in tables:
#                 print("_", table[0])

#             cursor.execute("SELECT * FROM products_products;")
#             rows = cursor.fetchall()
#             print("\nДанные из таблицы products_products:")
#             for row in rows:
#                 print(row)

# except Exception as e:
#     print("Ошибка:", e)
# finally:
#     if connection:
#         connection.close()


                               #                   #10.10.2025

# """
# Модели приложения

# Определяет все модели данных для приложения.
# """

# from .product import Product, Category, ProductImage
# from .order import Order, OrderItem, OrderStatus
# from .customer import Customer, Address, PaymentMethod
# from .review import Review, Rating

# all = [
#     # Product models
#     'Product',
#     'Category',
#     'ProductImage',
    
#     # Order models
#     'Order', 
#     'OrderItem',
#     'OrderStatus',
    
#     # Customer models
#     'Customer',
#     'Address',
#     'PaymentMethod',
    
#     # Review models
#     'Review',
#     'Rating',
# ]

# # Мета информация
# MODEL_GROUPS = {
#     'product_models': ['Product', 'Category', 'ProductImage'],
#     'order_models': ['Order', 'OrderItem', 'OrderStatus'],
#     'customer_models': ['Customer', 'Address', 'PaymentMethod'],
#     'review_models': ['Review', 'Rating'],
# }


                     # # 1. Product models 13.10.2025

#  pip freeze > requirements.txt   для скачивания всех библиотек в файл





                                                 #ORM
# ORM (Object-Relational Mapping) — это технология, которая позволяет разработчикам взаимодействовать с базой данных
# используя объектно-ориентированный подход вместо написания SQL-запросов напрямую.
# ORM автоматически преобразует объекты в записи базы данных и наоборот,
# упрощая работу с данными и повышая производительность разработки.
# Пример использования ORM в Django:

#Online Reputation Management — это управление репутацией компании в интернете.
#  ORM входит в комплексную стратегию продвижения и создает лояльность клиентов.
#  Он необходим, когда человек услышал о продукте, но еще не оформил покупку.


                   
                                       #STR
 #STR — это аббревиатура, которая имеет несколько основных значений в зависимости от контекста.



# import asyncio

# async def download(name):
#     print(f"Starting download: {name}")
#     await asyncio.sleep(2)  # Simulate a network operation
#     print(f"Finished download: {name}")
#     return f"Data of {name}"
# async def main():
#     tasks = [
#         download("file1.txt"),
#         download("file2.txt"),
#         download("file3.txt")
#     ]
#     results = await asyncio.gather(*tasks)
#     for result in results:
#         print(result)
# if __name__ == "__main__":
#     asyncio.run(main())
import asyncio
import json
import base64
import uuid
import time
from collections import defaultdict, deque

HOST = "localhost"
PORT = 8888

MSG_RATE_LIMIT = 5  # messages per second
RATE_PERIOD = 2  # in seconds

class Client:
    def __init__(self, reader, writer :StreamReader, StreamWriter):
        self.reader = reader
        self.writer = writer
        self.addr = writer.get_extra_info('peername')
        self.msg_timestamps = deque()
        self.id = None
        self.last_messeges = deque()
        self.alive = True

    async def send_json(self,obj):
        data = json.dumps(obj).encode()
        b64_data = base64.b64encode(data).decode()
        self.writer.write((b64_data + "\n").encode())
        await self.writer.drain()

    class ChatServer:
        def __init__(self):
            self.clients = {}
            self.usernames = set()
            self.file_buffers=()

        async def handle_client(self, reader, writer):
            client = Client(reader, writer)
            await self.register_client(client)
            try:
                await client.send_json({"type":"welcome","message":"Welcome to the chat server!"})
                while not reader.at_eof()and client.alive:
                    data = await reader.readline()
                    if not line:
                        break
                    try:
                        msg =json.loads(base64.b64decode(data).decode())
                    except Exception:
                        print(f"Exception client loop  {client.addr}")

                    await self.process_message(client, data.decode().strip())

                                                   #RATE LIMITING

                while client.alive:
                    data = await reader.readline()
                    if not data:
                        break
                    await self.process_message(client, data.decode().strip())
            except Exception as e:
                print(f"Error with client {client.addr}: {e}")
            finally:
                await self.unregister_client(client)

        async def register_client(self, client):
            async with self.lock:
                self.clients[client.addr] = client
                print(f"Client connected: {client.addr}")

        async def unregister_client(self, client):
            async with self.lock:
                if client.addr in self.clients:
                    del self.clients[client.addr]
                    print(f"Client disconnected: {client.addr}")
                client.writer.close()
                await client.writer.wait_closed()

        async def process_message(self, client, data):
            current_time = time.time()
            # Remove timestamps older than RATE_PERIOD
            while client.msg_timestamps and current_time - client.msg_timestamps[0] > RATE_PERIOD:
                client.msg_timestamps.popleft()
            if len(client.msg_timestamps) >= MSG_RATE_LIMIT:
                await client.send_json({"type":"error","message":"Rate limit exceeded. Please wait."})
                return
            client.msg_timestamps.append(current_time)
            try:
                msg = json.loads(base64.b64decode(data).decode())
            except Exception:
                await client.send_json({"type":"error","message":"Invalid message format."})
                return
            msg_type = msg.get("type")
            if msg_type == "register":
                await self.handle_register(client, msg)
            elif msg_type == "message":
                await self.handle_chat_message(client, msg)
            elif msg_type == "file_chunk":
                await self.handle_file_chunk(client, msg)
            else:
                await client.send_json({"type":"error","message":"Unknown message type."})
        async def handle_register(self, client, msg):
            username = msg.get("username")
            if not username:
                await client.send_json({"type":"error","message":"Username is required."})
                return
            async with self.lock:
                if username in self.usernames:
                    await client.send_json({"type":"error","message":"Username already taken."})
                    return
                self.usernames.add(username)
                client.id = str(uuid.uuid4())
                await client.send_json({"type":"registered","id":client.id})
                print(f"User registered: {username} with id {client.id}")

        async def handle_chat_message(self, client, msg):
            if not client.id:
                await client.send_json({"type":"error","message":"You must register first."})
                return
            content = msg.get("content")
            if not content:
                await client.send_json({"type":"error","message":"Message content cannot be empty."})
                return
            broadcast_msg = {
                "type":"message",
                "from":client.id,
                "content":content,
                "timestamp":time.time()
            }
            await self.broadcast_message(broadcast_msg)

        async def broadcast_message(self, msg):
            async with self.lock:
                for client in self.clients.values():
                    await client.send_json(msg)
        async def handle_file_chunk(self, client, msg):
            if not client.id:
                await client.send_json({"type":"error","message":"You must register first."})
                return
            file_id = msg.get("file_id")
            chunk_data = msg.get("data")
            is_last_chunk = msg.get("is_last_chunk", False)
            if not file_id or not chunk_data:
                await client.send_json({"type":"error","message":"File ID and data are required."})
                return
            if file_id not in self.file_buffers:
                self.file_buffers[file_id] = bytearray()
            self.file_buffers[file_id].extend(base64.b64decode(chunk_data))
            if is_last_chunk:
                file_data = self.file_buffers.pop(file_id)
                # Here you would typically save the file_data to disk or process it
                await client.send_json({"type":"file_received","file_id":file_id,"size":len(file_data)})
                print(f"Received complete file {file_id} of size {len(file_data)} bytes from {client.id}")

    async def start_server(self):
        server = await asyncio.start_server(self.handle_client, HOST, PORT)
        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")
        async with server:
            await server.serve_forever()
if __name__ == "__main__":
    chat_server = ChatServer()
    asyncio.run(chat_server.start_server())
    
