# UserInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**NameInformation**](NameInformation.md) | Structure representing the name of the user. | [optional] 
**email** | **str** | The e-mail address of the user. | [optional] 

## Example

```python
from clientapi_barion.models.user_information import UserInformation

# TODO update the JSON string below
json = "{}"
# create an instance of UserInformation from a JSON string
user_information_instance = UserInformation.from_json(json)
# print the JSON string representation of the object
print(UserInformation.to_json())

# convert the object into a dict
user_information_dict = user_information_instance.to_dict()
# create an instance of UserInformation from a dict
user_information_from_dict = UserInformation.from_dict(user_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


