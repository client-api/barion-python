# UserHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the history item. | [optional] 
**type** | **str** |  | [optional] 
**happened_at_utc** | **datetime** | The exact time when the item happened. | [optional] 
**concurrency_order** | **int** | The order of the transaction when more than one transaction happened at the same time. When only one transaction happened at a given timestamp, this value can be ignored. | [optional] 
**source_account** | [**UserHistoryParticipant**](UserHistoryParticipant.md) | The user who initiated the transaction or from whom the money originated. | [optional] 
**target_account** | [**UserHistoryParticipant**](UserHistoryParticipant.md) | The user who will receive the amount of the transaction. | [optional] 
**amount** | **float** | The amount of the transaction. | [optional] 
**currency** | **str** | The currency of the payment. Must be supplied in ISO 4217 format. This affects all transactions included in the payment; it is not possible to define multiple transactions in different currencies. | [optional] 
**description** | **str** | Description of the transaction. | [optional] 
**is_in_progress** | **bool** | This flag indicates that the transaction is not in the final state. | [optional] 
**balance_change_type** | **str** |  | [optional] 

## Example

```python
from clientapi_barion.models.user_history import UserHistory

# TODO update the JSON string below
json = "{}"
# create an instance of UserHistory from a JSON string
user_history_instance = UserHistory.from_json(json)
# print the JSON string representation of the object
print(UserHistory.to_json())

# convert the object into a dict
user_history_dict = user_history_instance.to_dict()
# create an instance of UserHistory from a dict
user_history_from_dict = UserHistory.from_dict(user_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


