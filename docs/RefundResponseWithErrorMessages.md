# RefundResponseWithErrorMessages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The identifier of the payment in the Barion system. | [optional] 
**refunded_transactions** | [**List[RefundedTransaction]**](RefundedTransaction.md) |  | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.refund_response_with_error_messages import RefundResponseWithErrorMessages

# TODO update the JSON string below
json = "{}"
# create an instance of RefundResponseWithErrorMessages from a JSON string
refund_response_with_error_messages_instance = RefundResponseWithErrorMessages.from_json(json)
# print the JSON string representation of the object
print(RefundResponseWithErrorMessages.to_json())

# convert the object into a dict
refund_response_with_error_messages_dict = refund_response_with_error_messages_instance.to_dict()
# create an instance of RefundResponseWithErrorMessages from a dict
refund_response_with_error_messages_from_dict = RefundResponseWithErrorMessages.from_dict(refund_response_with_error_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


