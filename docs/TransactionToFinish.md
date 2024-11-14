# TransactionToFinish


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier of the transaction in the Barion system. | 
**total** | **float** | The total amount of the transaction. | 
**comment** | **str** | A comment associated with the transaction. | [optional] 
**payee_transactions** | [**List[PayeeTransactionToFinish]**](PayeeTransactionToFinish.md) |  | [optional] 
**items** | [**List[Item]**](Item.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.transaction_to_finish import TransactionToFinish

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionToFinish from a JSON string
transaction_to_finish_instance = TransactionToFinish.from_json(json)
# print the JSON string representation of the object
print(TransactionToFinish.to_json())

# convert the object into a dict
transaction_to_finish_dict = transaction_to_finish_instance.to_dict()
# create an instance of TransactionToFinish from a dict
transaction_to_finish_from_dict = TransactionToFinish.from_dict(transaction_to_finish_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


