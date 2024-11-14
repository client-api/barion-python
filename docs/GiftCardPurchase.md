# GiftCardPurchase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The total amount of gift cards purchased, depending on payment currency precision. - &#x60;CZK&#x60;: two digits - &#x60;EUR&#x60;: two digits - &#x60;HUF&#x60;: zero digits - &#x60;USD&#x60;: two digits | [optional] 
**count** | **int** | The number of gift cards purchased. | [optional] 

## Example

```python
from clientapi_barion.models.gift_card_purchase import GiftCardPurchase

# TODO update the JSON string below
json = "{}"
# create an instance of GiftCardPurchase from a JSON string
gift_card_purchase_instance = GiftCardPurchase.from_json(json)
# print the JSON string representation of the object
print(GiftCardPurchase.to_json())

# convert the object into a dict
gift_card_purchase_dict = gift_card_purchase_instance.to_dict()
# create an instance of GiftCardPurchase from a dict
gift_card_purchase_from_dict = GiftCardPurchase.from_dict(gift_card_purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


