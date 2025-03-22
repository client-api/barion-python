# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.beneficiary import Beneficiary

class TestBeneficiary(unittest.TestCase):
    """Beneficiary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Beneficiary:
        """Test Beneficiary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Beneficiary`
        """
        model = Beneficiary()
        if include_optional:
            return Beneficiary(
                name = 'Example Wallet - Barion',
                country = 'HUN',
                city = 'Budapest',
                zip = '1234',
                street = 'Example Street 12'
            )
        else:
            return Beneficiary(
        )
        """

    def testBeneficiary(self):
        """Test Beneficiary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
