
# class Pet:

#     def init(self, name, hunger = 30, energy = 70, mod = 70):
#         self.name = str(name)
#         self.hunger = int(hunger)
#         self.energy = int(energy)
#         self.mod = int(mod)
#         self._clamp()

#     def _clamp(self):
#         self.hunger = max(0, min(100, self.hunger))
#         self.energy = max(0, min(100, self.energy))
#         self.mod = max(0, min(100, self.mod))

#     def feed(self, amount):
#         if amount <= 0:
#             return
#         self.hunger -= int(amount)
#         self.mod -= int(amount * 0.2)
#         self._clamp()

    
#     def play(self, minute):
#         if minute <= 0:
#             return
        
#         self.mod += int(minute *0.8)
#         self.energy += int(minute *0.7)
#         self.hunger += int(minute *0.5)
#         self._clamp()



#     def sleep(self, hours):
#         if hours <= 0 :
#             return
#         self.energy +=int(hours * 25)
#         self.hunger += int(hours * 5)
#         self.mod += int(hours*2)
#         self._clamp()
        

#     def tick(self, minutes = 10):
#         if minutes <= 0 :
#             return
#         self.hunger +=int(minutes * 0.3)
#         self.energy -=int(minutes * 0.2)
#         self.mod -=int(minutes * 0.2)
#         self._clamp()

    
#     def str(self):
#         bars = lambda v: "😒" * (v //10 ) + "-" * (10-v//10)
#         return(f"{self.name}\n" f"Голод: {self.hunger } [{bars(self.hunger)}]\n" f"энергия : {self.energy  } [{bars(self.energy)}]\n"  f"развитие : {self.energy } [{bars(self.energy)}]\n")
    




# if name == "main":
#     pet = Pet("mkdm")

#     print(pet , end="\n\n")

#     pet.feed(1)
#     pet.play(1)
#     pet.sleep(1)
#     pet.tick(1)

#     print(pet)

#     #RGRFNGDVR;ODFLJKCMVF.FLDDD;;;;;;;;;;;;;;;;;77777777777777777777777777777777777777777777777777777777

# import pygame
# import sys

# # инициализация
# pygame.init()

# # окно
# WIDTH, HEIGHT = 600, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создает окно
# pygame.display.set_caption("Первая игра")

# # главный цикл
# running = True
# while running:
#     for event in pygame.event.get():  
#         if event.type == pygame.QUIT: # закрытие окно
#             running = False

#     # заливка фона
#     screen.fill((0,0,0))

#     # обновление экрана
#     pygame.display.flip()

# pygame.quit()
# sys.exit()




# # pygame.init()             ЗапускаетPygame
# # pygame.display.set_mode() создает окно
# # pygame.event.get()        обработка событий(нажатия клавиш, мыши, закрытие окна)
# # pygame.display.flip()     обновляет картину
# # while running:            главный цикл игры

#                            # GANE TIME

# import pygame
# import sys

# # инициализация
# pygame.init()

# # окно
# WIDTH, HEIGHT = 1200, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создает окно
# pygame.display.set_caption("Анимация")

# x,y = 100, 100
# speed_x, speed_y = 3, 2

# clock = pygame.time.Clock()

# # главный цикл
# running = True
# while running:
#     for event in pygame.event.get():  
#         if event.type == pygame.QUIT: # закрытие окно
#             running = False

# # движение
#     x += speed_x
#     y += speed_y

# # отражение от стен
#     if x <= 0 or x >= WIDTH - 50:
#         speed_x = -speed_x

#     if y <= 0 or y >= HEIGHT - 50:
#         speed_y = -speed_y


#     # заливка фона
#     screen.fill((255, 255, 255))

#     pygame.draw.rect(screen,(255, 0, 0),
#                  (x , y , 50, 50))

#     # обновление экрана
#     pygame.display.flip()

#     clock.tick(100)

# pygame.quit()
# sys.exit()  

#00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000




# from os import name
# import telebot
# from abc import ABC, abstractmethod

# # Конфигурация 
# TOKEN  = "8344622545:AAF6wajK2mE2SedQsygrzuNHz-Kt6C07bpk"
# bot = telebot.TeleBot(TOKEN)


# # Абстркный класс для задача
# class AbstractTask(ABC):

#     @abstractmethod
#     def display(self) -> str:
#         """Метод для отображение задачи"""
#         pass


# # Класс для простой задачи
# class Task(AbstractTask):
#     def init(self, description : str):
#         self.description = description
#         self.done = False           #по умолчанию задача не выполнено 
    
#     def mark_done(self):
#         self.done = True

#     def display(self) -> str:
#       status = "✅" if self.done else "❎"
#       return f"{status} {self.description}"
    

# # Менеджер для задач
# class TaskManager:
#     def init(self):
#         self.tasks: list[Task] = []

#     def add_task(self, description: str):
#         task = Task(description)
#         self.tasks.append(task)

#     def remove_task(self, index: int):
#         if 0 <= index < len(self.tasks):
#             self.tasks.pop(index)

#     def mark_done(self, index: int):
#          if 0 <= index < len(self.tasks):
#             self.tasks[index].mark_done()


#     def list_taks(self) -> str:
#         if not self.tasks:
#             return "Список задач пуст."
#         return "\n".join([f"{i+1}.{task.display()}" for i, task in enumerate(self.tasks)])



# # Класс для бота

# class TaskBot:
#     def init(self, bot_instance, manager: TaskManager):
#         self.bot = bot_instance
#         self.manager = manager
#         self.register_handler()

#     def register_handler(self):
#         @self.bot.message_handler(commands = ["start"])

#         def start(message):
#                 self.bot.send_message(message.chat.id,  "Привет! Я бот-менежер задач \n"
#                                         "Команды: \n"
#                                         "/add <задачи> - добавить задачу\n"
#                                         "/list список задач\n "
#                                         "/done <номер> - отметить как выполненное \n"
#                                         "/remove <номер> - удалить задачу" )
                
    

#         @self.bot.message_handler(commands = ["add"])
#         def add(message):
#             task_text = message.text.replace("/add", "").strip()
#             if task_text:
#                 self.manager.add_task(task_text)
#                 self.bot.send_message(message.chat.id,"Задача добавлена ✅")
#             else:
#                 self.bot.send_message(message.chat.id,"Напишите задачу после команды!")


#         @self.bot.message_handler(commands = ["list"])
#         def list_tasks(message):
#             self.bot.send_message(message.chat.id, self.manager.list_taks())


        



#     def run(self):
#         self.bot.polling()



# if name == "main":
#     task_manager = TaskManager()
#     task_bot = TaskBot(bot, task_manager)
#     task_bot.run()