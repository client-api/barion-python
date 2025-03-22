# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class QRCodeSize(str, Enum):
    """
    QRCodeSize
    """

    """
    allowed enum values
    """
    SMALL = 'Small'
    NORMAL = 'Normal'
    LARGE = 'Large'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of QRCodeSize from a JSON string"""
        return cls(json.loads(json_str))


