import base64
import request

class Error(Exception):
    pass


class TrasmitApiErrorError(Error):
    def __init__(self, code, message):
        Error.__init__(self, message)
        self.code = code


class TransmitSmsApi(obj):

    def __init__(self, api_key=None, api_secret=None):

        self.api_url = 'https://api.transmitsms.com/'
        self.version = 2

        self.api_key = api_key
        self.api_secret = api_secret


    def build_url_for(self, resource_name):

        return '%s/%s.json' % (self.api_url, resource_name)


    def post(self, url, data={}):

        resp = request.post(url, data, auth=(self.api_key, self.api_secret))

        resp_dict = json.loads(resp.json())

        print resp_dict


    def send_sms(self, data={}):

        url = self.build_url_for('send-sms')

        self.post(url, data)





