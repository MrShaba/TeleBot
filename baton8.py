# # # # import pygame
# # # # import sys

# # # # # инициализация
# # # # pygame.init()

# # # # # окно
# # # # WIDTH, HEIGHT = 1200, 400
# # # # screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создает окно
# # # # pygame.display.set_caption("Анимация")

# # # # x,y = 100, 100
# # # # speed_x, speed_y = 3, 2

# # # # clock = pygame.time.Clock()

# # # # # главный цикл
# # # # running = True
# # # # while running:
# # # #     for event in pygame.event.get():  
# # # #         if event.type == pygame.QUIT: # закрытие окно
# # # #             running = False

# # # # # движение
# # # #     x += speed_x
# # # #     y += speed_y

# # # # # отражение от стен
# # # #     if x <= 0 or x >= WIDTH - 50:
# # # #         speed_x = -speed_x

# # # #     if y <= 0 or y >= HEIGHT - 50:
# # # #         speed_y = -speed_y


# # # #     # заливка фона
# # # #     screen.fill((255, 255, 255))

# # # #     pygame.draw.rect(screen,(255, 0, 0),
# # # #                  (x , y , 50, 50))

# # # #     # обновление экрана
# # # #     pygame.display.flip()

# # # #     clock.tick(100)

# # # # pygame.quit()
# # # # sys.exit()


# # # #uuuuuuuuuuuuuuuuuuuu
# # # import pygame
# # # import sys
# # # import random

# # # # Инициализация
# # # pygame.init()

# # # # Окно
# # # WIDTH, HEIGHT = 1200, 400
# # # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # # pygame.display.set_caption("Простая RPG")

# # # # Цвета
# # # WHITE = (255, 255, 255)
# # # RED = (255, 0, 0)
# # # GREEN = (0, 255, 0)
# # # BLUE = (0, 0, 255)
# # # BLACK = (0, 0, 255)

# # # # Игрок
# # # class Player:
# # #     def __init__(self):
# # #         self.x = 400
# # #         self.y = 400
# # #         self.width = 50
# # #         self.height = 50
# # #         self.speed = 10
# # #         self.health = 50
# # #         self.score = 1
    
# # #     def move(self, keys):
# # #         if keys[pygame.K_LEFT] and self.x > 0:
# # #             self.x -= self.speed
# # #         if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
# # #             self.x += self.speed
# # #         if keys[pygame.K_UP] and self.y > 0:
# # #             self.y -= self.speed
# # #         if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
# # #             self.y += self.speed
    
# # #     def draw(self):
# # #         pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
# # #         # Полоска здоровья
# # #         pygame.draw.rect(screen, RED, (self.x, self.y - 10, self.width, 5))
# # #         pygame.draw.rect(screen, GREEN, (self.x, self.y - 10, self.width * (self.health / 100), 5))

# # # # Враг
# # # class Enemy:
# # #     def __init__(self):
# # #         self.x = random.randint(200, WIDTH - 50)
# # #         self.y = random.randint(0, HEIGHT - 50)
# # #         self.width = 40
# # #         self.height = 40
# # #         self.speed_x = random.choice([-2, -1, 1, 2])
# # #         self.speed_y = random.choice([-2, -1, 1, 2])
# # #         self.health = 30
    
# # #     def update(self):
# # #         self.x += self.speed_x
# # #         self.y += self.speed_y
        
# # #         # Отражение от стен
# # #         if self.x <= 0 or self.x >= WIDTH - self.width:
# # #             self.speed_x = -self.speed_x
# # #         if self.y <= 0 or self.y >= HEIGHT - self.height:
# # #             self.speed_y = -self.speed_y
    
# # #     def draw(self):
# # #         pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))

# # # # Пуля
# # # class Bullet:
# # #     def __init__(self, x, y):
# # #         self.x = x
# # #         self.y = y
# # #         self.width = 10
# # #         self.height = 5
# # #         self.speed = 10
# # #         self.direction = 1  # 1 - вправо, -1 - влево
    
