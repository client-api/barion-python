# PaymentTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pos_transaction_id** | **str** | The unique identifier of the transaction at the shop that started the payment. | [optional] 
**payee** | **str** | The recipient user of the transaction. This Barion Wallet receives the money when the payment is completed by the payer. | [optional] 
**total** | **float** | The total amount of the transaction. This is the amount that is charged towards the payer when completing the payment. The final amount of the transactiom. This will overwrite the original amount. The allowed number of decimal digits depends on the currency of the payment containing this transaction:   - &#x60;CZK&#x60;: two digits  - &#x60;EUR&#x60;: two digits  - &#x60;HUF&#x60;: zero digits  - &#x60;USD&#x60;: two digits | [optional] 
**comment** | **str** | A comment associated with the transaction. This is NOT shown to the payer. Description of the transaction, this will overwrite the original description | [optional] 
**payee_transactions** | [**List[PayeeTransaction]**](PayeeTransaction.md) | An array containing possible sub-transactions, which are executed after the payment was completed. | [optional] 
**items** | [**List[Item]**](Item.md) | An array containing the items (products or services) included in the transaction. | [optional] 

## Example

```python
from clientapi_barion.models.payment_transaction import PaymentTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTransaction from a JSON string
payment_transaction_instance = PaymentTransaction.from_json(json)
# print the JSON string representation of the object
print(PaymentTransaction.to_json())

# convert the object into a dict
payment_transaction_dict = payment_transaction_instance.to_dict()
# create an instance of PaymentTransaction from a dict
payment_transaction_from_dict = PaymentTransaction.from_dict(payment_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


