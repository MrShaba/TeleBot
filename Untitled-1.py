print("Hello world,im MR,SHABA")
# pow("damashny'zadania")
# print("hello worlld")
# a = 10
# b = 5

# print("a - b =", a - b)
# print("a + b =", a + b)
# print("a / b =", a / b)
# print("a * b =", a * b)

#                                           #1
# #djskhfuidsjfksdlkfldjfiohrfuejiuj2ei2e2
# print("urok=1")

# age=int(input("18:"))

# if age<18:
#     print("ty nesovershennoletniy")
# else:
#     print("ty vzrosluy")


# #frkfjerkgfkjerjkgjregjerkjejio3ue3ieiie
# print("urok2")
# hour= int(input( 0 < 23))
# if 0<5:
#     print("dobroi vremeni sutok")
# elif 6<11:
#     print("dobroe utro!")
# elif 12<17:
#     print("dobrui den")
# elif 18<23:
#     print("dobrui vecher")
# else:("he chotnoe")
 

# #fjrfrekl;kfgfjlkgkfl;kgkfkljeokekpo23ip
# print("urok3")
# password=("komisar")
# if password ("komisar"):
#     print("dostup:komisar")
# else:
#     print("hevernui:komiser")


# #jdjfiorjigjrjgkrjgjrfkgjfkkwijiwjjwwjjl
# print("urok4")
# secret=9
# guess=int(input(5))
# if guess<9:
#     print("slishkom malo")
# elif guess>5:
#     print("slishkom mnogo")
# else:9>5
# print("!?")


# #kjgrjijejkrejtgigjkgjkrgtjgetkwo[pkrkf]
# print("urok5")
# grade=int(input(1-5))
# if grade==5:
#     print("otlichno!")
# elif grade==4:
#     print("xorosho!")
# elif grade==3:
#     print("nujno podtynut znaniya")
# else:


# #jkhsudiejkhterittoeijfhlautnfdifuirjdkn
#    print("urok6")
# if op =='+':
#    resultat=a+b
# elif op == '_':
#    resultat=a-b
# elif op =='*':
#    resultat=a*b
# elif op =='/':
#  if b!=0:
#   resultat=a/b
# else:

# ifreodihoireihriouiohfjfkdfjfirjiroepji??

                                           #2

# for i in range(1, 15):
#     if i ==9:
#         break
#     print(i)

# # #jdfjifjifjifjifjfifjifjifjifjifjifjifjif
# for i in range(1,18):
#     if i == 10:
#         break
#     if i % 2 == 0:
#         continue
# print(i) 
    
# #jkhjgyhliykjk[piguhk;kihujkjljjohuijjhj]

# while True:
#     password=("hello")
#     javalnvalid=("java")
#     enterpassword:("python")
#     ("Accessallowed")

# #jkhjgyhliykjk[piguhk;kihujkjljjohuijjhj]

#text = "on skazal:\n\"-hello world\""
print("text")

word = "paytan"

print(word[0:5])

txt = "Hello, world!"

print(txt.upper())
print(txt.lower())
print(txt.replace("world", "Python"))

# list - spisok
# tuple - kortej
# set - mnojestvo
# dict - slova
#okokklkkloolllllmmm


student = {"familya": "Али", "возраст": 19, "город": "Бишкек"}
print(student["familya"])
print(student["возраст"])
print(student["город"])
print(student.keys())
print(student.values())

# ##jdjccdcdcdfffffff
# file = open("test.txt"), ("w")
# print(file.write("Hello, world!"))

# print("Hello, world!"),

# print("praktika 2")

text = "Привет, мир!"
upper_text = text.upper()
print(upper_text)  # Выведет: ПРИВЕТ, МИР!

# print("praktika 5")

#student ="name" "ivan",
#print("name student:", student["name"])
#student = {"name": "Ivan", "age": 20, "course": 2}
#print("name student:", student["name"])


# print("praktika 4")
numbers = [1, 2, 5, 6, 5,5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers) # Выведет: [1, 4, 9, 16, 25, 25] 
[1, 4, 9, 16,25,25]

# print("praktika 3")
numbers=[1,2,3]
print("summa:", sum(numbers))  # Выведет: summa: 6
numbers.append(4)
print("posle dobavleniya:", 
      numbers) [1,2,3,4,]
                            

                            #dz3

 # rabota s strokom


user_string = input("1,2,3,4,5,6,7,8,: ")

print(f"samalet: '{user_string[0]}', vertalet: '{user_string[-1]}'")
print("vertalet:", user_string[::2])
print(f"7,8: {len(user_string)} символов 2 а: '{user_string[6:8]}'")

#print("\n" + "="*50 + "\n") 

# rabota s spiskom
games = ["The Witcher 3", "call of duty moble", "crossout", "GTA V"]
print("Список любимых игр 4:", games)

games.append("wormate.io")  # dobavlyaem novuyu igru
print("После добавления новой игры:1", games)

