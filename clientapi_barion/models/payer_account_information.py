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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from clientapi_barion.models.account_change_indicator import AccountChangeIndicator
from clientapi_barion.models.account_creation_indicator import AccountCreationIndicator
from clientapi_barion.models.password_change_indicator import PasswordChangeIndicator
from clientapi_barion.models.payment_method_indicator import PaymentMethodIndicator
from clientapi_barion.models.shipping_address_usage_indicator import ShippingAddressUsageIndicator
from clientapi_barion.models.suspicious_activity_indicator import SuspiciousActivityIndicator
from typing import Optional, Set
from typing_extensions import Self

class PayerAccountInformation(BaseModel):
    """
    PayerAccountInformation
    """ # noqa: E501
    account_id: Optional[Annotated[str, Field(strict=True, max_length=64)]] = Field(default=None, description="A unique ID of the payer's account in the merchant's system.", alias="AccountId")
    account_created: Optional[datetime] = Field(default=None, description="The timestamp when the payer created its account in UTC.", alias="AccountCreated")
    account_creation_indicator: Optional[AccountCreationIndicator] = Field(default=None, alias="AccountCreationIndicator")
    account_last_changed: Optional[datetime] = Field(default=None, description="The timestamp when the payer last changed its account in UTC.", alias="AccountLastChanged")
    account_change_indicator: Optional[AccountChangeIndicator] = Field(default=None, alias="AccountChangeIndicator")
    password_last_changed: Optional[datetime] = Field(default=None, description="The timestamp when the payer last changed its password in UTC.", alias="PasswordLastChanged")
    password_change_indicator: Optional[PasswordChangeIndicator] = Field(default=None, alias="PasswordChangeIndicator")
    purchases_in_the_last6_months: Optional[Annotated[int, Field(le=9999, strict=True, ge=0)]] = Field(default=None, description="The number of successful purchases of the payer in the last 6 months.", alias="PurchasesInTheLast6Months")
    shipping_address_added: Optional[datetime] = Field(default=None, description="The timestamp when the shipping address used for this payment was added to the payer's account in UTC.", alias="ShippingAddressAdded")
    shipping_address_usage_indicator: Optional[ShippingAddressUsageIndicator] = Field(default=None, alias="ShippingAddressUsageIndicator")
    provision_attempts: Optional[Annotated[int, Field(le=999, strict=True, ge=0)]] = Field(default=None, description="How many times the customer tried to add a card to its account during the last 24 hours.", alias="ProvisionAttempts")
    transactional_activity_per_day: Optional[Annotated[int, Field(le=999, strict=True, ge=0)]] = Field(default=None, description="The number of purchases attached to this payer in the last 24 hours.", alias="TransactionalActivityPerDay")
    transactional_activity_per_year: Optional[Annotated[int, Field(le=999, strict=True, ge=0)]] = Field(default=None, description="The number of purchases attached to this payer in the last 365 days.", alias="TransactionalActivityPerYear")
    payment_method_added: Optional[datetime] = Field(default=None, description="When this card was added to the payer's account in UTC.", alias="PaymentMethodAdded")
    payment_method_indicator: Optional[PaymentMethodIndicator] = Field(default=None, alias="PaymentMethodIndicator")
    suspicious_activity_indicator: Optional[SuspiciousActivityIndicator] = Field(default=None, alias="SuspiciousActivityIndicator")
    __properties: ClassVar[List[str]] = ["AccountId", "AccountCreated", "AccountCreationIndicator", "AccountLastChanged", "AccountChangeIndicator", "PasswordLastChanged", "PasswordChangeIndicator", "PurchasesInTheLast6Months", "ShippingAddressAdded", "ShippingAddressUsageIndicator", "ProvisionAttempts", "TransactionalActivityPerDay", "TransactionalActivityPerYear", "PaymentMethodAdded", "PaymentMethodIndicator", "SuspiciousActivityIndicator"]

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
        """Create an instance of PayerAccountInformation from a JSON string"""
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
        # set to None if account_creation_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.account_creation_indicator is None and "account_creation_indicator" in self.model_fields_set:
            _dict['AccountCreationIndicator'] = None

        # set to None if account_change_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.account_change_indicator is None and "account_change_indicator" in self.model_fields_set:
            _dict['AccountChangeIndicator'] = None

        # set to None if password_change_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.password_change_indicator is None and "password_change_indicator" in self.model_fields_set:
            _dict['PasswordChangeIndicator'] = None

        # set to None if shipping_address_usage_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.shipping_address_usage_indicator is None and "shipping_address_usage_indicator" in self.model_fields_set:
            _dict['ShippingAddressUsageIndicator'] = None

        # set to None if payment_method_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.payment_method_indicator is None and "payment_method_indicator" in self.model_fields_set:
            _dict['PaymentMethodIndicator'] = None

        # set to None if suspicious_activity_indicator (nullable) is None
        # and model_fields_set contains the field
        if self.suspicious_activity_indicator is None and "suspicious_activity_indicator" in self.model_fields_set:
            _dict['SuspiciousActivityIndicator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PayerAccountInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "AccountId": obj.get("AccountId"),
            "AccountCreated": obj.get("AccountCreated"),
            "AccountCreationIndicator": obj.get("AccountCreationIndicator"),
            "AccountLastChanged": obj.get("AccountLastChanged"),
            "AccountChangeIndicator": obj.get("AccountChangeIndicator"),
            "PasswordLastChanged": obj.get("PasswordLastChanged"),
            "PasswordChangeIndicator": obj.get("PasswordChangeIndicator"),
            "PurchasesInTheLast6Months": obj.get("PurchasesInTheLast6Months"),
            "ShippingAddressAdded": obj.get("ShippingAddressAdded"),
            "ShippingAddressUsageIndicator": obj.get("ShippingAddressUsageIndicator"),
            "ProvisionAttempts": obj.get("ProvisionAttempts"),
            "TransactionalActivityPerDay": obj.get("TransactionalActivityPerDay"),
            "TransactionalActivityPerYear": obj.get("TransactionalActivityPerYear"),
            "PaymentMethodAdded": obj.get("PaymentMethodAdded"),
            "PaymentMethodIndicator": obj.get("PaymentMethodIndicator"),
            "SuspiciousActivityIndicator": obj.get("SuspiciousActivityIndicator")
        })
        return _obj


