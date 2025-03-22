# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.payment_complete_response_with_error_messages import PaymentCompleteResponseWithErrorMessages

class TestPaymentCompleteResponseWithErrorMessages(unittest.TestCase):
    """PaymentCompleteResponseWithErrorMessages unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentCompleteResponseWithErrorMessages:
        """Test PaymentCompleteResponseWithErrorMessages
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentCompleteResponseWithErrorMessages`
        """
        model = PaymentCompleteResponseWithErrorMessages()
        if include_optional:
            return PaymentCompleteResponseWithErrorMessages(
                payment_id = '123e4567-e89b-12d3-a456-426614174001',
                payment_request_id = 'PAYMENT123',
                payment_status = '',
                is_successful = True,
                trace_id = 'TRACE123',
                errors = [
                    clientapi_barion.models.error.Error(
                        error_code = '', 
                        title = '', 
                        description = '', 
                        end_point = '', 
                        auth_data = '', 
                        happened_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        payment_id = '', )
                    ]
            )
        else:
            return PaymentCompleteResponseWithErrorMessages(
        )
        """

    def testPaymentCompleteResponseWithErrorMessages(self):
        """Test PaymentCompleteResponseWithErrorMessages"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
