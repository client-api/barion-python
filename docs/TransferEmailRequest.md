# TransferEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_account_id** | **str** | The identifier of the Barion wallet. This can be determined using the [Accounts-Get-v2](https://docs.barion.com/Accounts-Get-v2) API endpoint. | 
**amount** | [**TransferEmailAmount**](TransferEmailAmount.md) |  | 
**target_email** | **str** | The e-mail address of the recipient of the transfer. If they are an active Barion user, they receive the money instantly. If the e-mail address is not registered in Barion, they must register in 7 days in order to claim the money. If the money is not claimed, it gets transferred back to the sender. | 
**comment** | **str** | The comment of the money transfer. | 

## Example

```python
from clientapi_barion.models.transfer_email_request import TransferEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferEmailRequest from a JSON string
transfer_email_request_instance = TransferEmailRequest.from_json(json)
# print the JSON string representation of the object
print(TransferEmailRequest.to_json())

# convert the object into a dict
transfer_email_request_dict = transfer_email_request_instance.to_dict()
# create an instance of TransferEmailRequest from a dict
transfer_email_request_from_dict = TransferEmailRequest.from_dict(transfer_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


