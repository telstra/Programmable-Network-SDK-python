# TelstraTPN.VportsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_regularvport**](VportsApi.md#inventory_regularvport) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
[**inventory_vnf_vport**](VportsApi.md#inventory_vnf_vport) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
[**inventory_vport**](VportsApi.md#inventory_vport) | **GET** /1.0.0/inventory/vport/{vportuuid} | Get information about the specified VPort


# **inventory_regularvport**
> SuccessFragment inventory_regularvport(regvportrequest=regvportrequest)

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
regvportrequest = TelstraTPN.Regvportrequest() # Regvportrequest |  (optional)

try:
    # Create VPort for physical endpoint
    api_response = api_instance.inventory_regularvport(regvportrequest=regvportrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->inventory_regularvport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regvportrequest** | [**Regvportrequest**](Regvportrequest.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_vnf_vport**
> InlineResponse2008 inventory_vnf_vport(vportrequest=vportrequest)

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
vportrequest = TelstraTPN.Vportrequest() # Vportrequest |  (optional)

try:
    # Create VNF VPort
    api_response = api_instance.inventory_vnf_vport(vportrequest=vportrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->inventory_vnf_vport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vportrequest** | [**Vportrequest**](Vportrequest.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_vport**
> EndpointPort inventory_vport(vportuuid)

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
    api_response = api_instance.inventory_vport(vportuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->inventory_vport: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

