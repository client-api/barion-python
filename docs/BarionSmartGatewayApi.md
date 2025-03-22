# clientapi_barion.BarionSmartGatewayApi

All URIs are relative to *https://api.barion.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_state_v2**](BarionSmartGatewayApi.md#get_payment_state_v2) | **GET** /v2/Payment/GetPaymentState | Get Payment State
[**get_payment_state_v4**](BarionSmartGatewayApi.md#get_payment_state_v4) | **GET** /v4/Payment/{PaymentId}/PaymentState | Get the state of a payment
[**payment_cancel_authorization_v2**](BarionSmartGatewayApi.md#payment_cancel_authorization_v2) | **POST** /v2/Payment/CancelAuthorization | Cancel Authorization of a payment
[**payment_capture_v2**](BarionSmartGatewayApi.md#payment_capture_v2) | **POST** /v2/Payment/Capture | Capture of a payment
[**payment_complete_v2**](BarionSmartGatewayApi.md#payment_complete_v2) | **POST** /v2/Payment/Complete | Complete a payment
[**payment_finish_reservation_v2**](BarionSmartGatewayApi.md#payment_finish_reservation_v2) | **POST** /v2/Payment/FinishReservation | Finish a pending reservation
[**payment_start_v2**](BarionSmartGatewayApi.md#payment_start_v2) | **POST** /v2/Payment/Start | Create a new payment
[**payment_start_with_google_token_v3**](BarionSmartGatewayApi.md#payment_start_with_google_token_v3) | **POST** /v3/Payment/StartPaymentWithGoogleToken | Create a new payment
[**refund_payment_v2**](BarionSmartGatewayApi.md#refund_payment_v2) | **POST** /v2/Payment/Refund | Execute the refund of a payment


# **get_payment_state_v2**
> GetPaymentStateResponseWithErrorMessages get_payment_state_v2(payment_id)

Get Payment State

### Example

* Api Key Authentication (PosKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.get_payment_state_response_with_error_messages import GetPaymentStateResponseWithErrorMessages
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

# Configure API key authorization: PosKeyAuth
configuration.api_key['PosKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PosKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionSmartGatewayApi(api_client)
    payment_id = '123e4567-e89b-12d3-a456-426614174001' # str | The identifier of the payment in the Barion system.

    try:
        # Get Payment State
        api_response = api_instance.get_payment_state_v2(payment_id)
        print("The response of BarionSmartGatewayApi->get_payment_state_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionSmartGatewayApi->get_payment_state_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| The identifier of the payment in the Barion system. | 

### Return type

[**GetPaymentStateResponseWithErrorMessages**](GetPaymentStateResponseWithErrorMessages.md)

### Authorization

[PosKeyAuth](../README.md#PosKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response returning payment state details |  -  |
**400** | Invalid input, object invalid. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |
**429** | Too many request To prevent potential disruptions in our service caused by the abuse of the [/v4/Payment/&lt;PaymentId&gt;/PaymentState](https://docs.barion.com/Payment-PaymentState-v4) API endpoint, we have introduced a rate-limiting feature to throttle excessive requests. **Generally, you should rely on the callback mechanism whenever possible unless you have a specific reason not to**, but if you want to manually get the details of a payment, here are a couple of things to bear in mind: - Make sure you do not send continuous requests for the same payment even if you need to get its current state manually without waiting for the callback to happen - Do not keep requesting for an indefinite time, even if your requests are throttled (e.g. if a problem occurs during the payment process, and the callback never happens, you shouldn&#39;t keep polling the API indefinitely) In this case the frequency is not the problem, but as time passes these orphan requests can cause a great load together To avoid these situations, the following throttling logic is implemented on our API:   - During a 5 seconds window we only accept the first 2 [/v4/Payment/&lt;PaymentId&gt;/PaymentState](https://docs.barion.com/Payment-PaymentState-v4) requests with the same payment ID. This means that if you submit two requests less than 5 seconds apart, subsequent requests will be denied until 5 seconds pass after the initial successful request. These requests will return with an HTTP 429 \&quot;Too many requests\&quot; error.  - We keep track of requests, and if requests with the same payment ID reach a certain limit during a specific timeframe, all further requests will return HTTP 429. The exact timeframe and limits are not disclosed to the public.  To reinforce the points above, we recommend using the callback mechanism described above, and calling the [/v4/Payment/&lt;PaymentId&gt;/PaymentState](https://docs.barion.com/Payment-PaymentState-v4) API endpoint only when there&#39;s a reason to do so. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_state_v4**
> PaymentStateResponseWithErrorMessages get_payment_state_v4(payment_id)

Get the state of a payment

Retrieves the state of a payment from the Barion system.

### Example

* Api Key Authentication (PosKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.payment_state_response_with_error_messages import PaymentStateResponseWithErrorMessages
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

# Configure API key authorization: PosKeyAuth
configuration.api_key['PosKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PosKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionSmartGatewayApi(api_client)
    payment_id = 'payment_id_example' # str | The identifier of the payment in the Barion system.

    try:
        # Get the state of a payment
        api_response = api_instance.get_payment_state_v4(payment_id)
        print("The response of BarionSmartGatewayApi->get_payment_state_v4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionSmartGatewayApi->get_payment_state_v4: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| The identifier of the payment in the Barion system. | 

### Return type

[**PaymentStateResponseWithErrorMessages**](PaymentStateResponseWithErrorMessages.md)

### Authorization

[PosKeyAuth](../README.md#PosKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request. Invalid input parameters. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |
**429** | Too many request To prevent potential disruptions in our service caused by the abuse of the [/v4/Payment/&lt;PaymentId&gt;/PaymentState](https://docs.barion.com/Payment-PaymentState-v4) API endpoint, we have introduced a rate-limiting feature to throttle excessive requests. **Generally, you should rely on the callback mechanism whenever possible unless you have a specific reason not to**, but if you want to manually get the details of a payment, here are a couple of things to bear in mind: - Make sure you do not send continuous requests for the same payment even if you need to get its current state manually without waiting for the callback to happen - Do not keep requesting for an indefinite time, even if your requests are throttled (e.g. if a problem occurs during the payment process, and the callback never happens, you shouldn&#39;t keep polling the API indefinitely) In this case the frequency is not the problem, but as time passes these orphan requests can cause a great load together To avoid these situations, the following throttling logic is implemented on our API:   - During a 5 seconds window we only accept the first 2 [/v4/Payment/&lt;PaymentId&gt;/PaymentState](https://docs.barion.com/Payment-PaymentState-v4) requests with the same payment ID. This means that if you submit two requests less than 5 seconds apart, subsequent requests will be denied until 5 seconds pass after the initial successful request. These requests will return with an HTTP 429 \&quot;Too many requests\&quot; error.  - We keep track of requests, and if requests with the same payment ID reach a certain limit during a specific timeframe, all further requests will return HTTP 429. The exact timeframe and limits are not disclosed to the public.  To reinforce the points above, we recommend using the callback mechanism described above, and calling the [/v4/Payment/&lt;PaymentId&gt;/PaymentState](https://docs.barion.com/Payment-PaymentState-v4) API endpoint only when there&#39;s a reason to do so. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_cancel_authorization_v2**
> CancelAuthorizationResponseWithErrorMessages payment_cancel_authorization_v2(cancel_authorization_request)

Cancel Authorization of a payment

### Example

* Api Key Authentication (PosKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.cancel_authorization_request import CancelAuthorizationRequest
from clientapi_barion.models.cancel_authorization_response_with_error_messages import CancelAuthorizationResponseWithErrorMessages
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

# Configure API key authorization: PosKeyAuth
configuration.api_key['PosKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PosKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionSmartGatewayApi(api_client)
    cancel_authorization_request = clientapi_barion.CancelAuthorizationRequest() # CancelAuthorizationRequest | 

    try:
        # Cancel Authorization of a payment
        api_response = api_instance.payment_cancel_authorization_v2(cancel_authorization_request)
        print("The response of BarionSmartGatewayApi->payment_cancel_authorization_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionSmartGatewayApi->payment_cancel_authorization_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_authorization_request** | [**CancelAuthorizationRequest**](CancelAuthorizationRequest.md)|  | 

### Return type

[**CancelAuthorizationResponseWithErrorMessages**](CancelAuthorizationResponseWithErrorMessages.md)

### Authorization

[PosKeyAuth](../README.md#PosKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful cancel authorization response |  -  |
**400** | Bad request. Invalid input parameters. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_capture_v2**
> CapturePaymentResponseWithErrorMessages payment_capture_v2(capture_payment_request)

Capture of a payment

### Example

* Api Key Authentication (PosKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.capture_payment_request import CapturePaymentRequest
from clientapi_barion.models.capture_payment_response_with_error_messages import CapturePaymentResponseWithErrorMessages
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

# Configure API key authorization: PosKeyAuth
configuration.api_key['PosKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PosKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionSmartGatewayApi(api_client)
    capture_payment_request = clientapi_barion.CapturePaymentRequest() # CapturePaymentRequest | 

    try:
        # Capture of a payment
        api_response = api_instance.payment_capture_v2(capture_payment_request)
        print("The response of BarionSmartGatewayApi->payment_capture_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionSmartGatewayApi->payment_capture_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **capture_payment_request** | [**CapturePaymentRequest**](CapturePaymentRequest.md)|  | 

### Return type

[**CapturePaymentResponseWithErrorMessages**](CapturePaymentResponseWithErrorMessages.md)

### Authorization

[PosKeyAuth](../README.md#PosKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful capture response |  -  |
**400** | Bad request. Invalid input parameters. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_complete_v2**
> PaymentCompleteResponseWithErrorMessages payment_complete_v2(payment_complete_request)

Complete a payment

This used to complete a formerly prepared and 3DS authenticated payment in the Barion system.

### Example

* Api Key Authentication (PosKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.payment_complete_request import PaymentCompleteRequest
from clientapi_barion.models.payment_complete_response_with_error_messages import PaymentCompleteResponseWithErrorMessages
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

# Configure API key authorization: PosKeyAuth
configuration.api_key['PosKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PosKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionSmartGatewayApi(api_client)
    payment_complete_request = clientapi_barion.PaymentCompleteRequest() # PaymentCompleteRequest | 

    try:
        # Complete a payment
        api_response = api_instance.payment_complete_v2(payment_complete_request)
        print("The response of BarionSmartGatewayApi->payment_complete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionSmartGatewayApi->payment_complete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_complete_request** | [**PaymentCompleteRequest**](PaymentCompleteRequest.md)|  | 

### Return type

[**PaymentCompleteResponseWithErrorMessages**](PaymentCompleteResponseWithErrorMessages.md)

### Authorization

[PosKeyAuth](../README.md#PosKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful completion response |  -  |
**400** | Bad request. Invalid input parameters. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_finish_reservation_v2**
> PaymentFinishReservationResponseWithErrorMessages payment_finish_reservation_v2(payment_finish_reservation_request)

Finish a pending reservation

### Example

* Api Key Authentication (PosKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.payment_finish_reservation_request import PaymentFinishReservationRequest
from clientapi_barion.models.payment_finish_reservation_response_with_error_messages import PaymentFinishReservationResponseWithErrorMessages
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

# Configure API key authorization: PosKeyAuth
configuration.api_key['PosKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PosKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionSmartGatewayApi(api_client)
    payment_finish_reservation_request = clientapi_barion.PaymentFinishReservationRequest() # PaymentFinishReservationRequest | 

    try:
        # Finish a pending reservation
        api_response = api_instance.payment_finish_reservation_v2(payment_finish_reservation_request)
        print("The response of BarionSmartGatewayApi->payment_finish_reservation_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionSmartGatewayApi->payment_finish_reservation_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_finish_reservation_request** | [**PaymentFinishReservationRequest**](PaymentFinishReservationRequest.md)|  | 

### Return type

[**PaymentFinishReservationResponseWithErrorMessages**](PaymentFinishReservationResponseWithErrorMessages.md)

### Authorization

[PosKeyAuth](../README.md#PosKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful completion response |  -  |
**400** | Bad request. Invalid input parameters. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_start_v2**
> PaymentStartResponseWithErrorMessages payment_start_v2(payment_start_request)

Create a new payment

This endpoint is used to create a new payment in the Barion system. If 3DS-related properties are provided, the chance of avoiding the challenge flow is increased. If not, the payer may have a higher chance of getting a challenge during payment.


### Example

* Api Key Authentication (PosKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.payment_start_request import PaymentStartRequest
from clientapi_barion.models.payment_start_response_with_error_messages import PaymentStartResponseWithErrorMessages
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

# Configure API key authorization: PosKeyAuth
configuration.api_key['PosKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PosKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionSmartGatewayApi(api_client)
    payment_start_request = clientapi_barion.PaymentStartRequest() # PaymentStartRequest | 

    try:
        # Create a new payment
        api_response = api_instance.payment_start_v2(payment_start_request)
        print("The response of BarionSmartGatewayApi->payment_start_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionSmartGatewayApi->payment_start_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_start_request** | [**PaymentStartRequest**](PaymentStartRequest.md)|  | 

### Return type

[**PaymentStartResponseWithErrorMessages**](PaymentStartResponseWithErrorMessages.md)

### Authorization

[PosKeyAuth](../README.md#PosKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment successfully created. |  -  |
**400** | Invalid input, object invalid. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_start_with_google_token_v3**
> PaymentStartResponseWithGoogleTokenAndErrorMessages payment_start_with_google_token_v3(payment_start_request_with_google_token)

Create a new payment

This endpoint is used to create a new payment in the Barion system. If 3DS-related properties are provided, the chance of avoiding the challenge flow is increased. If not, the payer may have a higher chance of getting a challenge during payment.


### Example

* Api Key Authentication (PosKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.payment_start_request_with_google_token import PaymentStartRequestWithGoogleToken
from clientapi_barion.models.payment_start_response_with_google_token_and_error_messages import PaymentStartResponseWithGoogleTokenAndErrorMessages
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

# Configure API key authorization: PosKeyAuth
configuration.api_key['PosKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PosKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionSmartGatewayApi(api_client)
    payment_start_request_with_google_token = clientapi_barion.PaymentStartRequestWithGoogleToken() # PaymentStartRequestWithGoogleToken | 

    try:
        # Create a new payment
        api_response = api_instance.payment_start_with_google_token_v3(payment_start_request_with_google_token)
        print("The response of BarionSmartGatewayApi->payment_start_with_google_token_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionSmartGatewayApi->payment_start_with_google_token_v3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_start_request_with_google_token** | [**PaymentStartRequestWithGoogleToken**](PaymentStartRequestWithGoogleToken.md)|  | 

### Return type

[**PaymentStartResponseWithGoogleTokenAndErrorMessages**](PaymentStartResponseWithGoogleTokenAndErrorMessages.md)

### Authorization

[PosKeyAuth](../README.md#PosKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment successfully created. |  -  |
**400** | Invalid input, object invalid. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_payment_v2**
> RefundResponseWithErrorMessages refund_payment_v2(refund_request)

Execute the refund of a payment

### Example

* Api Key Authentication (PosKeyAuth):

```python
import clientapi_barion
from clientapi_barion.models.refund_request import RefundRequest
from clientapi_barion.models.refund_response_with_error_messages import RefundResponseWithErrorMessages
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

# Configure API key authorization: PosKeyAuth
configuration.api_key['PosKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PosKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with clientapi_barion.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clientapi_barion.BarionSmartGatewayApi(api_client)
    refund_request = clientapi_barion.RefundRequest() # RefundRequest | 

    try:
        # Execute the refund of a payment
        api_response = api_instance.refund_payment_v2(refund_request)
        print("The response of BarionSmartGatewayApi->refund_payment_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BarionSmartGatewayApi->refund_payment_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_request** | [**RefundRequest**](RefundRequest.md)|  | 

### Return type

[**RefundResponseWithErrorMessages**](RefundResponseWithErrorMessages.md)

### Authorization

[PosKeyAuth](../README.md#PosKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refund successful |  -  |
**400** | Invalid input, object invalid. |  -  |
**401** | Unauthorized. Invalid API key. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

