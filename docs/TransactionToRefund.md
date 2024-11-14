# TransactionToRefund


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** | The unique identifier of the transaction in the Barion system. | 
**pos_transaction_id** | **str** | The unique identifier of the transaction at the shop that initiated the payment. | 
**amount_to_refund** | **float** | The amount to refund from the given transaction. Must be greater than zero and cannot exceed the remaining value of the transaction after previous refunds. | 
**comment** | **str** | A comment associated with the refund. This is shown to the original payer. | [optional] 

## Example

```python
from clientapi_barion.models.transaction_to_refund import TransactionToRefund

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionToRefund from a JSON string
transaction_to_refund_instance = TransactionToRefund.from_json(json)
# print the JSON string representation of the object
print(TransactionToRefund.to_json())

# convert the object into a dict
transaction_to_refund_dict = transaction_to_refund_instance.to_dict()
# create an instance of TransactionToRefund from a dict
transaction_to_refund_from_dict = TransactionToRefund.from_dict(transaction_to_refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


