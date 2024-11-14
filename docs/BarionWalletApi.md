# clientapi_barion.BarionWalletApi

All URIs are relative to *https://api.barion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_v2**](BarionWalletApi.md#get_accounts_v2) | **GET** /v2/Accounts | Get existing accounts of the user
[**get_history_v3**](BarionWalletApi.md#get_history_v3) | **GET** /v3/UserHistory/GetHistory | Get User Transaction History
[**get_statement_download_v2**](BarionWalletApi.md#get_statement_download_v2) | **GET** /v2/Statement/Download | Download statement file
[**transfer_email_v2**](BarionWalletApi.md#transfer_email_v2) | **POST** /v2/Transfer/Email | Send money to an e-mail address
[**withdraw_bank_transfer_v3**](BarionWalletApi.md#withdraw_bank_transfer_v3) | **POST** /v3/Withdraw/BankTransfer | Initiate Bank Transfer


# **get_accounts_v2**
> AccountsResponseWithErrorMessages get_accounts_v2()

Get existing accounts of the user

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.accounts_response_with_error_messages import AccountsResponseWithErrorMessages
from clientapi_barion.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.barion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_barion.Configuration(
    host = "https://api.barion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionWalletApi(api_client)

    try:
        # Get existing accounts of the user
        api_response = api_instance.get_accounts_v2()
        print("The response of BarionWalletApi->get_accounts_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionWalletApi->get_accounts_v2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountsResponseWithErrorMessages**](AccountsResponseWithErrorMessages.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response returning user&#39;s accounts |  -  |
**400** | Bad request. Invalid input parameters. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_v3**
> GetUserHistoryResponseWithErrorMessages get_history_v3(last_visible_item_id=last_visible_item_id, last_request_time=last_request_time, limit=limit, currency=currency)

Get User Transaction History

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.get_user_history_response_with_error_messages import GetUserHistoryResponseWithErrorMessages
from clientapi_barion.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.barion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_barion.Configuration(
    host = "https://api.barion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionWalletApi(api_client)
    last_visible_item_id = 'last_visible_item_id_example' # str | The identifier of the oldest transaction. Only transactions before the defined transaction will be included in the response. (optional)
    last_request_time = '2013-10-20T19:20:30+01:00' # datetime | The exact time of the last request. Only transactions after or at the defined request time will be included in the response. (optional)
    limit = 56 # int | The expected number of transactions in the response. Default is 20. (optional)
    currency = 'currency_example' # str | Optional. Currency of transactions to retrieve (ISO 4217 format). (optional)

    try:
        # Get User Transaction History
        api_response = api_instance.get_history_v3(last_visible_item_id=last_visible_item_id, last_request_time=last_request_time, limit=limit, currency=currency)
        print("The response of BarionWalletApi->get_history_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionWalletApi->get_history_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_visible_item_id** | **str**| The identifier of the oldest transaction. Only transactions before the defined transaction will be included in the response. | [optional] 
 **last_request_time** | **datetime**| The exact time of the last request. Only transactions after or at the defined request time will be included in the response. | [optional] 
 **limit** | **int**| The expected number of transactions in the response. Default is 20. | [optional] 
 **currency** | **str**| Optional. Currency of transactions to retrieve (ISO 4217 format). | [optional] 

### Return type

[**GetUserHistoryResponseWithErrorMessages**](GetUserHistoryResponseWithErrorMessages.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response returning transaction history |  -  |
**400** | Bad request. Invalid input parameters. |  -  |
**404** | Not found. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement_download_v2**
> bytearray get_statement_download_v2(year, month, currency, day=day)

Download statement file

The `/statement/download` API endpoint is used to download monthly or daily statement files generated by the Barion system. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import clientapi_barion
from clientapi_barion.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.barion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_barion.Configuration(
    host = "https://api.barion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionWalletApi(api_client)
    year = 56 # int | The statement year.
    month = 56 # int | The statement month.
    currency = 'currency_example' # str | The currency of the statement's account. Accounts with separate currencies have separate statement files. If the user doesn't have an account in the specified currency, the API returns an error message with an HTTP 400 Bad request status code. 
    day = 56 # int | The statement day. If specified, the system will serve a daily statement file.  Otherwise, a monthly statement is returned.   **IMPORTANT:** Daily statements are only available if you explicitly request them from Barion customer service.  (optional)

    try:
        # Download statement file
        api_response = api_instance.get_statement_download_v2(year, month, currency, day=day)
        print("The response of BarionWalletApi->get_statement_download_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionWalletApi->get_statement_download_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**| The statement year. | 
 **month** | **int**| The statement month. | 
 **currency** | **str**| The currency of the statement&#39;s account. Accounts with separate currencies have separate statement files. If the user doesn&#39;t have an account in the specified currency, the API returns an error message with an HTTP 400 Bad request status code.  | 
 **day** | **int**| The statement day. If specified, the system will serve a daily statement file.  Otherwise, a monthly statement is returned.   **IMPORTANT:** Daily statements are only available if you explicitly request them from Barion customer service.  | [optional] 

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Depending on whether a day parameter was passed, the endpoint responds with one of the following outputs: - if a day parameter was passed, an .xlsx-format daily statement with an XML digital signature (signed by \&quot;Barion Payments Zrt\&quot;, certified by an external issuer) to guarantee data integrity; - if no day parameter was passed, a PDF-format monthly statement.  |  -  |
**400** | Bad request. The user doesn&#39;t have an account in the specified currency. |  -  |
**404** | Not found. The requested statement is not found. |  -  |
**403** | Forbidden. The requested statement type(daily/monthly) is unavailable. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_email_v2**
> TransferEmailResponseWithErrorMessages transfer_email_v2(transfer_email_request)

Send money to an e-mail address

The `/transfer/email` API endpoint is used to send money to another Barion Wallet. 

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.transfer_email_request import TransferEmailRequest
from clientapi_barion.models.transfer_email_response_with_error_messages import TransferEmailResponseWithErrorMessages
from clientapi_barion.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.barion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_barion.Configuration(
    host = "https://api.barion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionWalletApi(api_client)
    transfer_email_request = clientapi_barion.TransferEmailRequest() # TransferEmailRequest | 

    try:
        # Send money to an e-mail address
        api_response = api_instance.transfer_email_v2(transfer_email_request)
        print("The response of BarionWalletApi->transfer_email_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionWalletApi->transfer_email_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_email_request** | [**TransferEmailRequest**](TransferEmailRequest.md)|  | 

### Return type

[**TransferEmailResponseWithErrorMessages**](TransferEmailResponseWithErrorMessages.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request completed |  -  |
**400** | Bad request. The user doesn&#39;t have an account in the specified currency. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_bank_transfer_v3**
> WithdrawBankTransferResponseWithErrorMessages withdraw_bank_transfer_v3(withdraw_bank_transfer_request)

Initiate Bank Transfer

Initiate a bank transfer from Barion Wallet via POST request

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.withdraw_bank_transfer_request import WithdrawBankTransferRequest
from clientapi_barion.models.withdraw_bank_transfer_response_with_error_messages import WithdrawBankTransferResponseWithErrorMessages
from clientapi_barion.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.barion.com
# See configuration.py for a list of all supported configuration parameters.
configuration = clientapi_barion.Configuration(
    host = "https://api.barion.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionWalletApi(api_client)
    withdraw_bank_transfer_request = clientapi_barion.WithdrawBankTransferRequest() # WithdrawBankTransferRequest | 

    try:
        # Initiate Bank Transfer
        api_response = api_instance.withdraw_bank_transfer_v3(withdraw_bank_transfer_request)
        print("The response of BarionWalletApi->withdraw_bank_transfer_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionWalletApi->withdraw_bank_transfer_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **withdraw_bank_transfer_request** | [**WithdrawBankTransferRequest**](WithdrawBankTransferRequest.md)|  | 

### Return type

[**WithdrawBankTransferResponseWithErrorMessages**](WithdrawBankTransferResponseWithErrorMessages.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful bank transfer initiation response |  -  |
**400** | Bad request. Invalid input parameters. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

