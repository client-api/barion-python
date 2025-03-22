# BankAccountDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | 3-letter ISO 3166-1 Alpha-3 country code of the recipient&#39;s bank. | 
**format** | **str** | Format of the bank account number for bank transfers.  | 
**account_number** | **str** | Bank account number. Must comply with legal GIRO/IBAN format standards if applicable.  | 

## Example

```python
from clientapi_barion.models.bank_account_details import BankAccountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BankAccountDetails from a JSON string
bank_account_details_instance = BankAccountDetails.from_json(json)
# print the JSON string representation of the object
print(BankAccountDetails.to_json())

# convert the object into a dict
bank_account_details_dict = bank_account_details_instance.to_dict()
# create an instance of BankAccountDetails from a dict
bank_account_details_from_dict = BankAccountDetails.from_dict(bank_account_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


