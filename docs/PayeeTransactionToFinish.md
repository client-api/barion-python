# PayeeTransactionToFinish


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier of the payee transaction in the Barion system. | 
**total** | **float** | The total amount of the payee transaction. | 
**comment** | **str** | Comment of the payee transaction. | [optional] 

## Example

```python
from clientapi_barion.models.payee_transaction_to_finish import PayeeTransactionToFinish

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeTransactionToFinish from a JSON string
payee_transaction_to_finish_instance = PayeeTransactionToFinish.from_json(json)
# print the JSON string representation of the object
print(PayeeTransactionToFinish.to_json())

# convert the object into a dict
payee_transaction_to_finish_dict = payee_transaction_to_finish_instance.to_dict()
# create an instance of PayeeTransactionToFinish from a dict
payee_transaction_to_finish_from_dict = PayeeTransactionToFinish.from_dict(payee_transaction_to_finish_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


