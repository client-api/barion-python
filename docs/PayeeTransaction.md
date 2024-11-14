# PayeeTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pos_transaction_id** | **str** | The unique identifier of the transaction at the shop that started the payment. | 
**payee** | **str** | The recipient&#39;s e-mail address. Payees other than the shop owner&#39;s Barion Wallet can only be listed if the shop has Barion Bridge enabled. | 
**total** | **float** | The total amount of the transaction. | 
**comment** | **str** | Comment of the transaction. This is shown to the recipient. | [optional] 

## Example

```python
from clientapi_barion.models.payee_transaction import PayeeTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PayeeTransaction from a JSON string
payee_transaction_instance = PayeeTransaction.from_json(json)
# print the JSON string representation of the object
print(PayeeTransaction.to_json())

# convert the object into a dict
payee_transaction_dict = payee_transaction_instance.to_dict()
# create an instance of PayeeTransaction from a dict
payee_transaction_from_dict = PayeeTransaction.from_dict(payee_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


