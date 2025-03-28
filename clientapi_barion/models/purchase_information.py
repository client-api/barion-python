# coding: utf-8

"""
    Barion API

    Integrate with ease and get unbeatable fees and data that helps you grow your business.

    The version of the OpenAPI document: 0.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from clientapi_barion.models.gift_card_purchase import GiftCardPurchase
from clientapi_barion.models.purchase_type import PurchaseType
from typing import Optional, Set
from typing_extensions import Self

class PurchaseInformation(BaseModel):
    """
    PurchaseInformation
    """ # noqa: E501
    delivery_timeframe: Optional[StrictStr] = Field(default=None, description="Enumeration indicating the length of the delivery period.", alias="DeliveryTimeframe")
    delivery_email_address: Optional[StrictStr] = Field(default=None, description="If goods are sent electronically, the payer's email address where goods should be delivered.", alias="DeliveryEmailAddress")
    pre_order_date: Optional[datetime] = Field(default=None, description="The date when pre-ordered goods will be available, in UTC.", alias="PreOrderDate")
    availability_indicator: Optional[StrictStr] = Field(default=None, description="Enumeration indicating when the goods will be available.", alias="AvailabilityIndicator")
    re_order_indicator: Optional[StrictStr] = Field(default=None, description="Enumeration indicating if the purchase is a re-order.", alias="ReOrderIndicator")
    shipping_address_indicator: Optional[StrictStr] = Field(default=None, description="Enumeration indicating what kind of shipping is used.", alias="ShippingAddressIndicator")
    recurring_expiry: Optional[datetime] = Field(default=None, description="`Required` in case of initial `Recurring` payment. The date past which no further payments should be accepted in the recurrence cycle, required for initial Recurring payments, in UTC.", alias="RecurringExpiry")
    recurring_frequency: Optional[Annotated[int, Field(le=9999, strict=True, ge=1)]] = Field(default=None, description="`Required` in case of initial `Recurring` payment. Minimum number of days between subsequent payments for initial Recurring payments.", alias="RecurringFrequency")
    purchase_type: Optional[PurchaseType] = Field(default=None, description="The type of purchase.", alias="PurchaseType")
    gift_card_purchase: Optional[GiftCardPurchase] = Field(default=None, description="Information about purchased gift cards.", alias="GiftCardPurchase")
    purchase_date: Optional[datetime] = Field(default=None, description="The date and time of the purchase, in UTC.", alias="PurchaseDate")
    __properties: ClassVar[List[str]] = ["DeliveryTimeframe", "DeliveryEmailAddress", "PreOrderDate", "AvailabilityIndicator", "ReOrderIndicator", "ShippingAddressIndicator", "RecurringExpiry", "RecurringFrequency", "PurchaseType", "GiftCardPurchase", "PurchaseDate"]

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
        """Create an instance of PurchaseInformation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of gift_card_purchase
        if self.gift_card_purchase:
            _dict['GiftCardPurchase'] = self.gift_card_purchase.to_dict()
        # set to None if purchase_type (nullable) is None
        # and model_fields_set contains the field
        if self.purchase_type is None and "purchase_type" in self.model_fields_set:
            _dict['PurchaseType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PurchaseInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "DeliveryTimeframe": obj.get("DeliveryTimeframe"),
            "DeliveryEmailAddress": obj.get("DeliveryEmailAddress"),
            "PreOrderDate": obj.get("PreOrderDate"),
            "AvailabilityIndicator": obj.get("AvailabilityIndicator"),
            "ReOrderIndicator": obj.get("ReOrderIndicator"),
            "ShippingAddressIndicator": obj.get("ShippingAddressIndicator"),
            "RecurringExpiry": obj.get("RecurringExpiry"),
            "RecurringFrequency": obj.get("RecurringFrequency"),
            "PurchaseType": obj.get("PurchaseType"),
            "GiftCardPurchase": GiftCardPurchase.from_dict(obj["GiftCardPurchase"]) if obj.get("GiftCardPurchase") is not None else None,
            "PurchaseDate": obj.get("PurchaseDate")
        })
        return _obj


