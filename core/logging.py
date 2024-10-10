import os
import loguru

class BotLogger:
    def __init__(self) -> None:
        self.logs_dir: str = os.path.abspath(__file__).rsplit(r'core\logging.py', 1)[0]

        self.info_log: int = self.init_logger("INFO", "1 week")
        self.warn_log: int = self.init_logger("WARN", "1 month")
        self.error_log: int = self.init_logger("ERROR", "1 month")

    def init_logger(self, level: str, rotation) -> None:
        print(f"Logger: inited {level} level")

        return loguru.logger.add(
            f"{self.logs_dir}/{level.lower()}.log",
            format="{level} {time} {message}",
            enqueue=True,
            level=level,
            rotation=rotation
        )
