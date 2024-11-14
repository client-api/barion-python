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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from clientapi_barion.models.currency import Currency
from clientapi_barion.models.detailed_payment_transaction import DetailedPaymentTransaction
from clientapi_barion.models.funding_information import FundingInformation
from clientapi_barion.models.payment_status import PaymentStatus
from clientapi_barion.models.recurrence_type import RecurrenceType
from typing import Optional, Set
from typing_extensions import Self

class GetPaymentStateResponse(BaseModel):
    """
    GetPaymentStateResponse
    """ # noqa: E501
    payment_id: Optional[StrictStr] = Field(default=None, description="The identifier of the payment in the Barion system.", alias="PaymentId")
    payment_request_id: Optional[StrictStr] = Field(default=None, description="The identifier of the payment in the shop's system.", alias="PaymentRequestId")
    posid: Optional[StrictStr] = Field(default=None, description="The public identifier of the shop that created the payment.", alias="POSId")
    pos_name: Optional[StrictStr] = Field(default=None, description="The name of the shop that created the payment.", alias="POSName")
    pos_owner_email: Optional[StrictStr] = Field(default=None, description="The e-mail address of the owner of the shop that created the payment.", alias="POSOwnerEmail")
    pos_owner_country: Optional[StrictStr] = Field(default=None, description="ISO2 country code of the owner of the shop that created the payment.", alias="POSOwnerCountry")
    status: Optional[PaymentStatus] = Field(default=None, description="The current status of the payment in the Barion system.", alias="Status")
    payment_type: Optional[StrictStr] = Field(default=None, description="The type of the payment.", alias="PaymentType")
    allowed_funding_sources: Optional[List[StrictStr]] = Field(default=None, description="The allowed funding sources defined when creating the payment. **⚠️ Note ⚠️:** Barion's documentation is contradictory, as it refers to the bankcard as a `Card` in some places and as a `BankCard` in others, and does not mention it in others. Therefore we do not use `FundingResource` here.", alias="AllowedFundingSources")
    funding_source: Optional[StrictStr] = Field(default=None, description="The funding source used to complete the payment. **⚠️ Note ⚠️:** Barion's documentation is contradictory as it should be of the `FundingSource` type.", alias="FundingSource")
    funding_information: Optional[FundingInformation] = Field(default=None, description="Detailed information about the funding source used to complete the payment.", alias="FundingInformation")
    recurrence_type: Optional[RecurrenceType] = Field(default=None, description="The RecurrenceType defined in the payment/start request for the recurring scenario.", alias="RecurrenceType")
    trace_id: Optional[StrictStr] = Field(default=None, description="The Trace Id that identifies the recurring scenario.", alias="TraceId")
    guest_checkout: Optional[StrictBool] = Field(default=None, description="Indicates whether the payment allows guest checkout.", alias="GuestCheckout")
    created_at: Optional[datetime] = Field(default=None, description="The timestamp showing when the payment was created.", alias="CreatedAt")
    completed_at: Optional[datetime] = Field(default=None, description="The timestamp showing when the payment was completed.", alias="CompletedAt")
    valid_until: Optional[datetime] = Field(default=None, description="Timestamp showing the expiration time of the payment time window.", alias="ValidUntil")
    reserved_until: Optional[datetime] = Field(default=None, description="Timestamp showing the expiration time of the reservation time window.", alias="ReservedUntil")
    delayed_capture_until: Optional[datetime] = Field(default=None, description="Timestamp showing the expiration time of the authorization time window.", alias="DelayedCaptureUntil")
    transactions: Optional[List[DetailedPaymentTransaction]] = Field(default=None, description="An array containing detailed structure of all transactions associated with the payment.", alias="Transactions")
    total: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount of the payment at the time of the request.", alias="Total")
    currency: Optional[Currency] = Field(default=None, description="The 3 character ISO 4217 currency code of the payment.", alias="Currency")
    suggested_locale: Optional[StrictStr] = Field(default=None, description="Indicates in which language the Barion Smart Gateway should be shown for the payer.", alias="SuggestedLocale")
    fraud_risk_score: Optional[StrictInt] = Field(default=None, description="A risk score computed by the anti-fraud analysis, between 0 to 100.", alias="FraudRiskScore")
    callback_url: Optional[StrictStr] = Field(default=None, description="The URL where the Barion system sends requests whenever there is a change in the payment state.", alias="CallbackUrl")
    redirect_url: Optional[StrictStr] = Field(default=None, description="The URL where the payer gets redirected after the payment is completed or cancelled.", alias="RedirectUrl")
    __properties: ClassVar[List[str]] = ["PaymentId", "PaymentRequestId", "POSId", "POSName", "POSOwnerEmail", "POSOwnerCountry", "Status", "PaymentType", "AllowedFundingSources", "FundingSource", "FundingInformation", "RecurrenceType", "TraceId", "GuestCheckout", "CreatedAt", "CompletedAt", "ValidUntil", "ReservedUntil", "DelayedCaptureUntil", "Transactions", "Total", "Currency", "SuggestedLocale", "FraudRiskScore", "CallbackUrl", "RedirectUrl"]

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
        """Create an instance of GetPaymentStateResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of funding_information
        if self.funding_information:
            _dict['FundingInformation'] = self.funding_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item_transactions in self.transactions:
                if _item_transactions:
                    _items.append(_item_transactions.to_dict())
            _dict['Transactions'] = _items
        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['Status'] = None

        # set to None if payment_type (nullable) is None
        # and model_fields_set contains the field
        if self.payment_type is None and "payment_type" in self.model_fields_set:
            _dict['PaymentType'] = None

        # set to None if recurrence_type (nullable) is None
        # and model_fields_set contains the field
        if self.recurrence_type is None and "recurrence_type" in self.model_fields_set:
            _dict['RecurrenceType'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['Currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetPaymentStateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "PaymentId": obj.get("PaymentId"),
            "PaymentRequestId": obj.get("PaymentRequestId"),
            "POSId": obj.get("POSId"),
            "POSName": obj.get("POSName"),
            "POSOwnerEmail": obj.get("POSOwnerEmail"),
            "POSOwnerCountry": obj.get("POSOwnerCountry"),
            "Status": obj.get("Status"),
            "PaymentType": obj.get("PaymentType"),
            "AllowedFundingSources": obj.get("AllowedFundingSources"),
            "FundingSource": obj.get("FundingSource"),
            "FundingInformation": FundingInformation.from_dict(obj["FundingInformation"]) if obj.get("FundingInformation") is not None else None,
            "RecurrenceType": obj.get("RecurrenceType"),
            "TraceId": obj.get("TraceId"),
            "GuestCheckout": obj.get("GuestCheckout"),
            "CreatedAt": obj.get("CreatedAt"),
            "CompletedAt": obj.get("CompletedAt"),
            "ValidUntil": obj.get("ValidUntil"),
            "ReservedUntil": obj.get("ReservedUntil"),
            "DelayedCaptureUntil": obj.get("DelayedCaptureUntil"),
            "Transactions": [DetailedPaymentTransaction.from_dict(_item) for _item in obj["Transactions"]] if obj.get("Transactions") is not None else None,
            "Total": obj.get("Total"),
            "Currency": obj.get("Currency"),
            "SuggestedLocale": obj.get("SuggestedLocale"),
            "FraudRiskScore": obj.get("FraudRiskScore"),
            "CallbackUrl": obj.get("CallbackUrl"),
            "RedirectUrl": obj.get("RedirectUrl")
        })
        return _obj


