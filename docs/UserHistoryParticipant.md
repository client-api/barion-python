# UserHistoryParticipant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_account_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**login_name** | **str** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**shop_id** | **str** |  | [optional] 
**shop_name** | **str** |  | [optional] 

## Example

```python
from clientapi_barion.models.user_history_participant import UserHistoryParticipant

# TODO update the JSON string below
json = "{}"
# create an instance of UserHistoryParticipant from a JSON string
user_history_participant_instance = UserHistoryParticipant.from_json(json)
# print the JSON string representation of the object
print(UserHistoryParticipant.to_json())

# convert the object into a dict
user_history_participant_dict = user_history_participant_instance.to_dict()
# create an instance of UserHistoryParticipant from a dict
user_history_participant_from_dict = UserHistoryParticipant.from_dict(user_history_participant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


