import unittest
import unittest
import json
import sys

from api_client_v2 import TransmitSmsApi


class TestSendSmsInvalidAuth(unittest.TestCase):

    def setUp(self):

        self.api = TransmitSmsApi('dcae6d3a62e8a88da9dd442fb1f08082','secretdaw1')


    def test_send_sms_failed1(self):

        data = {
            'message':'test message',
            'to':'6123456789',
        }

        resp = self.api.send_sms(data)

        self.assertEqual(resp['error']['code'], u'AUTH_FAILED')


class TestSendSms(unittest.TestCase):

    def setUp(self):

        self.api = TransmitSmsApi('dcae6d3a62e8a88da9dd442fb1f08082','secretdaw')


    def test_send_sms_failed1(self):

        data = {
            'message':None,
            'to':'',
        }

        resp = self.api.send_sms(data)

        self.assertEqual(resp['error']['code'], 'FIELD_EMPTY')


    def test_send_sms_failed1(self):

        data = {
            'message':"test message",
            'to':'',
        }

        resp = self.api.send_sms(data)

        self.assertEqual(resp['error']['code'], 'FIELD_INVALID')
        self.assertEqual(resp['error']['description'],u"You must provide either 'list_id' or 'to'" )


    def test_send_sms_failed1(self):

        data = {
            'message':"",
            'to':'1234456',
        }

        resp = self.api.send_sms(data)

        self.assertEqual(resp['error']['code'], 'FIELD_EMPTY')
        self.assertEqual(resp['error']['description'],u"Required field 'message' is empty" )



    def test_send_sms_failed1(self):

        data = {
            'message':"test message 2",
            'to':'1234456',
        }

        resp = self.api.send_sms(data)

        self.assertEqual(resp['error']['code'], 'FIELD_INVALID')
        self.assertEqual(resp['error']['description'],u'Field "to" is not a valid number.' )

    def test_send_sms_valid(self):

        data = {
            'message':"test message valid",
            'to':'61422265404',
        }        


        resp = self.api.send_sms(data)

        self.assertEqual(resp['error']['code'], 'SUCCESS')
        self.assertEqual(resp['error']['description'],u'OK' )

