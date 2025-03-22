# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.payee_transaction_to_finish import PayeeTransactionToFinish

class TestPayeeTransactionToFinish(unittest.TestCase):
    """PayeeTransactionToFinish unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PayeeTransactionToFinish:
        """Test PayeeTransactionToFinish
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PayeeTransactionToFinish`
        """
        model = PayeeTransactionToFinish()
        if include_optional:
            return PayeeTransactionToFinish(
                transaction_id = '123e4567-e89b-12d3-a456-426614174003',
                total = 50.0,
                comment = 'Refund for returned item'
            )
        else:
            return PayeeTransactionToFinish(
                transaction_id = '123e4567-e89b-12d3-a456-426614174003',
                total = 50.0,
        )
        """

    def testPayeeTransactionToFinish(self):
        """Test PayeeTransactionToFinish"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
