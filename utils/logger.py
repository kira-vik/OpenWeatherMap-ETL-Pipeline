import logging
from logging.handlers import RotatingFileHandler


def setup_logger():
    log_file = "weather_data_etl.log"
    max_log_size = 5 * 1024 * 1024  # 5 MB
    backup_count = 5

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            RotatingFileHandler(
                log_file, maxBytes=max_log_size, backupCount=backup_count
            ),
            logging.StreamHandler(),
        ],
    )
    return logging.getLogger(__name__)


# TODO: Create directory for logs and update code to use that directory