games[1] = "battle cars"  # zamenaem vtoruy ugry
print("После замены одной из игр 5:", games)

print ("Список в обратном порядке:,battle cars,gta v,crossout,wormate.io,the witcher 3,call of duty moble:",
        games[::-1])
#print("\n" + "="*50 + "\n")

# rabota s kortejom 
mixed_tuple = (1, "Python", 3.14, "Java", 42, "C++", "JavaScript")
print("Кортеж:", mixed_tuple)
strings_only = [item for item in mixed_tuple if isinstance(item, str)]
print("Только строки из кортежа:puthon,java,c++,javascript", "strings_tuple")

#print("\n" + "="*50 + "\n")

# rabota s mnojestvom 
numbers_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("Множество чисел:", numbers_set)

numbers_set.discard(5)  # Удаляем 5
print("После удаления 5:", numbers_set)

numbers_set.add(11)  # Добавляем 11
print("После добавления 11:", numbers_set)

print("Есть ли число 7 в множестве?", 10 in numbers_set)

#print("\n" + "="*50 + "\n")

# rabota s slovarem 
car = {
    "марка": "Toyota",
    "модель": "Camry", 
    "год выпуска": 2022
}
print("Данные о машине:toyota camry 2022", car)

car["цвет"] = "cherniy"  # dobavlyem novui cluch i svet
print("После добавления цвета:", car)
car = {
    "mersedes benz"
      : "S-Class",
        "год выпуска":
          2023, "цвет":
            "белый"}
print("Данные о машине:mercedes benz s-class 2023 белый", car)

print("toyota camry 2022 cherniy",list(car.values()))   



                                ## 21.08.25
                                
# print(KDEDJFBFS)
try:
    X = int(input("Введите число X: "))
    print(f"Вы ввели число: {X}")
except ValueError:
    print("Ошибка: Введено не число. Пожалуйста, введите целое число.")

try:
    Y = int(input("Введите число Y: "))
    print(f"Вы ввели число: {Y}")
except ValueError:
    print("Ошибка: Введено не число. Пожалуйста, введите целое число.")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль. Пожалуйста, введите число, отличное от нуля.")

   #try:
    X = int(input("Введите число X: "))
except ValueError:
    print("Ошибка: Введено не число. Пожалуйста, введите целое число.")
else:
    print(f"Вы ввели число: {X}")
finally:
    print("Блок finally выполнен, независимо от наличия ошибок.")


import time

print("Привет! Я - калкулятор- бот.")
print("Доступные операции: + / - / * / %, history, exit")

while True:
    command = input("/n Введите команду: ")
    if  command == "exit":
         print("Выход из программы.")
         break

    elif command == "history":
         pass

    elif command in ["+", "-", "*", "/", "%"]:
      #try:
             a = float(input("145: "))
             b = float(input("150: "))
    elif command == "-":
                    result = a - b
    
    else:
             result = a - b
             print("5", result)

#jkirdk;jdjfofjlejdfmkdkdkcjidjjcimkolml
 
                         #DZ 4

import time

print("hello! mu - kolkulyator & shabdan.")
print("Доступные операции: + / - / * / %, history, exit")

# Список для хранения истории операций
history = []

while True:
    command = input("\nВведите команду: ")
    
    if command == "exit":
        print("Выход из программы.")
        break

    elif command == "history":
        if not history:
            print("История операций пуста.")
        else:
            print("\nИстория операций:")
            for i, operation in enumerate(history, 1):
                print(f"{i}. {operation}")
    
    elif command in ["+", "-", "*", "/", "%"]:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            result = None
            
            if command == "+":
                result = a + b
            elif command == "-":
                result = a - b
            elif command == "*":
                result = a * b
            elif command == "/":
                if b == 0:
                    raise ZeroDivisionError
                result = a / b
            elif command == "%":
                result = a % b
            
            # Форматируем вывод для целых чисел без .0
            if result is not None:
                if result == int(result):
                    result_str = str(int(result))
                else:
                    result_str = str(result)
                    
                operation_str = f"{a} {command} {b} = {result_str}"
                print(f"Результат: {operation_str}")
                
                # Добавляем операцию в историю
                history.append(operation_str)
                
        except ZeroDivisionError:
            error_msg = "Ошибка: деление на ноль невозможно."
            print(error_msg)
            history.append(error_msg)
        except ValueError:
            error_msg = "Ошибка: введите корректные числа."
            print(error_msg)
            history.append(error_msg)

    else:
        print("Неизвестная команда. Пожалуйста, попробуйте еще раз.")
#uieheudgedgeugedgeuuegegdugf



from math import sqrt

def imyafunkcia (parametr):
    #""opisaniye funkcii""
    return parametr*2

def hello(name):
     print("hello", name)
hello("mir")

def power(x, p=2):
    return x**p

print(power(3))
print(power(2,3))

def f(a,/,b,*,c):
     print(a,b,c)
     return a+b+c

f(1,2,c=3)

#rekursia

def area_cirle(r):
     return 3.14*r**2
