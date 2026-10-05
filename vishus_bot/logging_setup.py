"""Logger setup for VISHU'S BOT."""

import logging
import sys

def get_logger(name: str = "vishus_bot") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("[VISHU'S BOT] %(asctime)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
