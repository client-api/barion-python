# Beneficiary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The displayed name of the wallet that will be the target of the wire transfer. | [optional] 
**country** | **str** | ISO-3 country code of the wire transfer target&#39;s address. | [optional] 
**city** | **str** | The city of the wire transfer target&#39;s address. | [optional] 
**zip** | **str** | The zip code of the wire transfer target&#39;s address. | [optional] 
**street** | **str** | The street and house number of the wire transfer target&#39;s address. | [optional] 

## Example

```python
from clientapi_barion.models.beneficiary import Beneficiary

# TODO update the JSON string below
json = "{}"
# create an instance of Beneficiary from a JSON string
beneficiary_instance = Beneficiary.from_json(json)
# print the JSON string representation of the object
print(Beneficiary.to_json())

# convert the object into a dict
beneficiary_dict = beneficiary_instance.to_dict()
# create an instance of Beneficiary from a dict
beneficiary_from_dict = Beneficiary.from_dict(beneficiary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