print(area_cirle(5))

def min_max(tems):
     return min(tems), max(tems)

min_max=min_max([1,2,3,4,5])
print(min_max)

print("praktika 6")

#args, proizvolnoe kol-vo argumetov
#kwargs, proizvolnoe kol-vo imenovannih argumetov


def total(args):
     s=0
     for i in args:
            s+=i
            return s
     print(total(1,2,3,))


def describe_user(**kwars):
     for key, value in kwars,items():
          print(f"{key}:{value}")

describe_user(name="ivan", age=20, city="bishkek")
describe_user(name="alina", age=19, city="osh", job="student")

def demo(a,b=0,*args,verbose = False ,**Kwars):
 if verbose:
            print("a=",a)
            print("b=",b)
            print("args=",args)
            print("kwars=",(Kwars))
 return a+b+sum(args)+sum (Kwars.Values)()

result=demo(1,2,3,4,x=5,y=6,verbose = True)
print("result=", result)

vaiue=[1,2,3]
print(*vaiue) #unpacking raspakovka slovara

squares=lambda x: x*X
add=lambda a,b: a+b
print(squares(5))
print(add(3,4))



nums=[4,5,2,9,1]
print(sorted(nums,key=lambda x: -x)) #sortirovka po ubivaniu
print(sorted(nums,key=lambda x: x%2)) #sortirovka chet-ne

words=["apple","banana","cherry","date"]
print(sorted(words,key=lambda x: len(x))) #sortirovka po dline
print(sorted(words,key=lambda x: x[-1])) #sortirovka po poslednemu simvolu

nums=[1,2,3,4,5]
squared_nums=list(map(lambda x: x*2, nums))
print(squared_nums)
filtered_nums=list(filter(lambda x: x%2==0, nums))
print(filtered_nums)
from functools import reduce
product=reduce(lambda x,y: x*y, nums)


even=list(filter(lambda x: x%2==0, range(10)))
print(even)

def add_item(item,bag=[]):
     bag.append(item)
     return bag

print(add_item("apple"))
print(add_item("banana"))     #soxranyetsya sostayanie spiska bag
print(add_item("cherry",[]))
print(add_item("date"))

def add_item(item, bag=None):
     if bag is None:
          bag=[]
     bag.append(item)
     return bag

print(add_item("apple"))      #kajdui raz sozdaetsya novui spisok bak
print(add_item("banana"))     #ne soxranyetsya sostayanie spiska


def hello():
     """Greets the user."""
     print("Hello, world!")
hello()
print(hello.__doc__)

def foo():
     pass
print(foo.__doc__) #None
print(foo()) #Nonetype 

def name(): #obyablenie funkcii
     """Returns the name of the user."""
     return "Alice"

#args  #karej(1,2,3) #dopolnitelnie pozizionnue argumenti

#kwargs #slovar(name="ivan",age=20) #dopolnitelnie imenovannue argumenti

#return x vozvrashaet znachenie x

#f(seg),g(**dict) #unpacking raspakovka spiska i slovara

func = lambda x: x*2 #lambda funkcia
print([f()for i in range(5)]) #spisok s pomoshyu lambda funkcii
print([i*2 for i in func]) #vse funksii ssulautsya na odnu i ty je!
print(list(map(lambda x: x*2, range(5)))) #spisok s pomoshyu lambda funkcii
print(list(filter(lambda x: x%2==0, range(10)))) #chetniye chisla s pomoshyu lambda funkcii
from functools import reduce


print(reduce(lambda x,y: x+y, range(5))) #summa s pom

print(reduce(lambda x,y: x*y, range(1,6))) #proizvedenie s pomoshyu lambda funkcii


#funcs=[lambda x: x*2, lambda x: x**2, lambda x: x**3]
#print([f(3) for f in funcs]) #primenenie neskolkix lambda funkcii,KAJDAYA FUNKCIA ZAPOMINAET SVOE ZNACHENIE!

print([f(3) for f in funcs]) #primenenie neskolkix lambda funkcii,KAJDAYA FUNKCIA ZAPOMINAET SVOE ZNACHENIE!


                     #DZ

print("Игра - угадай число")

comp = random.randint(1,100)
while True:
    user = int(input("Введите число:"))

if user<comp: 
   print("99")
elif user>comp: 
   print("19") 
else:
    print("vu ugadali ") 

    #FHGFJGKFJLGKFJ

import random

num = 5
print(f"Таблица умножения для числа {num}:")
for i in range(1, 11):
    print(f"{i} × {num} = {i * num}")


Num=5

print ("1 × 5 = 5")
print("2 × 5 = 10")
print("3 × 5 = 15")
print("4 × 5 = 20")
print("5 × 5 = 25")
print("6 × 5 = 30")
print("7 × 5 = 35")
print("8 × 5 = 40")
print("9 × 5 = 45")
print("10 × 5 = 50")


#RJIJJJFKJFIDIJ
#import math

#v144
#$print(math.sqrt(144)) #12.0

