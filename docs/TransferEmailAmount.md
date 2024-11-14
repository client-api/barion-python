# TransferEmailAmount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**Currency**](Currency.md) | The currency of the money | [optional] 
**value** | **float** | The total amount of money in the currency set above. | [optional] 

## Example

```python
from clientapi_barion.models.transfer_email_amount import TransferEmailAmount

# TODO update the JSON string below
json = "{}"
# create an instance of TransferEmailAmount from a JSON string
transfer_email_amount_instance = TransferEmailAmount.from_json(json)
# print the JSON string representation of the object
print(TransferEmailAmount.to_json())

# convert the object into a dict
transfer_email_amount_dict = transfer_email_amount_instance.to_dict()
# create an instance of TransferEmailAmount from a dict
transfer_email_amount_from_dict = TransferEmailAmount.from_dict(transfer_email_amount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


