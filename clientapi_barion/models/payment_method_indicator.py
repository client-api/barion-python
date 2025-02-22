# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PaymentMethodIndicator(str, Enum):
    """
    PaymentMethodIndicator
    """

    """
    allowed enum values
    """
    NOACCOUNT = 'NoAccount'
    THISTRANSACTION = 'ThisTransaction'
    LESSTHAN30DAYS = 'LessThan30Days'
    BETWEEN30AND60DAYS = 'Between30And60Days'
    MORETHAN60DAYS = 'MoreThan60Days'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PaymentMethodIndicator from a JSON string"""
        return cls(json.loads(json_str))


