# StartPaymentWithGoogleToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer_email_address** | **str** | The e-mail address of the Google Pay user. This is provided by Google. | 
**google_pay_token** | **str** | The Google Pay token. The encrypted Google Pay token that contains the card information. | 

## Example

```python
from clientapi_barion.models.start_payment_with_google_token import StartPaymentWithGoogleToken

# TODO update the JSON string below
json = "{}"
# create an instance of StartPaymentWithGoogleToken from a JSON string
start_payment_with_google_token_instance = StartPaymentWithGoogleToken.from_json(json)
# print the JSON string representation of the object
print(StartPaymentWithGoogleToken.to_json())

# convert the object into a dict
start_payment_with_google_token_dict = start_payment_with_google_token_instance.to_dict()
# create an instance of StartPaymentWithGoogleToken from a dict
start_payment_with_google_token_from_dict = StartPaymentWithGoogleToken.from_dict(start_payment_with_google_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


