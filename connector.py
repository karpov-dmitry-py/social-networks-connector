import logging

import requests

USER_ID = '33275712'


class VkConnector:
    ACCESS_KEY = 'ed770aaced770aaced770aac58ed05f4c1eed77ed770aacb27ecb1e54bfb59ba227936d'
    # ACCESS_KEY = '8mGcAcVnSbdfLhrIMZTl'
    API_URL = 'https://api.vk.com/method/'
    API_VERSION = '5.120'

    def __init__(self, user_id=''):
        self.user_id = user_id if user_id else USER_ID
        self._set_logger()
        self.payload = self._get_payload()

    def _set_logger(self):
        self.logger = logging.getLogger('vk_connector')
        self.logger.setLevel(logging.DEBUG)
        logger_handler = logging.StreamHandler()
        logger_handler.setLevel(logging.DEBUG)
        logger_formatter = logging.Formatter('%(name)s - %(message)s')
        logger_handler.setFormatter(logger_formatter)
        self.logger.addHandler(logger_handler)

    def _get_payload(self):
        result = {
            'v': self.API_VERSION,
            'access_token': self.ACCESS_KEY,
        }
        return result

    def _set_url(self):
        self.url = f'{self.API_URL}{self.method_name}'

    def _get_request_result(self, user_param_title='user_id'):
        self.payload = self._get_payload()
        self.payload[user_param_title] = self.user_id
        response = requests.get(url=self.url, params=self.payload)
        result = response.json()
        for key, value in result.items():
            self.logger.info(f'{key}: {value}\n')
        return result

    def get_user_info(self):
        self.method_name = 'users.get'
        self._set_url()
        result = self._get_request_result()
        return result

    def get_friends(self):
        self.method_name = 'friends.get'
        self._set_url()
        result = self._get_request_result()
        return result

    def get_wall(self):
        self.method_name = 'wall.get'
        self._set_url()
        result = self._get_request_result(user_param_title='owner_id')
        return result


def main():
    connector = VkConnector()
    connector.get_user_info()
    connector.get_wall()
    connector.get_friends()


if __name__ == '__main__':
    main()
