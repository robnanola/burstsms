import re
from copy import copy
import urllib2
import urllib
import base64
import json
import requests

from django import forms
from django.conf import settings

from localflavor.au.forms import AUPhoneNumberField
import bitly_api
from transmit_sms_api.api_client_v2 import TransmitSmsApi

class SendSMSForm(forms.Form):
    mobile_number = AUPhoneNumberField()
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        data = self.parse_message(self.cleaned_data['message'])
        return data


    def send_sms_message(self):

        trans_api = TransmitSmsApi(settings.BURST_API_KEY, settings.BURST_API_SECRET+'1')
        trans_api.send_sms(self.cleaned_data)

        return trans_api.send_sms(self.cleaned_data)


    def parse_message(self, message):

        bitly_obj = bitly_api.Connection(settings.BITLY_API_USER, settings.BITLY_API_KEY)

        parsed_urls = re.findall(r'(https?://[^\s]+)', message)

        shortend_urls = [bitly_obj.shorten(url)['url'] for url in parsed_urls]

        url_mapping = zip(parsed_urls,shortend_urls)

        for k, v in url_mapping:
            message = message.replace(k,v)

        return message




