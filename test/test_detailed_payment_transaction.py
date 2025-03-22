# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.detailed_payment_transaction import DetailedPaymentTransaction

class TestDetailedPaymentTransaction(unittest.TestCase):
    """DetailedPaymentTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DetailedPaymentTransaction:
        """Test DetailedPaymentTransaction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DetailedPaymentTransaction`
        """
        model = DetailedPaymentTransaction()
        if include_optional:
            return DetailedPaymentTransaction(
                transaction_id = '',
                pos_transaction_id = '',
                transaction_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                total = 1.337,
                currency = '012',
                payer = clientapi_barion.models.user_information.UserInformation(
                    name = clientapi_barion.models.name_information.NameInformation(
                        login_name = '', 
                        first_name = '', 
                        last_name = '', 
                        organization_name = '', ), 
                    email = '', ),
                payee = clientapi_barion.models.user_information.UserInformation(
                    name = clientapi_barion.models.name_information.NameInformation(
                        login_name = '', 
                        first_name = '', 
                        last_name = '', 
                        organization_name = '', ), 
                    email = '', ),
                comment = '',
                status = '',
                transaction_type = None,
                items = [
                    clientapi_barion.models.item.Item(
                        name = '', 
                        description = '', 
                        image_url = '', 
                        quantity = 0, 
                        unit = '', 
                        unit_price = 1.337, 
                        item_total = 1.337, 
                        sku = '', )
                    ],
                related_id = ''
            )
        else:
            return DetailedPaymentTransaction(
        )
        """

    def testDetailedPaymentTransaction(self):
        """Test DetailedPaymentTransaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
