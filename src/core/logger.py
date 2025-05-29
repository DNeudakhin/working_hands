import logging

logging.basicConfig(
    level=logging.INFO,  # минимальный уровень логирования
    format='%(asctime)s (%(name)s): %(message)s',
    handlers=[logging.StreamHandler()]  # вывод в консоль
)

def get_logger(name):
    return logging.getLogger(name)