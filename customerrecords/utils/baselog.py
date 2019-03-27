from utils.generallogger import GeneralLogger


class BaseLog():
    def __init__(self):
        self.logger = GeneralLogger.__call__().get_logger()
