# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.refund_response import RefundResponse

class TestRefundResponse(unittest.TestCase):
    """RefundResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RefundResponse:
        """Test RefundResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RefundResponse`
        """
        model = RefundResponse()
        if include_optional:
            return RefundResponse(
                payment_id = '',
                refunded_transactions = [
                    clientapi_barion.models.refunded_transaction.RefundedTransaction(
                        transaction_id = '', 
                        pos_transaction_id = '', 
                        total = 1.337, 
                        comment = '', 
                        status = '', )
                    ]
            )
        else:
            return RefundResponse(
        )
        """

    def testRefundResponse(self):
        """Test RefundResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
