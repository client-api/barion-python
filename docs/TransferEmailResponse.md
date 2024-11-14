# TransferEmailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_transfer_successful** | **bool** | Indicates wether the e-money transfer was successfuly finished. | [optional] 

## Example

```python
from clientapi_barion.models.transfer_email_response import TransferEmailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransferEmailResponse from a JSON string
transfer_email_response_instance = TransferEmailResponse.from_json(json)
# print the JSON string representation of the object
print(TransferEmailResponse.to_json())

# convert the object into a dict
transfer_email_response_dict = transfer_email_response_instance.to_dict()
# create an instance of TransferEmailResponse from a dict
transfer_email_response_from_dict = TransferEmailResponse.from_dict(transfer_email_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


