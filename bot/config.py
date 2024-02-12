from pydantic import SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    ADMINS: list[int]
    DB_NAME: str
    TEST_GROUP_ID: int
    PROD_GROUP_ID: int
    db_echo: bool = True

    @property
    def aiosqlite_db_url(self) -> str:
        return f"sqlite+aiosqlite:///{self.DB_NAME}.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
