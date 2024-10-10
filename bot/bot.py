from aiogram import Router, Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# К чему плодить классы, если я мог в файле main.py просто объявить объект Bot?
# Ответ: класс AntagonBot является обёрткой для класса Bot, можно будет расширить функционал класса Bot (что и было сделано
# например в методе init_routers()), а также более точно контролировать аспекты и собрать всё воедино, такие как роутеры, диспетчеры и т.д.
class AntagonBot:
    def __init__(self) -> None:
        self.token: str = input("Ожидание ввода токена\n$:")
        self.dispatcher: Dispatcher = Dispatcher()
        self.routers: list[Router]
        self.bot: Bot = Bot(token=self.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    def init_routers(self, *routers: Router) -> None:
        if (routers):
            self.dispatcher.include_routers(routers)
        else:
            routers = (Router())
            self.dispatcher.include_router(routers)

        self.routers = routers

antagon = AntagonBot()