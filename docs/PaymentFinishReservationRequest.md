# PaymentFinishReservationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The identifier of the payment in the Barion system. | [optional] 
**transactions** | [**List[TransactionToFinish]**](TransactionToFinish.md) |  | [optional] 

## Example

```python
from clientapi_barion.models.payment_finish_reservation_request import PaymentFinishReservationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFinishReservationRequest from a JSON string
payment_finish_reservation_request_instance = PaymentFinishReservationRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFinishReservationRequest.to_json())

# convert the object into a dict
payment_finish_reservation_request_dict = payment_finish_reservation_request_instance.to_dict()
# create an instance of PaymentFinishReservationRequest from a dict
payment_finish_reservation_request_from_dict = PaymentFinishReservationRequest.from_dict(payment_finish_reservation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


