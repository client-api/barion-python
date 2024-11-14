# BankDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**swift_code** | **str** | Required for IBAN transfers. SwiftCode of the recipient bank for international transfers.  | [optional] 

## Example

```python
from clientapi_barion.models.bank_details import BankDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BankDetails from a JSON string
bank_details_instance = BankDetails.from_json(json)
# print the JSON string representation of the object
print(BankDetails.to_json())

# convert the object into a dict
bank_details_dict = bank_details_instance.to_dict()
# create an instance of BankDetails from a dict
bank_details_from_dict = BankDetails.from_dict(bank_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


