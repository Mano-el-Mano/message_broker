import logging


class CallbackHandler:

    def __init__(self, keys: list, log_config: dict):
        self.keys = keys
        logging.basicConfig(
            filename=log_config['filename'],
            filemode='a',
            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
            datefmt='%H:%M:%S',
            level=logging.INFO)
        self.__cache = list()

    @property
    def cache(self):
        return self.__cache

    @cache.setter
    def cache(self, value):
        self.cache.append(value)


    def handle(self, key: str, body: dict):
        print(f' {key}key')
        if key not in self.keys:
            return False

        if key == 'loans':
            self.handle_loans(body),
        elif key =='autumn_offers':
            self.handle_autumn_offers(body)


    @staticmethod
    def handle_autumn_offers(body: dict):
        answer = input(f"""
        {body} \n
        want to save discount?
        """)
        print(answer)
        if answer == 'yes' or answer == 'y':
            print("you have purchased this")
            logging.info(f"user has purchased {body}")
            return
        elif answer == 'n' or answer == 'no':
            print(" we will give you a better offer")
            return

    def handle_loans(self, body: dict):
        print(f"""
                saved loans:
                {self.cache}
                """)
        answer = input(f"""
        {body} \n
        want to save loan?
        """)
        print(answer)

        if (answer == 'yes' or answer == 'y') and body['id'] not in list(map(lambda elem: elem.id, self.cache)):
            self.cache.append(body)
            logging.info(f"user has purchased {body}")
            return
        elif answer == 'n' or answer == 'no':
            print(" we will give you a better offer")
            return
