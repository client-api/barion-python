# PayerAccountInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | A unique ID of the payer&#39;s account in the merchant&#39;s system. | [optional] 
**account_created** | **datetime** | The timestamp when the payer created its account in UTC. | [optional] 
**account_creation_indicator** | [**AccountCreationIndicator**](AccountCreationIndicator.md) |  | [optional] 
**account_last_changed** | **datetime** | The timestamp when the payer last changed its account in UTC. | [optional] 
**account_change_indicator** | [**AccountChangeIndicator**](AccountChangeIndicator.md) |  | [optional] 
**password_last_changed** | **datetime** | The timestamp when the payer last changed its password in UTC. | [optional] 
**password_change_indicator** | [**PasswordChangeIndicator**](PasswordChangeIndicator.md) |  | [optional] 
**purchases_in_the_last6_months** | **int** | The number of successful purchases of the payer in the last 6 months. | [optional] 
**shipping_address_added** | **datetime** | The timestamp when the shipping address used for this payment was added to the payer&#39;s account in UTC. | [optional] 
**shipping_address_usage_indicator** | [**ShippingAddressUsageIndicator**](ShippingAddressUsageIndicator.md) |  | [optional] 
**provision_attempts** | **int** | How many times the customer tried to add a card to its account during the last 24 hours. | [optional] 
**transactional_activity_per_day** | **int** | The number of purchases attached to this payer in the last 24 hours. | [optional] 
**transactional_activity_per_year** | **int** | The number of purchases attached to this payer in the last 365 days. | [optional] 
**payment_method_added** | **datetime** | When this card was added to the payer&#39;s account in UTC. | [optional] 
**payment_method_indicator** | [**PaymentMethodIndicator**](PaymentMethodIndicator.md) |  | [optional] 
**suspicious_activity_indicator** | [**SuspiciousActivityIndicator**](SuspiciousActivityIndicator.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.payer_account_information import PayerAccountInformation

# TODO update the JSON string below
json = "{}"
# create an instance of PayerAccountInformation from a JSON string
payer_account_information_instance = PayerAccountInformation.from_json(json)
# print the JSON string representation of the object
print(PayerAccountInformation.to_json())

# convert the object into a dict
payer_account_information_dict = payer_account_information_instance.to_dict()
# create an instance of PayerAccountInformation from a dict
payer_account_information_from_dict = PayerAccountInformation.from_dict(payer_account_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