#sin(90*)-perovodim gradusy v radianu
#print(math.sin(math.radian990*))) #1.0

#print(math.pi)

#import random


#for I in range(5):
     #print(random.randin(1,100))

#yy79h;lp08yjhjouj

#pip install emoji
#import emoji

#print(emoji.emojize(hello!:smile:))


     #uiy8ykli;kl[lkmlo9ij
     
def add(a,b):
     return a+b
def sub(a,b):
     return a-b
def mul(a,b):
     return a*b
def div(a,b):
     if b==0:
       return "oshibka:delemie na nol1!"
     return a/b 

    #hj8jkkoti
# import  emoji
# print(emoji.emojize("Привет!:smile:"))
# print(emoji.emojize("Python is :thumbs_up:"))
# print(emoji.emojize("Python is :thumbs_down:"))
# print(emoji.emojize("Python is :red_heart:"))

    
                    #DZ
import reguests

def get_users():
   response 
reguests.get('')
print ("spisok polzivatelei:")
for user in users:
     print(user["name"])

if name =="__main__":
     get_users()
#pip install reguests 

#juoifrupoge'ogrt[ofidgcktrpoft] 
# return count 

def count_vowels(s):
     """schitset kolichestvo glasnux bukv v stroke"""
     vowels='shabdan' #russkie i angliskie glasnue
     count = 0
for chat in s.lower():
 if char in vower():
      count +=1

# return count 

def is_palindrome(s):
     """proveryaet,yavlaetsya li stroka palindroma"""
     #yberaem problemu i privodim k nijnemy registury 
     # cleaned = ".join(s.lower().split())"
     return cleaned == cleaned[::-1]


                   #09.04.2025

import os
import telebot
from telebot import types
from telebot.hendler_backends import StatesGroup,state 
from telebot.storage import StateMemoryStorage
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

#POMYAT sostayanii v operativke
state_storage= StateMemoryStorage()

bot = telebot.TeleBOT(TOKEN,state_storage=state_storage)

# [03.09.2025 21:14]
import os
import telebot
from telebot import types
from telebot.handler_backends import StatesGroup_State
from telebot.storage import StateMemoryStorage
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

# Память состояний в оперативке
state_storage = StateMemoryStorage()

bot = telebot.TeleBot(TOKEN, state_storage=state_storage)

# Описываем набор состояний опроса
class Survey(StatesGroup):
    name = State()
    age = State()
    lang = State()

@bot.message_handler(commands=['survey'])
def survey_start(message):
    bot.set_state(message.from_user.id, Survey.name, message.chat.id)
    bot.send_message(message.chat.id, "Как тебя зовут?")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Напиши /survey, чтобы пройти опрос.")


@bot.message_handler(state=Survey.name)
def survey_name(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['name'] = message.text.strip()
    bot.set_state(message.from_user.id, Survey.age, message.chat.id)
    bot.send_message(message.chat.id, "Сколько тебе лет?")

@bot.message_handler(state=Survey.age)
def survey_age(message):
    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Пожалуйста, введи число (возраст).")
        return
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['age'] = int(message.text)



    # выбор языка — через inline
    ikb = types.InlineKeyboardMarkup()
    ikb.add(
        types.InlineKeyboardButton("Русский", callback_data="lang:ru"),
        types.InlineKeyboardButton("English", callback_data="lang:en")
    )
    bot.set_state(message.from_user.id, Survey.lang, message.chat.id)
    bot.send_message(message.chat.id, "Выбери язык:", reply_markup=ikb)

@bot.callback_query_handler(func=lambda c: c.data and c.data.startswith("lang:"))
def survey_lang(call):
    _, lang = call.data.split(":", 1)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['lang'] = lang
        name = data['name']
        age = data['age']

    bot.answer_callback_query(call.id, "Готово!")
    bot.delete_state(call.from_user.id, call.message.chat.id)

    lang_label = "Русский" if lang == "ru" else "English"
    bot.send_message(call.message.chat.id, f"Итоги опроса:\nИмя: {name}\nВозраст: {age}\nЯзык: {lang_label}")

print("Бот запущен (опрос со состояниями)")
bot.polling(none_stop=True)


#222222222222222222222222222222222222222222222

class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float) -> None:
        """Пополнить счет"""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount
        print(f"Счет пополнен на {amount:.2f}. Новый баланс: {self.balance:.2f}")
    
    def withdraw(self, amount: float) -> None:
        """Снять деньги со счета"""
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount
        print(f"Со счета снято {amount:.2f}. Новый баланс: {self.balance:.2f}")
    
    def get_balance(self) -> float:
        """Получить текущий баланс"""
        return self.balance
    
    def __str__(self) -> str:
        return f"Владелец счета: {self.owner}, Баланс: {self.balance:.2f}"