# # #     def update(self):
# # #         self.x += self.speed * self.direction
    
# # #     def draw(self):
# # #         pygame.draw.rect(screen, BLACK, (self.x, self.y, self.width, self.height))

# # # # Создание объектов
# # # player = Player()
# # # enemies = [Enemy() for _ in range(5)]
# # # bullets = []
# # # font = pygame.font.SysFont(None, 36)

# # # # Главный цикл
# # # clock = pygame.time.Clock()
# # # running = True

# # # while running:
# # #     for event in pygame.event.get():  
# # #         if event.type == pygame.QUIT:
# # #             running = False
# # #         if event.type == pygame.KEYDOWN:
# # #             if event.key == pygame.K_SPACE:
# # #                 # Создание пули
# # #                 bullets.append(Bullet(player.x + player.width, player.y + player.height // 2))
    
# # #     # Управление игроком
# # #     keys = pygame.key.get_pressed()
# # #     player.move(keys)
    
# # #     # Обновление врагов
# # #     for enemy in enemies:
# # #         enemy.update()
    
# # #     # Обновление пуль
# # #     for bullet in bullets[:]:
# # #         bullet.update()
# # #         if bullet.x > WIDTH:
# # #             bullets.remove(bullet)
    
# # #     # Проверка столкновений пуль с врагами
# # #     for bullet in bullets[:]:
# # #         for enemy in enemies[:]:
# # #             if (bullet.x < enemy.x + enemy.width and
# # #                 bullet.x + bullet.width > enemy.x and
# # #                 bullet.y < enemy.y + enemy.height and
# # #                 bullet.y + bullet.height > enemy.y):
                
# # #                 enemy.health -= 10
# # #                 if enemy.health <= 0:
# # #                     enemies.remove(enemy)
# # #                     player.score += 10
# # #                     enemies.append(Enemy())  # Новый враг
# # #                 if bullet in bullets:
# # #                     bullets.remove(bullet)
# # #                 break
    
# # #     # Проверка столкновений игрока с врагами
# # #     for enemy in enemies:
# # #         if (player.x < enemy.x + enemy.width and
# # #             player.x + player.width > enemy.x and
# # #             player.y < enemy.y + enemy.height and
# # #             player.
# # #     y + player.height > enemy.y):
            
# # #             player.health -= 1
# # #             if player.health <= 0:
# # #                 running = False
    
# # #     # Отрисовка
# # #     screen.fill(WHITE)
    
# # #     # Отрисовка объектов
# # #     player.draw()
# # #     for enemy in enemies:
# # #         enemy.draw()
# # #     for bullet in bullets:
# # #         bullet.draw()
    
# # #     # Отрисовка счета
# # #     score_text = font.render(f"Счет: {player.score}", True, BLACK)
# # #     health_text = font.render(f"Здоровье: {player.health}", True, BLACK)
# # #     screen.blit(score_text, (10, 10))
# # #     screen.blit(health_text, (10, 50))
    
# # #     # Обновление экрана
# # #     pygame.display.flip()
# # #     clock.tick(60)

# # # pygame.quit()
# # # sys.exit()



# #                               #zmeika game

# # import pygame
# # import sys
# # import random

# # # Инициализация
# # pygame.init()

# # # Константы
# # WIDTH, HEIGHT = 600, 600
# # GRID_SIZE = 20
# # GRID_WIDTH = WIDTH // GRID_SIZE
# # GRID_HEIGHT = HEIGHT // GRID_SIZE
# # FPS = 10

# # # Цвета
# # BLACK = (0, 0, 0)
# # WHITE = (255, 255, 255)
# # GREEN = (0, 255, 0)
# # RED = (255, 0, 0)
# # BLUE = (0, 120, 255)
# # DARK_GREEN = (0, 180, 0)
# # GRAY = (40, 40, 40)

# # # Создание окна
# # screen = pygame.display.set_mode((WIDTH, HEIGHT))
# # pygame.display.set_caption("Змейка")
# # clock = pygame.time.Clock()

