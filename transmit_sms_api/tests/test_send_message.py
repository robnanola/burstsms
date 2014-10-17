import unittest
import unittest
import json
import sys

from api_client_v2 import TransmitSmsApi


class TestSendSms(unittest.TestCase):

	def setUp(self):

		self.api = TransmitSmsApi('dcae6d3a62e8a88da9dd442fb1f08082','secretdaw')


	def test_send_sms_failed1(self):

		data = {
			'message':None
			'to':
		}

		self.api.send_sms()
