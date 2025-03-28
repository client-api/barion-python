# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.accounts_response import AccountsResponse

class TestAccountsResponse(unittest.TestCase):
    """AccountsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountsResponse:
        """Test AccountsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountsResponse`
        """
        model = AccountsResponse()
        if include_optional:
            return AccountsResponse(
                accounts = [
                    clientapi_barion.models.account.Account(
                        account_id = '123e4567-e89b-12d3-a456-426614174000', 
                        balance = clientapi_barion.models.balance.Balance(
                            available = 100.5, 
                            blocked = 10.0, ), 
                        currency = '012', 
                        account_info = clientapi_barion.models.account_info.AccountInfo(
                            bban_country = 'HUN', 
                            bban = '', 
                            iban = '', 
                            reference = '', 
                            swift_code = '', 
                            beneficiary = clientapi_barion.models.beneficiary.Beneficiary(
                                name = 'Example Wallet - Barion', 
                                country = 'HUN', 
                                city = 'Budapest', 
                                zip = '1234', 
                                street = 'Example Street 12', ), ), )
                    ]
            )
        else:
            return AccountsResponse(
        )
        """

    def testAccountsResponse(self):
        """Test AccountsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