# # # Шрифт
# # font = pygame.font.SysFont('Arial', 25)
# # big_font = pygame.font.SysFont('Arial', 50)

# # class Snake:
# #     def __init__(self):
# #         self.reset()
    
# #     def reset(self):
# #         self.length = 3
# #         self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
# #         self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
# #         self.score = 0
# #         self.grow_to = 3
# #         self.alive = True
    
# #     def get_head_position(self):
# #         return self.positions[0]
    
# #     def move(self):
# #         if not self.alive:
# #             return
            
# #         head_x, head_y = self.get_head_position()
# #         dir_x, dir_y = self.direction
# #         new_x = (head_x + dir_x) % GRID_WIDTH
# #         new_y = (head_y + dir_y) % GRID_HEIGHT
        
# #         # Проверка на столкновение с собой
# #         if (new_x, new_y) in self.positions[1:]:
# #             self.alive = False
# #             return
            
# #         self.positions.insert(0, (new_x, new_y))
        
# #         if len(self.positions) > self.grow_to:
# #             self.positions.pop()
    
# #     def draw(self):
# #         for i, (x, y) in enumerate(self.positions):
# #             color = GREEN if i == 0 else DARK_GREEN  # Голова зеленее
# #             rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
# #             pygame.draw.rect(screen, color, rect)
# #             pygame.draw.rect(screen, BLACK, rect, 1)  # Обводка
    
# #     def change_direction(self, direction):
# #         # Запрещаем движение в противоположном направлении
# #         if (direction[0] * -1, direction[1] * -1) != self.direction:
# #             self.direction = direction

# # class Food:
# #     def __init__(self):
# #         self.position = (0, 0)
# #         self.randomize_position()
    
# #     def randomize_position(self):
# #         self.position = (random.randint(0, GRID_WIDTH - 1), 
# #                          random.randint(0, GRID_HEIGHT - 1))
    
# #     def draw(self):
# #         rect = pygame.Rect(self.position[0] * GRID_SIZE, 
# #                           self.position[1] * GRID_SIZE, 
# #                           GRID_SIZE, GRID_SIZE)
# #         pygame.draw.rect(screen, RED, rect)
# #         pygame.draw.rect(screen, BLACK, rect, 1)  # Обводка

# # def draw_grid():
# #     for x in range(0, WIDTH, GRID_SIZE):
# #         pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
# #     for y in range(0, HEIGHT, GRID_SIZE):
# #         pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

# # def draw_score(score):
# #     score_text = font.render(f'Счет: {score}', True, WHITE)
# #     screen.blit(score_text, (10, 10))

# # def draw_game_over(score):
# #     overlay = pygame.Surface((WIDTH, HEIGHT))
# #     overlay.set_alpha(180)
# #     overlay.fill(BLACK)
# #     screen.blit(overlay, (0, 0))
    
# #     game_over_text = big_font.render('ИГРА ОКОНЧЕНА!', True, RED)
# #     score_text = font.render(f'Ваш счет: {score}', True, WHITE)
# #     restart_text = font.render('Нажмите R для новой игры', True, WHITE)
    
# #     screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 60))
# #     screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
# #     screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 40))

# # def main():
# #     snake = Snake()
# #     food = Food()
    
# #     while True:
# #         for event in pygame.event.get():
# #             if event.type == pygame.QUIT:
# #                 pygame.quit()
# #                 sys.exit()
# #             elif event.type == pygame.KEYDOWN:
# #                 if not snake.alive and event.key == pygame.K_r:
# #                     snake.reset()
# #                     food.randomize_position()
# #                 elif snake.alive:
# #                     if event. key == pygame.K_UP: snake.change_direction((0, -1))
# #                 elif event.key == pygame.K_DOWN:
# #                         snake.change_direction((0, 1))
# #             elif event.key == pygame.K_LEFT:
# #                         snake.change_direction((-1, 0))
# #             elif event.key == pygame.K_RIGHT:
# #                         snake.change_direction((1, 0))
        
