# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.payee_transaction import PayeeTransaction

class TestPayeeTransaction(unittest.TestCase):
    """PayeeTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayeeTransaction:
        """Test PayeeTransaction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayeeTransaction`
        """
        model = PayeeTransaction()
        if include_optional:
            return PayeeTransaction(
                pos_transaction_id = '1234567890',
                payee = 'recipient@example.com',
                total = 100.0,
                comment = 'Comment of the transaction. This is shown to the recipient.'
            )
        else:
            return PayeeTransaction(
                pos_transaction_id = '1234567890',
                payee = 'recipient@example.com',
                total = 100.0,
        )
        """

    def testPayeeTransaction(self):
        """Test PayeeTransaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
