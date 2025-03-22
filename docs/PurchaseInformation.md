# PurchaseInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_timeframe** | **str** | Enumeration indicating the length of the delivery period. | [optional] 
**delivery_email_address** | **str** | If goods are sent electronically, the payer&#39;s email address where goods should be delivered. | [optional] 
**pre_order_date** | **datetime** | The date when pre-ordered goods will be available, in UTC. | [optional] 
**availability_indicator** | **str** | Enumeration indicating when the goods will be available. | [optional] 
**re_order_indicator** | **str** | Enumeration indicating if the purchase is a re-order. | [optional] 
**shipping_address_indicator** | **str** | Enumeration indicating what kind of shipping is used. | [optional] 
**recurring_expiry** | **datetime** | &#x60;Required&#x60; in case of initial &#x60;Recurring&#x60; payment. The date past which no further payments should be accepted in the recurrence cycle, required for initial Recurring payments, in UTC. | [optional] 
**recurring_frequency** | **int** | &#x60;Required&#x60; in case of initial &#x60;Recurring&#x60; payment. Minimum number of days between subsequent payments for initial Recurring payments. | [optional] 
**purchase_type** | [**PurchaseType**](PurchaseType.md) | The type of purchase. | [optional] 
**gift_card_purchase** | [**GiftCardPurchase**](GiftCardPurchase.md) | Information about purchased gift cards. | [optional] 
**purchase_date** | **datetime** | The date and time of the purchase, in UTC. | [optional] 

## Example

```python
from clientapi_barion.models.purchase_information import PurchaseInformation

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseInformation from a JSON string
purchase_information_instance = PurchaseInformation.from_json(json)
# print the JSON string representation of the object
print(PurchaseInformation.to_json())

# convert the object into a dict
purchase_information_dict = purchase_information_instance.to_dict()
# create an instance of PurchaseInformation from a dict
purchase_information_from_dict = PurchaseInformation.from_dict(purchase_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


