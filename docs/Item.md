# Item


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The short name of the item. Shown to the payer on the Barion Smart Gateway. | 
**description** | **str** | The detailed description of the item. Not shown to the payer on the Barion Smart Gateway. | 
**image_url** | **str** | A URL pointing to an image that shows the item. Optional and for UX purposes only. | [optional] 
**quantity** | **float** | The total quantity of the item. | 
**unit** | **str** | The measurement unit of the item. | 
**unit_price** | **float** | The price of one measurement unit of the item. It can be any value, even negative if it indicates e.g. discount. | 
**item_total** | **float** | The total price of the item. Doesn&#39;t necessarily equal &#x60;Quantity × UnitPrice&#x60;. | 
**sku** | **str** | The SKU value of the item in the shop&#39;s inventory system. Optional. | [optional] 

## Example

```python
from clientapi_barion.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


