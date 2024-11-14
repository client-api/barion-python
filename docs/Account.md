# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The unique identifier of the account. | [optional] 
**balance** | [**Balance**](Balance.md) | The current balance of the account. | [optional] 
**currency** | [**Currency**](Currency.md) | The currency of the account in 3-letter ISO country code format. | [optional] 
**account_info** | [**AccountInfo**](AccountInfo.md) | Information about how to topup the account. | [optional] 

## Example

```python
from clientapi_barion.models.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


