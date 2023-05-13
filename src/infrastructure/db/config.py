from dataclasses import dataclass


@dataclass
class Config:
    host: str
    port: int
    user: str
    password: str
    database: str
    echo: bool = True

    @property
    def full_url(self) -> str:
        return "postgresql+asyncpg://{}:{}@{}:{}/{}".format(
            self.user, self.password, self.host, self.port, self.database,
        )
