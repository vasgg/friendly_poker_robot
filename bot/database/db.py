from bot.config import settings
from bot.database.database_connector import DatabaseConnector

db = DatabaseConnector(url=settings.aiosqlite_db_url, echo=settings.db_echo)
