# TelstraTPN.ExchangeApi

All URIs are relative to *https://penapi.pacnetconnect.com/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_profile_exchange_get**](ExchangeApi.md#account_profile_exchange_get) | **GET** /account/profile/exchange/ | Get the current account&#39;s Exchange profile
[**exchange_exprovuuid_get**](ExchangeApi.md#exchange_exprovuuid_get) | **GET** /exchange/{exprovuuid}/ | Exchange provider details
[**exchange_get**](ExchangeApi.md#exchange_get) | **GET** /exchange/ | List all Exchange providers, with POPs
[**visitcard_get**](ExchangeApi.md#visitcard_get) | **GET** /visitcard/ | Get list of Visit Cards
[**visitcard_visitcarduuid_get**](ExchangeApi.md#visitcard_visitcarduuid_get) | **GET** /visitcard/{visitcarduuid}/ | View details of the specified Visit Card
[**visitcard_visitcarduuid_put**](ExchangeApi.md#visitcard_visitcarduuid_put) | **PUT** /visitcard/{visitcarduuid}/ | Update details of the specified Visit Card


# **account_profile_exchange_get**
> InlineResponse20012 account_profile_exchange_get()

Get the current account's Exchange profile

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.ExchangeApi(TelstraTPN.ApiClient(configuration))

try:
    # Get the current account's Exchange profile
    api_response = api_instance.account_profile_exchange_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeApi->account_profile_exchange_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_exprovuuid_get**
> ExchangeProvider exchange_exprovuuid_get(exprovuuid)

Exchange provider details

Get information about the specified Exchange provider

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.ExchangeApi(TelstraTPN.ApiClient(configuration))
exprovuuid = 'exprovuuid_example' # str | Unique identifier representing a specific exchange provider

try:
    # Exchange provider details
    api_response = api_instance.exchange_exprovuuid_get(exprovuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeApi->exchange_exprovuuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exprovuuid** | **str**| Unique identifier representing a specific exchange provider | 

### Return type

[**ExchangeProvider**](ExchangeProvider.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_get**
> list[ExchangeProvider] exchange_get()

List all Exchange providers, with POPs

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.ExchangeApi(TelstraTPN.ApiClient(configuration))

try:
    # List all Exchange providers, with POPs
    api_response = api_instance.exchange_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeApi->exchange_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ExchangeProvider]**](ExchangeProvider.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visitcard_get**
> list[Visitcard] visitcard_get()

Get list of Visit Cards

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.ExchangeApi(TelstraTPN.ApiClient(configuration))

try:
    # Get list of Visit Cards
    api_response = api_instance.visitcard_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeApi->visitcard_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Visitcard]**](Visitcard.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visitcard_visitcarduuid_get**
> Visitcard visitcard_visitcarduuid_get(visitcarduuid)

View details of the specified Visit Card

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.ExchangeApi(TelstraTPN.ApiClient(configuration))
visitcarduuid = 'visitcarduuid_example' # str | Unique identifier representing a specific exchange visit card (provider description)

try:
    # View details of the specified Visit Card
    api_response = api_instance.visitcard_visitcarduuid_get(visitcarduuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeApi->visitcard_visitcarduuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visitcarduuid** | **str**| Unique identifier representing a specific exchange visit card (provider description) | 

### Return type

[**Visitcard**](Visitcard.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **visitcard_visitcarduuid_put**
> Visitcard visitcard_visitcarduuid_put(visitcarduuid, unknown_base_type=unknown_base_type)

Update details of the specified Visit Card

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oAuth2
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.ExchangeApi(TelstraTPN.ApiClient(configuration))
visitcarduuid = 'visitcarduuid_example' # str | Unique identifier representing a specific exchange visit card (provider description)
unknown_base_type = TelstraTPN.UNKNOWN_BASE_TYPE() # Visitcard |  (optional)

try:
    # Update details of the specified Visit Card
    api_response = api_instance.visitcard_visitcarduuid_put(visitcarduuid, unknown_base_type=unknown_base_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExchangeApi->visitcard_visitcarduuid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visitcarduuid** | **str**| Unique identifier representing a specific exchange visit card (provider description) | 
 **unknown_base_type** | [**Visitcard**](UNKNOWN_BASE_TYPE.md)|  | [optional] 

### Return type

[**Visitcard**](Visitcard.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

