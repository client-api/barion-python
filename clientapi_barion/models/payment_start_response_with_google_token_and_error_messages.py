# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from clientapi_barion.models.error import Error
from clientapi_barion.models.payment_status import PaymentStatus
from typing import Optional, Set
from typing_extensions import Self

class PaymentStartResponseWithGoogleTokenAndErrorMessages(BaseModel):
    """
    PaymentStartResponseWithGoogleTokenAndErrorMessages
    """ # noqa: E501
    payment_id: Optional[StrictStr] = Field(default=None, description="The identifier of the newly initialized payment, generated by the Barion system.", alias="PaymentId")
    payment_request_id: Optional[StrictStr] = Field(default=None, description="The payment identifier supplied by the API caller in the request.", alias="PaymentRequestId")
    payment_status: Optional[PaymentStatus] = Field(default=None, description="The status of the payment in the Barion system.", alias="PaymentStatus")
    three_ds_auth_client_data: Optional[StrictStr] = Field(default=None, description="Encrypted client authentication data required for 3D Secure processing. This value can be used when the webshop first tried to complete the payment without user interaction, but the charge failed due to a 3D Secure challenge being mandatory.", alias="ThreeDSAuthClientData")
    trace_id: Optional[StrictStr] = Field(default=None, description="A unique value generated by the card issuer to track a chain of [recurring or token payments that require 3D Secure authentication](https://docs.barion.com/Token_payment_3D_Secure). This shall be used in such scenarios, otherwise it can be ignored.", alias="TraceId")
    errors: Optional[List[Error]] = Field(default=None, alias="Errors")
    __properties: ClassVar[List[str]] = ["PaymentId", "PaymentRequestId", "PaymentStatus", "ThreeDSAuthClientData", "TraceId", "Errors"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PaymentStartResponseWithGoogleTokenAndErrorMessages from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['Errors'] = _items
        # set to None if payment_status (nullable) is None
        # and model_fields_set contains the field
        if self.payment_status is None and "payment_status" in self.model_fields_set:
            _dict['PaymentStatus'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentStartResponseWithGoogleTokenAndErrorMessages from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "PaymentId": obj.get("PaymentId"),
            "PaymentRequestId": obj.get("PaymentRequestId"),
            "PaymentStatus": obj.get("PaymentStatus"),
            "ThreeDSAuthClientData": obj.get("ThreeDSAuthClientData"),
            "TraceId": obj.get("TraceId"),
            "Errors": [Error.from_dict(_item) for _item in obj["Errors"]] if obj.get("Errors") is not None else None
        })
        return _obj


