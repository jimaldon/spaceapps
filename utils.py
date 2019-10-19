import logging


LOG_FORMAT = '%(asctime)-15s %(levelname)-5s %(name)-15s - %(message)s'


def setup_logging(log_path=None, log_level='DEBUG',
                  print_level='INFO', logger=None, fmt=LOG_FORMAT):
    """Prepare logging for the provided logger.
    Args:
        log_path (str, optional): full path to the desired log file
        debug (bool, optional): log in verbose mode or not
        logger (logging.Logger, optional): logger to setup logging upon,
            if it's None, root logger will be used
        fmt (str, optional): format for the logging message
    """
    logger = logger if logger else logging.getLogger()
    logger.setLevel(log_level)
    logger.handlers = []

    fmt = logging.Formatter(fmt=fmt)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fmt)
    stream_handler.setLevel(print_level)
    logger.addHandler(stream_handler)

    if log_path:
        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(fmt)
        logger.addHandler(file_handler)
        logger.info('Log file is %s', log_path)
