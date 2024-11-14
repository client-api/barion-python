# RefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The identifier of the payment in the Barion system. | 
**transactions_to_refund** | [**List[TransactionToRefund]**](TransactionToRefund.md) |  | 

## Example

```python
from clientapi_barion.models.refund_request import RefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RefundRequest from a JSON string
refund_request_instance = RefundRequest.from_json(json)
# print the JSON string representation of the object
print(RefundRequest.to_json())

# convert the object into a dict
refund_request_dict = refund_request_instance.to_dict()
# create an instance of RefundRequest from a dict
refund_request_from_dict = RefundRequest.from_dict(refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


