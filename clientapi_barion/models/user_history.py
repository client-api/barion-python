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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from clientapi_barion.models.user_history_participant import UserHistoryParticipant
from typing import Optional, Set
from typing_extensions import Self

class UserHistory(BaseModel):
    """
    UserHistory
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The identifier of the history item.", alias="Id")
    type: Optional[StrictStr] = Field(default=None, alias="Type")
    happened_at_utc: Optional[datetime] = Field(default=None, description="The exact time when the item happened.", alias="HappenedAtUtc")
    concurrency_order: Optional[StrictInt] = Field(default=None, description="The order of the transaction when more than one transaction happened at the same time. When only one transaction happened at a given timestamp, this value can be ignored.", alias="ConcurrencyOrder")
    source_account: Optional[UserHistoryParticipant] = Field(default=None, description="The user who initiated the transaction or from whom the money originated.", alias="SourceAccount")
    target_account: Optional[UserHistoryParticipant] = Field(default=None, description="The user who will receive the amount of the transaction.", alias="TargetAccount")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of the transaction.", alias="Amount")
    currency: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=3)]] = Field(default=None, description="The currency of the payment. Must be supplied in ISO 4217 format. This affects all transactions included in the payment; it is not possible to define multiple transactions in different currencies.", alias="Currency")
    description: Optional[Annotated[str, Field(strict=True, max_length=640)]] = Field(default=None, description="Description of the transaction.", alias="Description")
    is_in_progress: Optional[StrictBool] = Field(default=None, description="This flag indicates that the transaction is not in the final state.", alias="IsInProgress")
    balance_change_type: Optional[StrictStr] = Field(default=None, alias="BalanceChangeType")
    __properties: ClassVar[List[str]] = ["Id", "Type", "HappenedAtUtc", "ConcurrencyOrder", "SourceAccount", "TargetAccount", "Amount", "Currency", "Description", "IsInProgress", "BalanceChangeType"]

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
        """Create an instance of UserHistory from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source_account
        if self.source_account:
            _dict['SourceAccount'] = self.source_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_account
        if self.target_account:
            _dict['TargetAccount'] = self.target_account.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserHistory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Id": obj.get("Id"),
            "Type": obj.get("Type"),
            "HappenedAtUtc": obj.get("HappenedAtUtc"),
            "ConcurrencyOrder": obj.get("ConcurrencyOrder"),
            "SourceAccount": UserHistoryParticipant.from_dict(obj["SourceAccount"]) if obj.get("SourceAccount") is not None else None,
            "TargetAccount": UserHistoryParticipant.from_dict(obj["TargetAccount"]) if obj.get("TargetAccount") is not None else None,
            "Amount": obj.get("Amount"),
            "Currency": obj.get("Currency"),
            "Description": obj.get("Description"),
            "IsInProgress": obj.get("IsInProgress"),
            "BalanceChangeType": obj.get("BalanceChangeType")
        })
        return _obj


