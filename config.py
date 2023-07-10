import os
from dataclasses import dataclass
import dotenv


@dataclass  # Позволяет не писать инициализатор
class TGBot:
    token: str


dotenv.load_dotenv()  # Загружаем в систему переменные
config = TGBot(token=os.getenv('BOT_TOKEN'))  # Считываем их
