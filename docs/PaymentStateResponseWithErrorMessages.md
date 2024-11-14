# PaymentStateResponseWithErrorMessages


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
**allowed_funding_sources** | **List[str]** | The allowed funding sources that were defined when creating the payment. **⚠️ Note ⚠️:** Barion&#39;s documentation is contradictory, as it refers to the bankcard as a &#x60;Card&#x60; in some places and as a &#x60;BankCard&#x60; in others, and does not mention it in others. Therefore we do not use &#x60;FundingResource&#x60; here. | [optional] 
**funding_source** | **str** | The funding source that was used to complete the payment. **⚠️ Note ⚠️:** Barion&#39;s documentation is contradictory as it should be of the &#x60;FundingSource&#x60; type. | [optional] 
**funding_information** | [**FundingInformation**](FundingInformation.md) | Detailed information about the funding source that was used to complete the payment. | [optional] 
**recurrence_type** | [**RecurrenceType**](RecurrenceType.md) | The RecurrenceType that was defined in the payment/start request for the recurring scenario. | [optional] 
**trace_id** | **str** | The Trace Id that identifies that recurring scenario. | [optional] 
**guest_checkout** | **bool** | Indicates whether the payment allows guest checkout. | [optional] 
**created_at** | **datetime** | The locale-specific payment creation timestamp. | [optional] 
**completed_at** | **datetime** | The locale-specific payment completion timestamp. If the payment is not yet completed, this is empty. | [optional] 
**valid_until** | **datetime** | The payment must be completed before this locale-specific payment expiration timestamp. | [optional] 
**reserved_until** | **datetime** | If the payment is a reservation, the shop&#39;s owner has until this locale-specific expiration timestamp to finish it. If the payment isn&#39;t a reservation, this is empty. | [optional] 
**delayed_capture_until** | **datetime** | If the payment is a delayed capture, the shop owner has until this locale-specific expiration timestamp to capture it. If the payment isn&#39;t a delayed capture, this is empty. | [optional] 
**transactions** | [**List[DetailedPaymentTransaction]**](DetailedPaymentTransaction.md) |  | [optional] 
**total** | **float** | The total amount of the payment at the time of the request to the endpoint. | [optional] 
**currency** | [**Currency**](Currency.md) | The payment&#39;s 3-character ISO 4217 currency code. | [optional] 
**suggested_locale** | **str** | Indicates the language that the Barion Smart Gateway should be displayed to the payer. | [optional] 
**fraud_risk_score** | **int** | A risk score computed by the anti-fraud analysis, ranging from 0 (completely legit) to 100 (certain fraud). | [optional] 
**callback_url** | **str** | The URL (including the payment identifier) where the Barion system will send (or has already sent) a request to whenever there is a change in the state of the payment. | [optional] 
**redirect_url** | **str** | The URL (including the payment identifier) where the payer gets (or has already got) redirected to after the payment is, or was completed, or cancelled. | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) | The last method used when attempting to complete the payment. If there was no payment attempt made yet, this property is &#x60;Unknown&#x60;. | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.payment_state_response_with_error_messages import PaymentStateResponseWithErrorMessages

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentStateResponseWithErrorMessages from a JSON string
payment_state_response_with_error_messages_instance = PaymentStateResponseWithErrorMessages.from_json(json)
# print the JSON string representation of the object
print(PaymentStateResponseWithErrorMessages.to_json())

# convert the object into a dict
payment_state_response_with_error_messages_dict = payment_state_response_with_error_messages_instance.to_dict()
# create an instance of PaymentStateResponseWithErrorMessages from a dict
payment_state_response_with_error_messages_from_dict = PaymentStateResponseWithErrorMessages.from_dict(payment_state_response_with_error_messages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


