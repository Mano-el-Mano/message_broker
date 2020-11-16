import logging

class Logger:

    def __init__(self, name: str):
        self.logger = logging.getLogger(name)


@staticmethod
def configure(logname: str):
    logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)