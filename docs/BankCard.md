# BankCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**masked_pan** | **str** | The last four digits of the card number. | [optional] 
**bank_card_type** | [**CardType**](CardType.md) |  | [optional] 
**valid_thru_year** | **str** | The 4-digit year part of the card validity date. | [optional] 
**valid_thru_month** | **str** | The 2-digit month part of the card validity date. | [optional] 

## Example

```python
from clientapi_barion.models.bank_card import BankCard

# TODO update the JSON string below
json = "{}"
# create an instance of BankCard from a JSON string
bank_card_instance = BankCard.from_json(json)
# print the JSON string representation of the object
print(BankCard.to_json())

# convert the object into a dict
bank_card_dict = bank_card_instance.to_dict()
# create an instance of BankCard from a dict
bank_card_from_dict = BankCard.from_dict(bank_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


