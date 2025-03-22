# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.refund_request import RefundRequest

class TestRefundRequest(unittest.TestCase):
    """RefundRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RefundRequest:
        """Test RefundRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RefundRequest`
        """
        model = RefundRequest()
        if include_optional:
            return RefundRequest(
                payment_id = '',
                transactions_to_refund = [
                    clientapi_barion.models.transaction_to_refund.TransactionToRefund(
                        transaction_id = '', 
                        pos_transaction_id = '', 
                        amount_to_refund = 0.01, 
                        comment = '', )
                    ]
            )
        else:
            return RefundRequest(
                payment_id = '',
                transactions_to_refund = [
                    clientapi_barion.models.transaction_to_refund.TransactionToRefund(
                        transaction_id = '', 
                        pos_transaction_id = '', 
                        amount_to_refund = 0.01, 
                        comment = '', )
                    ],
        )
        """

    def testRefundRequest(self):
        """Test RefundRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
