# GetUserHistoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_history** | [**List[UserHistory]**](UserHistory.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.get_user_history_response import GetUserHistoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserHistoryResponse from a JSON string
get_user_history_response_instance = GetUserHistoryResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserHistoryResponse.to_json())

# convert the object into a dict
get_user_history_response_dict = get_user_history_response_instance.to_dict()
# create an instance of GetUserHistoryResponse from a dict
get_user_history_response_from_dict = GetUserHistoryResponse.from_dict(get_user_history_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


