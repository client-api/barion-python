# clientapi-barion
Integrate with ease and get unbeatable fees and data that helps you grow your business.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.1
- Package version: 0.1.1
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/client-api/barion-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/client-api/barion-python.git`)

Then import the package:
```python
import clientapi_barion
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import clientapi_barion
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    except ApiException as e:
        print("Exception when calling BarionSmartGatewayApi->get_payment_state_v2: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.barion.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BarionSmartGatewayApi* | [**get_payment_state_v2**](docs/BarionSmartGatewayApi.md#get_payment_state_v2) | **GET** /v2/Payment/GetPaymentState | Get Payment State
*BarionSmartGatewayApi* | [**get_payment_state_v4**](docs/BarionSmartGatewayApi.md#get_payment_state_v4) | **GET** /v4/Payment/{PaymentId}/PaymentState | Get the state of a payment
*BarionSmartGatewayApi* | [**payment_cancel_authorization_v2**](docs/BarionSmartGatewayApi.md#payment_cancel_authorization_v2) | **POST** /v2/Payment/CancelAuthorization | Cancel Authorization of a payment
*BarionSmartGatewayApi* | [**payment_capture_v2**](docs/BarionSmartGatewayApi.md#payment_capture_v2) | **POST** /v2/Payment/Capture | Capture of a payment
*BarionSmartGatewayApi* | [**payment_complete_v2**](docs/BarionSmartGatewayApi.md#payment_complete_v2) | **POST** /v2/Payment/Complete | Complete a payment
*BarionSmartGatewayApi* | [**payment_finish_reservation_v2**](docs/BarionSmartGatewayApi.md#payment_finish_reservation_v2) | **POST** /v2/Payment/FinishReservation | Finish a pending reservation
*BarionSmartGatewayApi* | [**payment_start_v2**](docs/BarionSmartGatewayApi.md#payment_start_v2) | **POST** /v2/Payment/Start | Create a new payment
*BarionSmartGatewayApi* | [**payment_start_with_google_token_v3**](docs/BarionSmartGatewayApi.md#payment_start_with_google_token_v3) | **POST** /v3/Payment/StartPaymentWithGoogleToken | Create a new payment
*BarionSmartGatewayApi* | [**refund_payment_v2**](docs/BarionSmartGatewayApi.md#refund_payment_v2) | **POST** /v2/Payment/Refund | Execute the refund of a payment
*BarionWalletApi* | [**get_accounts_v2**](docs/BarionWalletApi.md#get_accounts_v2) | **GET** /v2/Accounts | Get existing accounts of the user
*BarionWalletApi* | [**get_history_v3**](docs/BarionWalletApi.md#get_history_v3) | **GET** /v3/UserHistory/GetHistory | Get User Transaction History
*BarionWalletApi* | [**get_statement_download_v2**](docs/BarionWalletApi.md#get_statement_download_v2) | **GET** /v2/Statement/Download | Download statement file
*BarionWalletApi* | [**transfer_email_v2**](docs/BarionWalletApi.md#transfer_email_v2) | **POST** /v2/Transfer/Email | Send money to an e-mail address
*BarionWalletApi* | [**withdraw_bank_transfer_v3**](docs/BarionWalletApi.md#withdraw_bank_transfer_v3) | **POST** /v3/Withdraw/BankTransfer | Initiate Bank Transfer


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountInfo](docs/AccountInfo.md)
 - [AccountsResponse](docs/AccountsResponse.md)
 - [AccountsResponseWithErrorMessages](docs/AccountsResponseWithErrorMessages.md)
 - [Balance](docs/Balance.md)
 - [BankAccountDetails](docs/BankAccountDetails.md)
 - [BankCard](docs/BankCard.md)
 - [BankDetails](docs/BankDetails.md)
 - [Beneficiary](docs/Beneficiary.md)
 - [BillingAddress](docs/BillingAddress.md)
 - [CancelAuthorizationRequest](docs/CancelAuthorizationRequest.md)
 - [CancelAuthorizationResponse](docs/CancelAuthorizationResponse.md)
 - [CancelAuthorizationResponseWithErrorMessages](docs/CancelAuthorizationResponseWithErrorMessages.md)
 - [CapturePaymentRequest](docs/CapturePaymentRequest.md)
 - [CapturePaymentResponse](docs/CapturePaymentResponse.md)
 - [CapturePaymentResponseWithErrorMessages](docs/CapturePaymentResponseWithErrorMessages.md)
 - [DetailedPaymentTransaction](docs/DetailedPaymentTransaction.md)
 - [DetailedPaymentTransactionTransactionType](docs/DetailedPaymentTransactionTransactionType.md)
 - [Error](docs/Error.md)
 - [Errors](docs/Errors.md)
 - [FundingInformation](docs/FundingInformation.md)
 - [GetPaymentStateResponse](docs/GetPaymentStateResponse.md)
 - [GetPaymentStateResponseWithErrorMessages](docs/GetPaymentStateResponseWithErrorMessages.md)
 - [GetUserHistoryResponse](docs/GetUserHistoryResponse.md)
 - [GetUserHistoryResponseWithErrorMessages](docs/GetUserHistoryResponseWithErrorMessages.md)
 - [GiftCardPurchase](docs/GiftCardPurchase.md)
 - [Item](docs/Item.md)
 - [NameInformation](docs/NameInformation.md)
 - [PayeeTransaction](docs/PayeeTransaction.md)
 - [PayeeTransactionToFinish](docs/PayeeTransactionToFinish.md)
 - [PayerAccountInformation](docs/PayerAccountInformation.md)
 - [PaymentCompleteRequest](docs/PaymentCompleteRequest.md)
 - [PaymentCompleteResponse](docs/PaymentCompleteResponse.md)
 - [PaymentCompleteResponseWithErrorMessages](docs/PaymentCompleteResponseWithErrorMessages.md)
 - [PaymentFinishReservationRequest](docs/PaymentFinishReservationRequest.md)
 - [PaymentFinishReservationResponse](docs/PaymentFinishReservationResponse.md)
 - [PaymentFinishReservationResponseWithErrorMessages](docs/PaymentFinishReservationResponseWithErrorMessages.md)
 - [PaymentStartRequest](docs/PaymentStartRequest.md)
 - [PaymentStartRequestWithGoogleToken](docs/PaymentStartRequestWithGoogleToken.md)
 - [PaymentStartResponse](docs/PaymentStartResponse.md)
 - [PaymentStartResponseWithErrorMessages](docs/PaymentStartResponseWithErrorMessages.md)
 - [PaymentStartResponseWithGoogleTokenAndErrorMessages](docs/PaymentStartResponseWithGoogleTokenAndErrorMessages.md)
 - [PaymentStateResponse](docs/PaymentStateResponse.md)
 - [PaymentStateResponseWithErrorMessages](docs/PaymentStateResponseWithErrorMessages.md)
 - [PaymentTransaction](docs/PaymentTransaction.md)
 - [PaymentType](docs/PaymentType.md)
 - [ProcessedTransaction](docs/ProcessedTransaction.md)
 - [PurchaseInformation](docs/PurchaseInformation.md)
 - [PurchaseType](docs/PurchaseType.md)
 - [QRCodeSize](docs/QRCodeSize.md)
 - [RecipientAddress](docs/RecipientAddress.md)
 - [RecipientDetails](docs/RecipientDetails.md)
 - [RefundRequest](docs/RefundRequest.md)
 - [RefundResponse](docs/RefundResponse.md)
 - [RefundResponseWithErrorMessages](docs/RefundResponseWithErrorMessages.md)
 - [RefundedTransaction](docs/RefundedTransaction.md)
 - [ShippingAddress](docs/ShippingAddress.md)
 - [StartPaymentWithGoogleToken](docs/StartPaymentWithGoogleToken.md)
 - [StartPaymentWithGoogleTokenResponse](docs/StartPaymentWithGoogleTokenResponse.md)
 - [TransactionToFinish](docs/TransactionToFinish.md)
 - [TransactionToRefund](docs/TransactionToRefund.md)
 - [TransferEmailAmount](docs/TransferEmailAmount.md)
 - [TransferEmailRequest](docs/TransferEmailRequest.md)
 - [TransferEmailResponse](docs/TransferEmailResponse.md)
 - [TransferEmailResponseWithErrorMessages](docs/TransferEmailResponseWithErrorMessages.md)
 - [UserHistory](docs/UserHistory.md)
 - [UserHistoryParticipant](docs/UserHistoryParticipant.md)
 - [UserInformation](docs/UserInformation.md)
 - [WithdrawBankTransferRequest](docs/WithdrawBankTransferRequest.md)
 - [WithdrawBankTransferResponse](docs/WithdrawBankTransferResponse.md)
 - [WithdrawBankTransferResponseWithErrorMessages](docs/WithdrawBankTransferResponseWithErrorMessages.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header

<a id="PosKeyAuth"></a>
### PosKeyAuth

- **Type**: API key
- **API key parameter name**: x-pos-key
- **Location**: HTTP header


## Author




