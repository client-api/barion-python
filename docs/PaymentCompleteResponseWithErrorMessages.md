# PaymentCompleteResponseWithErrorMessages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The identifier of the payment, generated by the Barion system. | [optional] 
**payment_request_id** | **str** | The payment identifier supplied by the API caller in the request. | [optional] 
**payment_status** | **str** | The status of the payment in the Barion system. | [optional] 
**is_successful** | **bool** | Indicates whether the charge was successful. | [optional] 
**trace_id** | **str** | Identifies the nature of the token payment. | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.payment_complete_response_with_error_messages import PaymentCompleteResponseWithErrorMessages

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentCompleteResponseWithErrorMessages from a JSON string
payment_complete_response_with_error_messages_instance = PaymentCompleteResponseWithErrorMessages.from_json(json)
# print the JSON string representation of the object
print(PaymentCompleteResponseWithErrorMessages.to_json())

# convert the object into a dict
payment_complete_response_with_error_messages_dict = payment_complete_response_with_error_messages_instance.to_dict()
# create an instance of PaymentCompleteResponseWithErrorMessages from a dict
payment_complete_response_with_error_messages_from_dict = PaymentCompleteResponseWithErrorMessages.from_dict(payment_complete_response_with_error_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


