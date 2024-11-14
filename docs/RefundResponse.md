# RefundResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The identifier of the payment in the Barion system. | [optional] 
**refunded_transactions** | [**List[RefundedTransaction]**](RefundedTransaction.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.refund_response import RefundResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RefundResponse from a JSON string
refund_response_instance = RefundResponse.from_json(json)
# print the JSON string representation of the object
print(RefundResponse.to_json())

# convert the object into a dict
refund_response_dict = refund_response_instance.to_dict()
# create an instance of RefundResponse from a dict
refund_response_from_dict = RefundResponse.from_dict(refund_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