# #         # Движение змейки
# #         snake.move()
        
# #         # Проверка на съедание еды
# #         if snake.alive and snake.get_head_position() == food.position:
# #             snake.grow_to += 1
# #             snake.score += 10
# #             food.randomize_position()
# #             # Убедимся, что еда не появилась на змейке
# #             while food.position in snake.positions:
# #                 food.randomize_position()
        
# #         # Отрисовка
# # screen.fill(BLACK)
# # draw_grid()
# # Food.draw()
# # Snake.draw()
# # draw_score(Snake.score)
        
# # if not Snake.alive:
# #             draw_game_over(Snake.score)
        
# # pygame.display.flip()
# # clock.tick(FPS)

# # if name == "__main__":
# #     main()




# import pygame
# import sys
# import random

# # Инициализация
# pygame.init()

# # Константы
# WIDTH, HEIGHT = 600, 600
# GRID_SIZE = 20
# GRID_WIDTH = WIDTH // GRID_SIZE
# GRID_HEIGHT = HEIGHT // GRID_SIZE
# FPS = 10

# # Цвета
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 120, 255)
# DARK_GREEN = (0, 180, 0)
# GRAY = (40, 40, 40)

# # Создание окна
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Змейка")
# clock = pygame.time.Clock()

# # Шрифт
# font = pygame.font.SysFont('Arial', 25)
# big_font = pygame.font.SysFont('Arial', 50)

# class Snake:
#     def __init__(self):
#         self.reset()
    
#     def reset(self):
#         self.length = 3
#         self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
#         self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
#         self.score = 0
#         self.grow_to = 3
#         self.alive = True
    
#     def get_head_position(self):
#         return self.positions[0]
    
#     def move(self):
#         if not self.alive:
#             return
            
#         head_x, head_y = self.get_head_position()
#         dir_x, dir_y = self.direction
#         new_x = (head_x + dir_x) % GRID_WIDTH
#         new_y = (head_y + dir_y) % GRID_HEIGHT
        
#         # Проверка на столкновение с собой
#         if (new_x, new_y) in self.positions[1:]:
#             self.alive = False
#             return
            
#         self.positions.insert(0, (new_x, new_y))
        
#         if len(self.positions) > self.grow_to:
#             self.positions.pop()
    
#     def draw(self):
#         for i, (x, y) in enumerate(self.positions):
#             color = GREEN if i == 0 else DARK_GREEN  # Голова зеленее
#             rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
#             pygame.draw.rect(screen, color, rect)
#             pygame.draw.rect(screen, BLACK, rect, 1)  # Обводка
    
#     def change_direction(self, direction):
#         # Запрещаем движение в противоположном направлении
#         if (direction[0] * -1, direction[1] * -1) != self.direction:
#             self.direction = direction

# class Food:
#     def __init__(self):
#         self.position = (0, 0)
#         self.randomize_position()
    
#     def randomize_position(self):
#         self.position = (random.randint(0, GRID_WIDTH - 1), 
#                          random.randint(0, GRID_HEIGHT - 1))
    
#     def draw(self):
#         rect = pygame.Rect(self.position[0] * GRID_SIZE, 
#                           self.position[1] * GRID_SIZE, 
#                           GRID_SIZE, GRID_SIZE)
#         pygame.draw.rect(screen, RED, rect)
#         pygame.draw.rect(screen, BLACK, rect, 1)  # Обводка

# def draw_grid():
#     for x in range(0, WIDTH, GRID_SIZE):
#         pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
#     for y in range(0, HEIGHT, GRID_SIZE):
#         pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))

# def draw_score(score):
#     score_text = font.render(f'Счет: {score}', True, WHITE)
#     screen.blit(score_text, (10, 10))

# def draw_game_over(score):
#     overlay = pygame.Surface((WIDTH, HEIGHT))
#     overlay.set_alpha(180)
#     overlay.fill(BLACK)
#     screen.blit(overlay, (0, 0))
    
