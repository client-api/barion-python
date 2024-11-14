# TransferEmailResponseWithErrorMessages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_transfer_successful** | **bool** | Indicates wether the e-money transfer was successfuly finished. | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.transfer_email_response_with_error_messages import TransferEmailResponseWithErrorMessages

# TODO update the JSON string below
json = "{}"
# create an instance of TransferEmailResponseWithErrorMessages from a JSON string
transfer_email_response_with_error_messages_instance = TransferEmailResponseWithErrorMessages.from_json(json)
# print the JSON string representation of the object
print(TransferEmailResponseWithErrorMessages.to_json())

# convert the object into a dict
transfer_email_response_with_error_messages_dict = transfer_email_response_with_error_messages_instance.to_dict()
# create an instance of TransferEmailResponseWithErrorMessages from a dict
transfer_email_response_with_error_messages_from_dict = TransferEmailResponseWithErrorMessages.from_dict(transfer_email_response_with_error_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


