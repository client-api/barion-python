# GetPaymentStateResponseWithErrorMessages


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The identifier of the payment in the Barion system. | [optional] 
**payment_request_id** | **str** | The identifier of the payment in the shop&#39;s system. | [optional] 
**posid** | **str** | The public identifier of the shop that created the payment. | [optional] 
**pos_name** | **str** | The name of the shop that created the payment. | [optional] 
**pos_owner_email** | **str** | The e-mail address of the owner of the shop that created the payment. | [optional] 
**pos_owner_country** | **str** | ISO2 country code of the owner of the shop that created the payment. | [optional] 
**status** | [**PaymentStatus**](PaymentStatus.md) | The current status of the payment in the Barion system. | [optional] 
**payment_type** | [**PaymentType**](PaymentType.md) | The type of the payment. | [optional] 
**allowed_funding_sources** | **List[str]** | The allowed funding sources defined when creating the payment. **⚠️ Note ⚠️:** Barion&#39;s documentation is contradictory, as it refers to the bankcard as a &#x60;Card&#x60; in some places and as a &#x60;BankCard&#x60; in others, and does not mention it in others. Therefore we do not use &#x60;FundingResource&#x60; here. | [optional] 
**funding_source** | **str** | The funding source used to complete the payment. **⚠️ Note ⚠️:** Barion&#39;s documentation is contradictory as it should be of the &#x60;FundingSource&#x60; type. | [optional] 
**funding_information** | [**FundingInformation**](FundingInformation.md) | Detailed information about the funding source used to complete the payment. | [optional] 
**recurrence_type** | [**RecurrenceType**](RecurrenceType.md) | The RecurrenceType defined in the payment/start request for the recurring scenario. | [optional] 
**trace_id** | **str** | The Trace Id that identifies the recurring scenario. | [optional] 
**guest_checkout** | **bool** | Indicates whether the payment allows guest checkout. | [optional] 
**created_at** | **datetime** | The timestamp showing when the payment was created. | [optional] 
**completed_at** | **datetime** | The timestamp showing when the payment was completed. | [optional] 
**valid_until** | **datetime** | Timestamp showing the expiration time of the payment time window. | [optional] 
**reserved_until** | **datetime** | Timestamp showing the expiration time of the reservation time window. | [optional] 
**delayed_capture_until** | **datetime** | Timestamp showing the expiration time of the authorization time window. | [optional] 
**transactions** | [**List[DetailedPaymentTransaction]**](DetailedPaymentTransaction.md) | An array containing detailed structure of all transactions associated with the payment. | [optional] 
**total** | **float** | The total amount of the payment at the time of the request. | [optional] 
**currency** | [**Currency**](Currency.md) | The 3 character ISO 4217 currency code of the payment. | [optional] 
**suggested_locale** | **str** | Indicates in which language the Barion Smart Gateway should be shown for the payer. | [optional] 
**fraud_risk_score** | **int** | A risk score computed by the anti-fraud analysis, between 0 to 100. | [optional] 
**callback_url** | **str** | The URL where the Barion system sends requests whenever there is a change in the payment state. | [optional] 
**redirect_url** | **str** | The URL where the payer gets redirected after the payment is completed or cancelled. | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.get_payment_state_response_with_error_messages import GetPaymentStateResponseWithErrorMessages

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentStateResponseWithErrorMessages from a JSON string
get_payment_state_response_with_error_messages_instance = GetPaymentStateResponseWithErrorMessages.from_json(json)
# print the JSON string representation of the object
print(GetPaymentStateResponseWithErrorMessages.to_json())

# convert the object into a dict
get_payment_state_response_with_error_messages_dict = get_payment_state_response_with_error_messages_instance.to_dict()
# create an instance of GetPaymentStateResponseWithErrorMessages from a dict
get_payment_state_response_with_error_messages_from_dict = GetPaymentStateResponseWithErrorMessages.from_dict(get_payment_state_response_with_error_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


