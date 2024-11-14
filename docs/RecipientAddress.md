# RecipientAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | 3-letter ISO 3166-1 Alpha-3 country code of the recipient&#39;s address. | 
**street** | **str** | Street and street number part of the recipient&#39;s address. | 
**city** | **str** | City part of the recipient&#39;s address. | 
**zip** | **str** | Zip part of the recipient&#39;s address. | 

## Example

```python
from clientapi_barion.models.recipient_address import RecipientAddress

# TODO update the JSON string below
json = "{}"
# create an instance of RecipientAddress from a JSON string
recipient_address_instance = RecipientAddress.from_json(json)
# print the JSON string representation of the object
print(RecipientAddress.to_json())

# convert the object into a dict
recipient_address_dict = recipient_address_instance.to_dict()
# create an instance of RecipientAddress from a dict
recipient_address_from_dict = RecipientAddress.from_dict(recipient_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


