# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_barion.models.errors import Errors

class TestErrors(unittest.TestCase):
    """Errors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Errors:
        """Test Errors
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Errors`
        """
        model = Errors()
        if include_optional:
            return Errors(
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
            return Errors(
        )
        """

    def testErrors(self):
        """Test Errors"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
