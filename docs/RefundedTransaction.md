# RefundedTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier of the transaction in the Barion system. | [optional] 
**pos_transaction_id** | **str** | The unique identifier of the transaction at the shop that initiated the payment. | [optional] 
**total** | **float** | The amount that has been refunded from the given transaction. | [optional] 
**comment** | **str** | The comment associated with the refund. | [optional] 
**status** | [**TransactionStatus**](TransactionStatus.md) | The status of the transaction. | [optional] 

## Example

```python
from clientapi_barion.models.refunded_transaction import RefundedTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of RefundedTransaction from a JSON string
refunded_transaction_instance = RefundedTransaction.from_json(json)
# print the JSON string representation of the object
print(RefundedTransaction.to_json())

# convert the object into a dict
refunded_transaction_dict = refunded_transaction_instance.to_dict()
# create an instance of RefundedTransaction from a dict
refunded_transaction_from_dict = RefundedTransaction.from_dict(refunded_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


