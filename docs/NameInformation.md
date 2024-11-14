# NameInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_name** | **str** | The login name of the user. | [optional] 
**first_name** | **str** | The first name of the user, if applicable. | [optional] 
**last_name** | **str** | The last name of the user, if applicable. | [optional] 
**organization_name** | **str** | The organization name of the user, if applicable. | [optional] 

## Example

```python
from clientapi_barion.models.name_information import NameInformation

# TODO update the JSON string below
json = "{}"
# create an instance of NameInformation from a JSON string
name_information_instance = NameInformation.from_json(json)
# print the JSON string representation of the object
print(NameInformation.to_json())

# convert the object into a dict
name_information_dict = name_information_instance.to_dict()
# create an instance of NameInformation from a dict
name_information_from_dict = NameInformation.from_dict(name_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


