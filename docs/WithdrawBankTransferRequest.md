# WithdrawBankTransferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**Currency**](Currency.md) | Required. ISO 4217 currency code of the bank transfer. Barion does not perform currency conversion; ensure compatibility with recipient bank.  | 
**amount** | **float** | Total amount to withdraw, excluding fees. | 
**comment** | **str** | Comment associated with the bank transfer. | [optional] 
**bank_account** | [**BankAccountDetails**](BankAccountDetails.md) | Details of the recipient&#39;s bank account. | 
**bank** | [**BankDetails**](BankDetails.md) | Required for foreign withdrawals. Details of the recipient&#39;s bank. | 
**recipient** | [**RecipientDetails**](RecipientDetails.md) | Details of the recipient. | 

## Example

```python
from clientapi_barion.models.withdraw_bank_transfer_request import WithdrawBankTransferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WithdrawBankTransferRequest from a JSON string
withdraw_bank_transfer_request_instance = WithdrawBankTransferRequest.from_json(json)
# print the JSON string representation of the object
print(WithdrawBankTransferRequest.to_json())

# convert the object into a dict
withdraw_bank_transfer_request_dict = withdraw_bank_transfer_request_instance.to_dict()
# create an instance of WithdrawBankTransferRequest from a dict
withdraw_bank_transfer_request_from_dict = WithdrawBankTransferRequest.from_dict(withdraw_bank_transfer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


