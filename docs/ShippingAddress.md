# ShippingAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | The payer&#39;s country code in ISO-3166-1 format (e.g., HU or DE). Use &#x60;ZZ&#x60; if shipping address is not available. | 
**city** | **str** | Required if Region is specified. The complete name of the city of the recipient address. | [optional] 
**region** | **str** | Send &#x60;null&#x60; if not applicable. The country subdivision code (state or county) in [ISO-3166-2](https://en.wikipedia.org/wiki/ISO_3166-2:HU) format. | [optional] 
**zip** | **str** | The zip code of the recipient address. | [optional] 
**street** | **str** | The shipping street address with house number and other details. | [optional] 
**street2** | **str** | The address, continued. | [optional] 
**street3** | **str** | The address, continued. | [optional] 
**full_name** | **str** | The name of the customer on the shipping address. | [optional] 

## Example

```python
from clientapi_barion.models.shipping_address import ShippingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingAddress from a JSON string
shipping_address_instance = ShippingAddress.from_json(json)
# print the JSON string representation of the object
print(ShippingAddress.to_json())

# convert the object into a dict
shipping_address_dict = shipping_address_instance.to_dict()
# create an instance of ShippingAddress from a dict
shipping_address_from_dict = ShippingAddress.from_dict(shipping_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