# Пример использования
if name == "__main__":
    try:
        # Создание счета
        account = Account("Иван Иванов", 1000.0)
        print(account)
        
        # Пополнение счета
        account.deposit(500.0)
        
        # Снятие денег
        account.withdraw(200.0)
        
        # Попытка снять больше, чем есть на счете
        try:
            account.withdraw(2000.0)
        except ValueError as e:
            print(f"Ошибка: {e}")
            
        # Получение баланса
        print(f"Текущий баланс: {account.get_balance():.2f}")
        
    except ValueError as e:
        print(f"Ошибка создания счета: {e}")


#333333333333333333333333333333333333333333333333333333333333333333333333333333333333333

class BankAccount:
    def init(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # двойной подчеркивание делает атрибут приватным

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance
    


acc = BankAccount("aliya", 1000)
print(acc.get_balance())

acc.__balance = 500
print(acc.get_balance())

#44444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444

class BankAccount:

    def init(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # двойной подчеркивание делает атрибут приватным

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount >= 0 :
            self.__balance = amount


acc = BankAccount("Bek", 500)
print(acc.balance)

acc.balance = 1000
print(acc.balance)

acc.balance = -500
print(acc.balance)

#555555555555555555555555555555555555555555555555555555555555555555555555555555
                                                                                   #OP
                                                                                   
class Animal:
    def speak(self):
        print("Животное издает звук")

    def jump(self):
        print("Животное умеет прыгать")



class Dog(Animal):
    def speak(self):
        super().speak()
        print("Собака лает громко!")

d = Dog()
d.speak()

        


# class Cat(Animal):
     
#     def speak(self):
#         print(" мяу мяу!")

#     def jump(self):
#         print("Передний сальто")


# d = Dog()
# c = Cat()

# d.speak()
# d.jump()

# c.speak()
# c.jump()

# animals = [Dog(), Cat()]

# for animal in animals:
#     animal.speak()

#01010101010101010101010101101010101010110

from abc import ABC, abstractmethod

class Pet(ABC):
    def init(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Pet):
    
    def sound(self):
        print(f"{self.name} говорит: гав гав")


class Cat(Pet):

    def sound(self):
        print(f"{self.name} говорит: мяу мяу")


# d = Dog("Шарик")
# c = Cat("Барсик")

# d.sound()
# c.sound()



pets = [Dog("Альма"), Cat("Мурка")]

for pet in pets:
    pet.sound()

#000000000000000000000000000000000000000

#1  Создать абстрактный класс Bicycle с методом drive().
#2. Сделать дочерние классы: Car, Bike, Truck.
#3. В цикле пройтись по списку всех транспортных средств и вызвать drive().


from abc import ABC, abstractmethod

   # 1. Создать абстрактный класс Bicycle с методом drive()
class Bicycle(ABC):
    @abstractmethod
    def drive(self):
        pass

   # 2. Сделать дочерние классы: Car, Bike, Truck
class Car(Bicycle):
    def drive(self):
        return "Машина едет по дороге"

class Bike(Bicycle):
    def drive(self):
        return "Велосипед едет по велодорожке"

class Truck(Bicycle):
    def drive(self):
        return "Грузовик перевозит груз"

    # 3. В цикле пройтись по списку всех транспортных средств и вызвать drive()
if name == "__main__":
    # Создаем список транспортных средств
    vehicles = [
        Car(),    
        Bike(),
        Truck()
    ]
    
    # Проходим по списку и вызываем метод drive() для каждого транспортного средства
    for vehicle in vehicles:
        print(vehicle.drive())

        #Машина едет по дороге>
        #Велосипед едет по велодорожке>
        #Грузовик перевозит груз>

#000000000000000000000000000000000000000000000000000000000

from abc import ABC, abstractmethod

# Более логичное название базового класса
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        return "Машина едет по дороге"

class Bike(Vehicle):
    def drive(self):
        return "Велосипед едет по велодорожке"

class Truck(Vehicle):
    def drive(self):
        return "Грузовик перевозит груз"

# Использование
if name == "__main__":
    vehicles = [Car(), Bike(), Truck()]
    
    for vehicle in vehicles:
        print(f"{vehicle.__class__.__name__}: {vehicle.drive()}")

             #Car: Машина едет по дороге
             #Bike: Велосипед едет по велодорожке
             #Truck: Грузовик перевозит груз

#00000000000000000000000000000000000000000000000000000000000000000000000000OP
                                                                                  #OP

  

import json
import random
import time
from abc import ABC, abstractmethod
from typing import List

# -------------------------
#       УТИЛИТЫ
# -------------------------

def clamp(v, a=0, b=9999):
    """Удобная функция для ограничения значений."""
    return max(a, min(b, v))

def read_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Читает int из ввода с защитой."""
    while True:
        try:
            s = input(prompt)
            val = int(s)
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Введите число между {min_val} и {max_val}.")
                continue
            return val
        except ValueError:
            print("Ошибка: введите целое число.")


# -------------------------
#     КЛАССЫ ПРЕДМЕТОВ
# -------------------------

class Item:
    """Базовый предмет."""
    def __init__(self, name: str, description: str = "", weight: float = 0.0, value: int = 0):
        self.name = name
        self.description = description
        self.weight = float(weight)
        self.value = int(value)

    def use(self, user, target=None):
        """Что происходит при использовании предмета. Переопределяется."""
        print(f"{self.name} нельзя использовать прямо так.")

    def to_dict(self):
        return {"type": self.__class__.__name__, "name": self.name, "description": self.description,
                "weight": self.weight, "value": self.value}

    @classmethod
    def from_dict(cls, d):
        t = d.get("type", "Item")
        if t == "Weapon":
            return Weapon(d["name"], d.get("attack", 0), description=d.get("description",""), value=d.get("value",0))
        if t == "Consumable":
            return Consumable(d["name"], d.get("heal",0), description=d.get("description",""), value=d.get("value",0))
        # default
        return Item(d["name"], d.get("description",""), d.get("weight",0.0), d.get("value",0))

    def __str__(self):
        return f"Item({self.name})"


class Weapon(Item):
    """Оружие, увеличивает урон при атаке."""
    def __init__(self, name: str, attack: int, description: str = "", value: int = 0):
        super().__init__(name, description, weight=1.0, value=value)
        self.attack = int(attack)

    def to_dict(self):
        d = super().to_dict()
        d["attack"] = self.attack
        return d

    def __str__(self):
        return f"Weapon({self.name}, atk={self.attack})"


class Consumable(Item):
    """Съедобный предмет, восстанавливает HP."""
    def __init__(self, name: str, heal: int, description: str = "", value: int = 0):
        super().__init__(name, description, weight=0.2, value=value)
        self.heal = int(heal)

    def use(self, user, target=None):
        # target игнорируется — применяется к пользователю
        healed = user.heal(self.heal)
        print(f"{user.name} использовал {self.name} и восстановил {healed} HP.")

    def to_dict(self):
        d = super().to_dict()
        d["heal"] = self.heal
        return d

    def __str__(self):
        return f"Consumable({self.name}, heal={self.heal})"


# -------------------------
#    АБСТРАКТНЫЙ CHARACTER
# -------------------------

#Основные исправления:

#1. Метод __init__ вместо init - в Python конструктор класса называется init, а не init
#2. self.__class__.__name__ вместо self.class.name - правильный способ получить имя класса
#3. Добавлен метод __str__ для базового класса Item - для корректного строкового представления
#4. Исправлен вызов super() - в дочерних классах используется super().__init__() вместо super().init()
#5. Исправлены опечатки - например, str вместо str для магических методов

#Эти исправления обеспечат правильную работу классов предметов и их методов.




# -------------------------4444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444


import json
import random
import time
from abc import ABC, abstractmethod
from typing import List

# -------------------------
#       УТИЛИТЫ
# -------------------------

def clamp(v, a=0, b=9999):
    """Удобная функция для ограничения значений."""
    return max(a, min(b, v))

def read_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Читает int из ввода с защитой."""
    while True:
        try:
            s = input(prompt)
            val = int(s)
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Введите число между {min_val} и {max_val}.")
                continue
            return val
        except ValueError:
            print("Ошибка: введите целое число.")


# -------------------------
#     КЛАССЫ ПРЕДМЕТОВ
# -------------------------

class Item:
    """Базовый предмет."""
    def __init__(self, name: str, description: str = "", weight: float = 0.0, value: int = 0):
        self.name = name
        self.description = description
        self.weight = float(weight)
        self.value = int(value)

    def use(self, user, target=None):
        """Что происходит при использовании предмета. Переопределяется."""
        print(f"{self.name} нельзя использовать прямо так.")

    def to_dict(self):
        return {"type": self.__class__.__name__, "name": self.name, "description": self.description,
                "weight": self.weight, "value": self.value}

    @classmethod
    def from_dict(cls, d):
        t = d.get("type", "Item")
        if t == "Weapon":
            return Weapon(d["name"], d.get("attack", 0), description=d.get("description",""), value=d.get("value",0))
        if t == "Consumable":
            return Consumable(d["name"], d.get("heal",0), description=d.get("description",""), value=d.get("value",0))
        # default
        return Item(d["name"], d.get("description",""), d.get("weight",0.0), d.get("value",0))

    def __str__(self):
        return f"Item({self.name})"


class Weapon(Item):
    """Оружие, увеличивает урон при атаке."""
    def __init__(self, name: str, attack: int, description: str = "", value: int = 0):
        super().__init__(name, description, weight=1.0, value=value)
        self.attack = int(attack)

    def to_dict(self):
        d = super().to_dict()
        d["attack"] = self.attack
        return d

    def __str__(self):
        return f"Weapon({self.name}, atk={self.attack})"


class Consumable(Item):
    """Съедобный предмет, восстанавливает HP."""
    def __init__(self, name: str, heal: int, description: str = "", value: int = 0):
        super().__init__(name, description, weight=0.2, value=value)
        self.heal = int(heal)

    def use(self, user, target=None):
        # target игнорируется — применяется к пользователю
        healed = user.heal(self.heal)
        print(f"{user.name} использовал {self.name} и восстановил {healed} HP.")

    def to_dict(self):
        d = super().to_dict()
        d["heal"] = self.heal
        return d

    def __str__(self):
        return f"Consumable({self.name}, heal={self.heal})"


# -------------------------
#    АБСТРАКТНЫЙ CHARACTER2
# -------------------------
#55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555

from abc import ABC, abstractmethod

#Abstraksya
class ingredient(ABC):
    def __init__(self,name,cost):
        self._name=name 
        self._cost=cost 

    @abstractmethod
    def get_cost(self):
        pass

    @abstractmedhod
    def det_cost_(self):
        pass

    @property
    def name(self):
        return self._name 
    
  #nasledovanie
class Meat(ingredienty):
    def __init__(self,name,cost,fat_percent):
        super().init(name,cost)
        self.fat_percent=fat_percent

    def prepare(self):
             print(f"MIYASO{self._name}narezono i objareno(jirnos:{self.fat_percent}%)")
    
    def get_cost(self):
        return self._cost*1.7 #doroje myaso
    
class Vegetable(ingredient):
    def __init__(self,name,cost,is_spicy):
        super().init(name,cost,)
        self.is_spisy=is_spicy

    def prepare(self):
        spicy="osturui" if self.is_spicy else "ne osturui"
        print(f"ovosh{self._name}narezan({spicy})")

    def grt_cost(self):
        return self._cost
    
class Noodles(ingredient):
    def prepare(self):
        print(f"lapsha {self._name}bushty")

    def det_cost(self):
        return self._cost *1.4 #lapsha deshevle
    

#INKAPSULATSIAYA
class Lagman:

    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.__ingredients.append(ingredient)
        print(f"Добавлен ингредиент: {ingredient.name}")

    def cook(self):
        print("Готовим лагман:")
        for ing in self.__ingredients:
            ing.prepare()
        print("Лагман готов!")

    def calculate_total_cost(self):
        return sum(ing.get_cost() for ing in self.__ingredients)

# Kitchen — xranit dostupnue ingliedenti
class Kitchen:
    def __init__(self):
        self.ingredients = {}

    def add_ingredient(self, ingredient):
        self.ingredients[ingredient.name] = ingredient

    def make_lagman(self, recipe):
        lagman = Lagman()
        for name in recipe:
            if name not in self.ingredients:
                raise Exception(f"Ингредиент '{name}' не найден!")
            lagman.add_ingredient(self.ingredients[name])
        lagman.cook()
        print(f"Общая стоимость: {lagman.calculate_total_cost()} руб.")
        return lagman

    from abc import ABC, abstractmethod

# Абстракция
class Ingredient(ABC):
    def init(self, name, cost):
        self._name = name
        self._cost = cost

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    @property
    def name(self):
        return self._name

# Наследование
class Meat(Ingredient):
    def init(self, name, cost, fat_percent):
        super().init(name, cost)
        self.fat_percent = fat_percent

    def prepare(self):
        print(f"Мясо {self._name} нарезано и обжарено (жирность: {self.fat_percent}%)")

    def get_cost(self):
        return self._cost * 1.5  # мясо дороже

class Vegetable(Ingredient):
    def init(self, name, cost, is_spicy):
        super().init(name, cost)
        self.is_spicy = is_spicy

    def prepare(self):
        spicy = "острый" if self.is_spicy else "не острый"
        print(f"Овощ {self._name} нарезан ({spicy})")

    def get_cost(self):
        return self._cost

class Noodles(Ingredient):
    def prepare(self):
        print(f"Лапша {self._name} сварена")

    def get_cost(self):
        return self._cost * 0.8  # лапша дешевле

# Инкапсуляция
class Lagman:
    def init(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.__ingredients.append(ingredient)
        print(f"Добавлен ингредиент: {ingredient.name}")

    def cook(self):
        print("Готовим лагман:")
        for ing in self.__ingredients:
            ing.prepare()
        print("Лагман готов!")

    def calculate_total_cost(self):
        return sum(ing.get_cost() for ing in self.__ingredients)

# Kitchen — хранит доступные ингредиенты
class Kitchen:
    def __init(self):
        self.ingredients = {}

    def add_ingredient(self, ingredient):
        self.ingredients[ingredient.name] = ingredient

    def make_lagman(self, recipe):
        lagman = Lagman()
        for name in recipe:
            if name not in self.ingredients:
                raise Exception(f"Ингредиент '{name}' не найден!")
            lagman.add_ingredient(self.ingredients[name])
        lagman.cook()
        print(f"Общая стоимость: {lagman.calculate_total_cost()} руб.")
        return lagman

# Пример использования:
kitchen = Kitchen()
kitchen.add_ingredient(Meat("Говядина", 100, 20))
kitchen.add_ingredient(Vegetable("Перец", 30, True))
kitchen.add_ingredient(Vegetable("Морковь", 20, False))
kitchen.add_ingredient(Noodles("Домашняя лапша", 40))

recipe = ["Говядина", "Перец", "Морковь", "Домашняя лапша"]
try:
    kitchen.make_lagman(recipe)
except Exception as e:
    print(e)



                 # IGRA ZIMEIKA

import pygame
import sys
import random

# Инициализация
pygame.init()

# Константы
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 120, 255)
DARK_GREEN = (0, 180, 0)
GRAY = (40, 40, 40)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

# Шрифт
font = pygame.font.SysFont('Arial', 25)
big_font = pygame.font.SysFont('Arial', 50)

class Snake:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.length = 3
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.score = 0
        self.grow_to = 3
        self.alive = True
    
    def get_head_position(self):
        return self.positions[0]
    
    def move(self):
        if not self.alive:
            return
            
        head_x, head_y = self.get_head_position()
        dir_x, dir_y = self.direction
        new_x = (head_x + dir_x) % GRID_WIDTH
        new_y = (head_y + dir_y) % GRID_HEIGHT
        
        # Проверка на столкновение с собой
        if (new_x, new_y) in self.positions[1:]:
            self.alive = False
            return
            
        self.positions.insert(0, (new_x, new_y))
        
        if len(self.positions) > self.grow_to:
            self.positions.pop()
    
    def draw(self):
        for i, (x, y) in enumerate(self.positions):
            color = GREEN if i == 0 else DARK_GREEN  # Голова зеленее
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)  # Обводка
    
    def change_direction(self, direction):
        # Запрещаем движение в противоположном направлении
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1), 
                         random.randint(0, GRID_HEIGHT - 1))
    
    def draw(self):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, 
                          self.position[1] * GRID_SIZE, 
                          GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, RED, rect)
        pygame.draw.rect(screen, BLACK, rect, 1)  # Обводка

    def draw_grid():
        for x in range(0, WIDTH, GRID_SIZE):
          pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
          pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

    def draw_score(score):
       score_text = font.render(f'Счет: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    def draw_game_over(score):
      overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    
    game_over_text = big_font.render('ИГРА ОКОНЧЕНА!', True, RED)
    score_text = font.render(f'Ваш счет: {score}', True, WHITE)
    restart_text = font.render('Нажмите R для новой игры', True, WHITE)
    
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 60))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 40))


