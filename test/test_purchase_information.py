# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.purchase_information import PurchaseInformation

class TestPurchaseInformation(unittest.TestCase):
    """PurchaseInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PurchaseInformation:
        """Test PurchaseInformation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PurchaseInformation`
        """
        model = PurchaseInformation()
        if include_optional:
            return PurchaseInformation(
                delivery_timeframe = 'ElectronicDelivery',
                delivery_email_address = '',
                pre_order_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                availability_indicator = 'MerchandiseAvailable',
                re_order_indicator = 'FirstTimeOrdered',
                shipping_address_indicator = 'ShipToCardholdersBillingAddress',
                recurring_expiry = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                recurring_frequency = 1,
                purchase_type = 'GoodsAndServicePurchase',
                gift_card_purchase = clientapi_barion.models.gift_card_purchase.GiftCardPurchase(
                    amount = 0, 
                    count = 1, ),
                purchase_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PurchaseInformation(
        )
        """

    def testPurchaseInformation(self):
        """Test PurchaseInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