#     game_over_text = big_font.render('ИГРА ОКОНЧЕНА!', True, RED)
#     score_text = font.render(f'Ваш счет: {score}', True, WHITE)
#     restart_text = font.render('Нажмите R для новой игры', True, WHITE)
    
#     screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 60))
#     screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
#     screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 40))


# def main():
#     snake = Snake()
#     food = Food()
    
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.KEYDOWN:
#                 if not snake.alive and event.key == pygame.K_r:
#                     snake.reset()
#                     food.randomize_position()
#                 elif snake.alive:
#                     if event.key == pygame.K_UP:
#                         snake.change_direction((0, -1))
#                     elif event.key == pygame.K_DOWN:
#                         snake.change_direction((0, 1))
#                     elif event.key == pygame.K_LEFT:
#                         snake.change_direction((-1, 0))
#                     elif event.key == pygame.K_RIGHT:
#                         snake.change_direction((1, 0))
        
#         # Движение змейки
#         snake.move()
        
#         # Проверка на съедание еды
#         if snake.alive and snake.get_head_position() == food.position:
#             snake.grow_to += 1
#             snake.score += 10
#             food.randomize_position()
#             # Убедимся, что еда не появилась на змейке
#             while food.position in snake.positions:
#                 food.randomize_position()
        
#         # Отрисовка
#         screen.fill(BLACK)
#         draw_grid()
#         food.draw()
#         snake.draw()
#         draw_score(snake.score)
        
#         if not snake.alive:
#             draw_game_over(snake.score)
        
#         pygame.display.flip()
#         clock.tick(FPS)

# if __name__ == "__main__":
#     main()



#     #zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz


import telebot
from abc import ABC, abstractmethod

# Конфигурация 
TOKEN  = "8324683911:AAHtjZ888cjbihqWYPFxHYPBo9XVdLVscvk"
bot = telebot.TeleBot(TOKEN)


# Абстркный класс для задача
class AbstractTask(ABC):

    @abstractmethod
    def display(self) -> str:
        """Метод для отображение задачи"""
        pass


# Класс для простой задачи
class Task(AbstractTask):
    def init(self, description : str):
        self.description = description
        self.done = False           #по умолчанию задача не выполнено 
    
    def mark_done(self):
        self.done = True

    def display(self) -> str:
      status = "✅" if self.done else "❎"
      return f"{status} {self.description}"
    

# Менеджер для задач
class TaskManager:
    def init(self):
        self.tasks: list[Task] = []

    def add_task(self, description: str):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def mark_done(self, index: int):
         if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()


    def list_taks(self) -> str:
        if not self.tasks:
            return "Список задач пуст."
        return "\n".join([f"{i+1}.{task.display()}" for i, task in enumerate(self.tasks)])



# Класс для бота

class TaskBot:
    def init(self, bot_instance, manager: TaskManager):
        self.bot = bot_instance
        self.manager = manager
        self.register_handler()

    def register_handler(self):
        @self.bot.message_handler(commands = ["start"])

        def start(message):
                self.bot.send_message(message.chat.id,  "Привет! Я бот-менежер задач \n"
                                        "Команды: \n"
                                        "/add <задачи> - добавить задачу\n"
                                        "/list список задач\n "
                                        "/done <номер> - отметить как выполненное \n"
                                        "/remove <номер> - удалить задачу" )
                
    

        @self.bot.message_handler(commands = ["add"])
        def add(message):
            task_text = message.text.replace("/add", "").strip()
            if task_text:
                self.manager.add_task(task_text)
                self.bot.send_message(message.chat.id,"Задача добавлена ✅")
            else:
                self.bot.send_message(message.chat.id,"Напишите задачу после команды!")


        @self.bot.message_handler(commands = ["list"])
        def list_tasks(message):
            self.bot.send_message(message.chat.id, self.manager.list_taks())


        



    def run(self):
        self.bot.polling()



if names == "main":
    task_manager = TaskManager()
    task_bot = TaskBot(bot, task_manager)
    task_bot.run()
    