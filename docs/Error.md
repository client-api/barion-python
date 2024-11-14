# Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **str** | The error code of the payment, can be interpreted as an error Id. | [optional] 
**title** | **str** | The title of the error, is a more readable form of the error. | [optional] 
**description** | **str** | The description of the error, more information about the error. | [optional] 
**end_point** | **str** | The URL of the API endpoint to help the reproduction of the error scenario. | [optional] 
**auth_data** | **str** | The e-mail address of the caller to help the reproduction of the error scenario. | [optional] 
**happened_at** | **datetime** | The timestamp of the response. | [optional] 
**payment_id** | **str** | If the error is related to a business process that involves a given payment, the public identifier of the payment is supplied here. This property is not present for all errors. | [optional] 

## Example

```python
from clientapi_barion.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


