from typing import Any
from datetime import datetime

def log_info(message: Any) -> None:
    time = datetime.now()
    print(f"[INFO - {time}] {message}")

log_info(10)
log_info("hello")
log_info("True")

