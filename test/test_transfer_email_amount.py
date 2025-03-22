# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.transfer_email_amount import TransferEmailAmount

class TestTransferEmailAmount(unittest.TestCase):
    """TransferEmailAmount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransferEmailAmount:
        """Test TransferEmailAmount
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransferEmailAmount`
        """
        model = TransferEmailAmount()
        if include_optional:
            return TransferEmailAmount(
                currency = '012',
                value = 1.337
            )
        else:
            return TransferEmailAmount(
        )
        """

    def testTransferEmailAmount(self):
        """Test TransferEmailAmount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
