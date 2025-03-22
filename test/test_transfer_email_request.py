# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.transfer_email_request import TransferEmailRequest

class TestTransferEmailRequest(unittest.TestCase):
    """TransferEmailRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransferEmailRequest:
        """Test TransferEmailRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransferEmailRequest`
        """
        model = TransferEmailRequest()
        if include_optional:
            return TransferEmailRequest(
                source_account_id = '',
                amount = clientapi_barion.models.transfer_email_amount.TransferEmailAmount(
                    currency = '012', 
                    value = 1.337, ),
                target_email = '',
                comment = ''
            )
        else:
            return TransferEmailRequest(
                source_account_id = '',
                amount = clientapi_barion.models.transfer_email_amount.TransferEmailAmount(
                    currency = '012', 
                    value = 1.337, ),
                target_email = '',
                comment = '',
        )
        """

    def testTransferEmailRequest(self):
        """Test TransferEmailRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
