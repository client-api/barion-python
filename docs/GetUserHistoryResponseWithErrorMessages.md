# GetUserHistoryResponseWithErrorMessages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_history** | [**List[UserHistory]**](UserHistory.md) |  | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.get_user_history_response_with_error_messages import GetUserHistoryResponseWithErrorMessages

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserHistoryResponseWithErrorMessages from a JSON string
get_user_history_response_with_error_messages_instance = GetUserHistoryResponseWithErrorMessages.from_json(json)
# print the JSON string representation of the object
print(GetUserHistoryResponseWithErrorMessages.to_json())

# convert the object into a dict
get_user_history_response_with_error_messages_dict = get_user_history_response_with_error_messages_instance.to_dict()
# create an instance of GetUserHistoryResponseWithErrorMessages from a dict
get_user_history_response_with_error_messages_from_dict = GetUserHistoryResponseWithErrorMessages.from_dict(get_user_history_response_with_error_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


