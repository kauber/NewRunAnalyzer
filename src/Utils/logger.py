"""
logger caller
"""

import logging
import sys
from datetime import datetime
import os


def get_the_logger(log_name: str, logs_path: str, run_date: datetime) -> logging.Logger:
    """

    :param log_name:
    :param logs_path:
    :param run_date:
    :return:
    """

    today = run_date.strftime("%Y-%m-%d")
    # dir_date = os.path.join(logs_path, today)
    # dir_date_name = os.path.join(dir_date, log_name)

    if not os.path.exists(logs_path):
        os.mkdir(logs_path)

    # if not os.path.exists(dir_date):
    #     os.mkdir(dir_date)

    logging.basicConfig(
        format=f"%(levelname)s\t{today}\t%(asctime)s\t%(name)s"
        f"\t%(module)s\t%(funcName)s\t(lineno)d\t%(message)s",
        datefmt="%H:%M:%S",
        level=logging.INFO,
        stream=sys.stdout,
    )

    proj_logger = logging.getLogger(log_name)
    return proj_logger


if __name__ == "__main__":
    pass
