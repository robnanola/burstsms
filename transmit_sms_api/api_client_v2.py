import base64
import requests
import json

class Error(Exception):
    pass


class TrasmitApiErrorError(Error):
    """

    AUTH_FAILED_NO_DATA 401     You have not provided auth data.
    AUTH_FAILED         401     The auth data you have provided is invalid.
    NOT_IMPLEMENTED     404     The method you are requesting is unsupported.
    OVER_LIMIT          429     You have exceeded the request limit.
    FIELD_EMPTY         400     Required field is empty.
    FIELD_INVALID       400     Field has invalid format (see proper format in the description).
    NO_ACCESS           400     You do not have access to this resource.
    KEY_EXISTS          400     The resource with this key already exists.
    NOT_FOUND           400     The resource with this key is not found.

    """

    def __init__(self, code, message):
        Error.__init__(self, message)
        self.code = code


class TransmitSmsApi(object):

    def __init__(self, api_key=None, api_secret=None):

        self.api_url = 'https://api.transmitsms.com/'
        self.version = 2

        self.api_key = api_key
        self.api_secret = api_secret


    def build_url_for(self, resource_name):
        """
        constructs to url with the given resource_name.
        """

        return '%s/%s.json' % (self.api_url, resource_name)


    def post(self, resource_name, data={}):
        """
        http post request to a given url and data.
        """
        url = self.build_url_for(resource_name)

        resp = requests.post(url, data, auth=(self.api_key, self.api_secret))

        return resp.json()


    def send_sms(self, data={}):

        """

        source: http://burst.transmitsms.com/api-docs/2/sms/send-sms

        @data keys:
            message - required
            to - required if list_id is not set
            from 
            send_at
            list_id - required if to is not set
            dir_callback
            reply_callback
            validity
            replies_to email


        """

        

        return self.post('send-sms', data)


    def get_sms(self, message_id):
        """
        Get information about a message you have sent.

        """

        self.post('get-sms', data={'message_id':message_id})



    def get_sms_responses(self, data={}):
        """
        Pick up responses to messages you have sent. Filter by keyword or 
        for just one phone number.

        http://burst.transmitsms.com/api-docs/2/sms/get-sms-responses



        """

        self.post('get-sms-responses', data=data)


    def get_sms_sent(self, data={}):
        """
        Get a list of recipients from a message send. 
        Get up to date information such as opt-out status and delivery status.

        http://burst.transmitsms.com/api-docs/2/sms/get-sms-sent
        """

        self.post('get-sms-sent', data=data)


    