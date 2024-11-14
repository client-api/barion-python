# AccountInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bban_country** | **str** | ISO-3 country code of the country for the currency of the account. | [optional] 
**bban** | **str** | The BBAN (local bank account number) of the account for wire transfer topups (for HUF and CZK). | [optional] 
**iban** | **str** | The IBAN (international bank account number) of the account for wire transfer topups. | [optional] 
**reference** | **str** | Code used in conjunction with the bank account number for topups to a Barion deposit account. | [optional] 
**swift_code** | **str** | The Swift code of the bank for wire transfer topups. | [optional] 
**beneficiary** | [**Beneficiary**](Beneficiary.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.account_info import AccountInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfo from a JSON string
account_info_instance = AccountInfo.from_json(json)
# print the JSON string representation of the object
print(AccountInfo.to_json())

# convert the object into a dict
account_info_dict = account_info_instance.to_dict()
# create an instance of AccountInfo from a dict
account_info_from_dict = AccountInfo.from_dict(account_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


