import telebot
from abc import ABC, abstractmethod
import json
import os


# Конфигурация 
TOKEN  = "8217951972:AAEMFf-UsMEdvrQohlNlmTYYzPgvfD8nro4"
bot = telebot.TeleBot(TOKEN)
DATA_FILE = "tasks.json"



# === Абстрактный класс задачи ===
class AbstractTask(ABC):
    @abstractmethod
    def display(self) -> str:
        """Метод для отображения задачи"""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Метод для сохранения задачи в словарь"""
        pass

# === Класс простой задачи ===
class Task(AbstractTask):
    def init(self, description: str, done: bool = False):
        self.description = description
        self.done = done

    def mark_done(self):
        self.done = True

    def display(self) -> str:
        status = "✅" if self.done else "❌"
        return f"{status} {self.description}"

    def to_dict(self) -> dict:
        return {"description": self.description, "done": self.done}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(description=data["description"], done=data["done"])

# === Менеджер задач ===
class TaskManager:
    def init(self):
        self.tasks: list[Task] = []
        self.load_tasks()

    def add_task(self, description: str):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save_tasks()

    def mark_done(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            self.save_tasks()

    def list_tasks(self) -> str:
        if not self.tasks:
            return "Список задач пуст."
        return "\n".join([f"{i+1}. {task.display()}" for i, task in enumerate(self.tasks)])

    def save_tasks(self):
        data = [task.to_dict() for task in self.tasks]
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]

# === Класс бота ===
class TaskBot:
    def init(self, bot_instance, manager: TaskManager):
        self.bot = bot_instance
        self.manager = manager
        self.register_handlers()

    def register_handlers(self):
        @self.bot.message_handler(commands=["start"])
        def start(message):
            self.bot.send_message(
                message.chat.id,
                "Привет! Я бот-менеджер задач \n"
                "Команды:\n"
                "/add <задача> - добавить задачу\n"
                "/list - список задач\n"
                "/done <номер> - отметить как выполненную\n"
                "/remove <номер> - удалить задачу"
            )

        @self.bot.message_handler(commands=["add"])
        def add(message):
            task_text = message.text.replace("/add", "").strip()
            if task_text:
                self.manager.add_task(task_text)
                self.bot.send_message(message.chat.id, "Задача добавлена ✅")
            else:
                self.bot.send_message(message.chat.id, "Напишите задачу после команды!")

        @self.bot.message_handler(commands=["list"])
        def list_tasks(message):
            self.bot.send_message(message.chat.id, self.manager.list_tasks())

        @self.bot.message_handler(commands=["done"])
        def done(message):
            try:
                index = int(message.text.split()[1]) - 1
                self.manager.mark_done(index)
                self.bot.send_message(message.chat.id, "Задача отмечена как выполненная ✅")
            except:
                self.bot.send_message(message.chat.id, "Используйте: /done <номер>")

                print("Bot zapushen")
bot.polling(none_stop=True)