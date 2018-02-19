# TelstraTPN.VportsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventoryregularvportpost**](VportsApi.md#inventoryregularvportpost) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
[**inventoryvnfvportpost**](VportsApi.md#inventoryvnfvportpost) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
[**inventoryvportvportuuidget**](VportsApi.md#inventoryvportvportuuidget) | **GET** /1.0.0/inventory/vport/{vportuuid} | Get information about the specified VPort


# **inventoryregularvportpost**
> inventoryregularvportpost(body=body)

Create VPort for physical endpoint

Create VPort representing a VLAN on a Physical Ethernet Port

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
api_instance = TelstraTPN.VportsApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.Body5() # Body5 |  (optional)

try:
    # Create VPort for physical endpoint
    api_instance.inventoryregularvportpost(body=body)
except ApiException as e:
    print("Exception when calling VportsApi->inventoryregularvportpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body5**](Body5.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventoryvnfvportpost**
> InlineResponse2005 inventoryvnfvportpost(body=body)

Create VNF VPort

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
api_instance = TelstraTPN.VportsApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.Body6() # Body6 |  (optional)

try:
    # Create VNF VPort
    api_response = api_instance.inventoryvnfvportpost(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->inventoryvnfvportpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventoryvportvportuuidget**
> EndpointPort inventoryvportvportuuidget(vportuuid)

Get information about the specified VPort

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
api_instance = TelstraTPN.VportsApi(TelstraTPN.ApiClient(configuration))
vportuuid = 'vportuuid_example' # str | Unique identifier representing a specific virtual port

try:
    # Get information about the specified VPort
    api_response = api_instance.inventoryvportvportuuidget(vportuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->inventoryvportvportuuidget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vportuuid** | **str**| Unique identifier representing a specific virtual port | 

### Return type

[**EndpointPort**](EndpointPort.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

