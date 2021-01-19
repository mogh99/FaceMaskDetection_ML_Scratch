import requests

class BotHandler:
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    # Get the file_path to download the file (image) in load_image
    def get_file_path(self, file_id):
        params = {"file_id": file_id}
        method = "getFile"
        resp = requests.get(self.api_url + method, params)
        file_path = resp.json()["result"]["file_path"]
        return file_path

    def load_image(self, file_path):
        url = f"https://api.telegram.org/file/bot{self.token}/{file_path}"
        resp = requests.get(url)
        return resp.content
