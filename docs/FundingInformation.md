# FundingInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_card** | [**BankCard**](BankCard.md) |  | [optional] 
**authorization_code** | **str** | The authorization code received by the card processing system when executing the payment. If authorization was not successful, this is empty.  | [optional] 
**process_result** | **str** |  | [optional] 

## Example

```python
from clientapi_barion.models.funding_information import FundingInformation

# TODO update the JSON string below
json = "{}"
# create an instance of FundingInformation from a JSON string
funding_information_instance = FundingInformation.from_json(json)
# print the JSON string representation of the object
print(FundingInformation.to_json())

# convert the object into a dict
funding_information_dict = funding_information_instance.to_dict()
# create an instance of FundingInformation from a dict
funding_information_from_dict = FundingInformation.from_dict(funding_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


