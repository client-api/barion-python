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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from clientapi_barion.models.bank_account_details import BankAccountDetails
from clientapi_barion.models.bank_details import BankDetails
from clientapi_barion.models.recipient_details import RecipientDetails
from typing import Optional, Set
from typing_extensions import Self

class WithdrawBankTransferResponse(BaseModel):
    """
    WithdrawBankTransferResponse
    """ # noqa: E501
    transaction_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the bank transfer, generated by the Barion system.", alias="TransactionId")
    currency: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]] = Field(default=None, description="The currency of the payment. Must be supplied in ISO 4217 format. This affects all transactions included in the payment; it is not possible to define multiple transactions in different currencies.", alias="Currency")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount transferred.", alias="Amount")
    comment: Optional[Annotated[str, Field(strict=True, max_length=90)]] = Field(default=None, description="The comment associated with the bank transfer.", alias="Comment")
    bank_account: Optional[BankAccountDetails] = Field(default=None, description="Details of the recipient's bank account.", alias="BankAccount")
    bank: Optional[BankDetails] = Field(default=None, description="Details of the recipient's bank.", alias="Bank")
    recipient: Optional[RecipientDetails] = Field(default=None, description="Details of the recipient.", alias="Recipient")
    __properties: ClassVar[List[str]] = ["TransactionId", "Currency", "Amount", "Comment", "BankAccount", "Bank", "Recipient"]

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
        """Create an instance of WithdrawBankTransferResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of bank_account
        if self.bank_account:
            _dict['BankAccount'] = self.bank_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bank
        if self.bank:
            _dict['Bank'] = self.bank.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['Recipient'] = self.recipient.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WithdrawBankTransferResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "TransactionId": obj.get("TransactionId"),
            "Currency": obj.get("Currency"),
            "Amount": obj.get("Amount"),
            "Comment": obj.get("Comment"),
            "BankAccount": BankAccountDetails.from_dict(obj["BankAccount"]) if obj.get("BankAccount") is not None else None,
            "Bank": BankDetails.from_dict(obj["Bank"]) if obj.get("Bank") is not None else None,
            "Recipient": RecipientDetails.from_dict(obj["Recipient"]) if obj.get("Recipient") is not None else None
        })
        return _obj


