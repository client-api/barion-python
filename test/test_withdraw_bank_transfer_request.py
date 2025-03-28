# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.withdraw_bank_transfer_request import WithdrawBankTransferRequest

class TestWithdrawBankTransferRequest(unittest.TestCase):
    """WithdrawBankTransferRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WithdrawBankTransferRequest:
        """Test WithdrawBankTransferRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WithdrawBankTransferRequest`
        """
        model = WithdrawBankTransferRequest()
        if include_optional:
            return WithdrawBankTransferRequest(
                currency = '012',
                amount = 0,
                comment = '',
                bank_account = clientapi_barion.models.bank_account_details.BankAccountDetails(
                    country = '012', 
                    format = '', 
                    account_number = '', ),
                bank = clientapi_barion.models.bank_details.BankDetails(
                    swift_code = '01234567', ),
                recipient = clientapi_barion.models.recipient_details.RecipientDetails(
                    name = '', 
                    address = clientapi_barion.models.recipient_address.RecipientAddress(
                        country = '012', 
                        street = '', 
                        city = '', 
                        zip = '', ), )
            )
        else:
            return WithdrawBankTransferRequest(
                currency = '012',
                amount = 0,
                bank_account = clientapi_barion.models.bank_account_details.BankAccountDetails(
                    country = '012', 
                    format = '', 
                    account_number = '', ),
                bank = clientapi_barion.models.bank_details.BankDetails(
                    swift_code = '01234567', ),
                recipient = clientapi_barion.models.recipient_details.RecipientDetails(
                    name = '', 
                    address = clientapi_barion.models.recipient_address.RecipientAddress(
                        country = '012', 
                        street = '', 
                        city = '', 
                        zip = '', ), ),
        )
        """

    def testWithdrawBankTransferRequest(self):
        """Test WithdrawBankTransferRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
