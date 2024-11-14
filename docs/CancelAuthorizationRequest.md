# CancelAuthorizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The identifier of the payment in the Barion system. | 

## Example

```python
from clientapi_barion.models.cancel_authorization_request import CancelAuthorizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelAuthorizationRequest from a JSON string
cancel_authorization_request_instance = CancelAuthorizationRequest.from_json(json)
# print the JSON string representation of the object
print(CancelAuthorizationRequest.to_json())

# convert the object into a dict
cancel_authorization_request_dict = cancel_authorization_request_instance.to_dict()
# create an instance of CancelAuthorizationRequest from a dict
cancel_authorization_request_from_dict = CancelAuthorizationRequest.from_dict(cancel_authorization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