def main():
    snake = Snake()
    food = Food()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if not snake.alive and event.key == pygame.K_r:
                    snake.reset()
                    food.randomize_position()
                elif snake.alive:
                    if event.key == pygame.K_UP:
                        snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction((1, 0))
        
        # Движение змейки
        snake.move()
        
        # Проверка на съедание еды
        if snake.alive and snake.get_head_position() == food.position:
            snake.grow_to += 1
            snake.score += 10
            food.randomize_position()
            # Убедимся, что еда не появилась на змейке
            while food.position in snake.positions:
                food.randomize_position()
        
        # Отрисовка
        screen.fill(BLACK)
        draw_grid()
        food.draw()
        snake.draw()
        draw_score(snake.score)
        
        if not snake.alive:
            draw_game_over(snake.score)
        
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()


                                                #THE DJANGO
                        

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField()
    email = models.EmailField(unique=True)


    def str(self):
        return f"{self.name} ({self.age} лет)"
    #11111111111111111111111111111111111111111111

from django.http import HttpResponse
from .models import User

def home(request):
    return HttpResponse("tmkvnvkndkvndkvnk")


def user_list(request):
    users = User.objects.all()
    text = ""
    for u in users:
        text += f"{u.name}, {u.age}лет, {u.email}<br>"
    return HttpResponse(text)

   #2222222222222222222222222222222222222222222222

   #from django.contrib import admin
from django.urls import path
from db_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('users/', views.user_list)
]

  #33333333333333333333333333333333333333333333333


from django.contrib import admin
from .models import User

admin.site.register(User)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name', 'age', 'email', )
#     search_fields = ('name', 'email',)
#     list_filter = ('age',)

# admin.site.register(User, UserAdmin)


#27.9.2025

from django import forms
from .models import Feedback, Message

# Обычная форма
class FeedbackForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100)
    email = forms.EmailField(label="Email")
    message = forms.CharField(label="Сообщение", widget=forms.Textarea)

# Модельная форма
class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'text']

        from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.name} - {self.email}"
    

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    from django.shortcuts import render, redirect
from .form import FeedbackForm, FeedbackModelForm, MessageForm

def feedback_view(request):
    form = FeedbackForm()
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return render(request, 'form/success.html', {'name': name})
    return render(request, 'form/feedback.html', {'form': form})

def feedback_model_view(request):
    form = FeedbackModelForm()
    if request.method == "POST":
        form = FeedbackModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form/success.html', {'name': form.cleaned_data['name']})
    return render(request, 'form/feedback.html', {'form': form})



def message_view(request):
    if request.method == "GET":
        form = MessageForm()
        return render(request, "message.html", {"form": form})

