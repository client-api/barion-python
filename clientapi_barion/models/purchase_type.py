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


class PurchaseType(str, Enum):
    """
    PurchaseType
    """

    """
    allowed enum values
    """
    GOODSANDSERVICEPURCHASE = 'GoodsAndServicePurchase'
    CHECKACCEPTANCE = 'CheckAcceptance'
    ACCOUNTFUNDING = 'AccountFunding'
    QUASICASHTRANSACTION = 'QuasiCashTransaction'
    PREPAIDVACATIONANDLOAN = 'PrePaidVacationAndLoan'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PurchaseType from a JSON string"""
        return cls(json.loads(json_str))


