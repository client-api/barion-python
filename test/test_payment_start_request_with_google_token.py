# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.payment_start_request_with_google_token import PaymentStartRequestWithGoogleToken

class TestPaymentStartRequestWithGoogleToken(unittest.TestCase):
    """PaymentStartRequestWithGoogleToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentStartRequestWithGoogleToken:
        """Test PaymentStartRequestWithGoogleToken
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentStartRequestWithGoogleToken`
        """
        model = PaymentStartRequestWithGoogleToken()
        if include_optional:
            return PaymentStartRequestWithGoogleToken(
                payer_email_address = '',
                google_pay_token = '',
                payment_type = 'Immediate',
                reservation_period = '48.07:28:88',
                delayed_capture_period = '48.07:28:88',
                payment_window = '48.07:28:88',
                guest_check_out = True,
                initiate_recurrence = True,
                recurrence_id = '',
                funding_sources = [
                    'All'
                    ],
                payment_request_id = '',
                payer_hint = '',
                card_holder_name_hint = '01',
                recurrence_type = 'OneClickPayment',
                trace_id = '',
                redirect_url = '',
                callback_url = '',
                transactions = [
                    clientapi_barion.models.payment_transaction.PaymentTransaction(
                        pos_transaction_id = '', 
                        payee = '', 
                        total = 1.337, 
                        comment = '', 
                        payee_transactions = [
                            clientapi_barion.models.payee_transaction.PayeeTransaction(
                                pos_transaction_id = '1234567890', 
                                payee = 'recipient@example.com', 
                                total = 100.0, 
                                comment = 'Comment of the transaction. This is shown to the recipient.', )
                            ], 
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
                            ], )
                    ],
                order_number = '',
                shipping_address = clientapi_barion.models.shipping_address.ShippingAddress(
                    country = 'HU', 
                    city = '', 
                    region = '', 
                    zip = '', 
                    street = '', 
                    street2 = '', 
                    street3 = '', 
                    full_name = '', ),
                locale = 'hu-HU',
                currency = 'HUF',
                payer_phone_number = '4',
                payer_work_phone_number = '4',
                payer_home_number = '4',
                billing_address = clientapi_barion.models.billing_address.BillingAddress(
                    country = 'HU', 
                    city = '', 
                    region = 'AE', 
                    zip = '', 
                    street = '', 
                    street2 = '', 
                    street3 = '', ),
                payer_account_information = clientapi_barion.models.payer_account_information.PayerAccountInformation(
                    account_id = '', 
                    account_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    account_creation_indicator = 'NoAccount', 
                    account_last_changed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    account_change_indicator = 'ChangedDuringThisTransaction', 
                    password_last_changed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    password_change_indicator = 'NoChange', 
                    purchases_in_the_last6_months = 0, 
                    shipping_address_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    shipping_address_usage_indicator = 'ThisTransaction', 
                    provision_attempts = 0, 
                    transactional_activity_per_day = 0, 
                    transactional_activity_per_year = 0, 
                    payment_method_added = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    payment_method_indicator = 'NoAccount', 
                    suspicious_activity_indicator = 'NoSuspiciousActivityObserved', ),
                purchase_information = clientapi_barion.models.purchase_information.PurchaseInformation(
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
                    purchase_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ),
                challenge_preference = 'NoPreference'
            )
        else:
            return PaymentStartRequestWithGoogleToken(
                payer_email_address = '',
                google_pay_token = '',
                payment_type = 'Immediate',
                guest_check_out = True,
                funding_sources = [
                    'All'
                    ],
                payment_request_id = '',
                redirect_url = '',
                transactions = [
                    clientapi_barion.models.payment_transaction.PaymentTransaction(
                        pos_transaction_id = '', 
                        payee = '', 
                        total = 1.337, 
                        comment = '', 
                        payee_transactions = [
                            clientapi_barion.models.payee_transaction.PayeeTransaction(
                                pos_transaction_id = '1234567890', 
                                payee = 'recipient@example.com', 
                                total = 100.0, 
                                comment = 'Comment of the transaction. This is shown to the recipient.', )
                            ], 
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
                            ], )
                    ],
                locale = 'hu-HU',
                currency = 'HUF',
        )
        """

    def testPaymentStartRequestWithGoogleToken(self):
        """Test PaymentStartRequestWithGoogleToken"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
