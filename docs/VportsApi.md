# TelstraTPN.VportsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_regularvport_post**](VportsApi.md#inventory_regularvport_post) | **POST** /1.0.0/inventory/regularvport | inventoryregularvportpost
[**inventory_vnf_vport_post**](VportsApi.md#inventory_vnf_vport_post) | **POST** /1.0.0/inventory/vnf/vport | inventoryvnfvportpost
[**inventory_vport_by_vportuuid_get**](VportsApi.md#inventory_vport_by_vportuuid_get) | **GET** /1.0.0/inventory/vport/{vportuuid} | inventoryvportvportuuidget


# **inventory_regularvport_post**
> InventoryregularvportpostResponse inventory_regularvport_post(body=body)

inventoryregularvportpost

Create VPort representing a VLAN on a Physical Ethernet Port

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.VportsApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.Body53() # Body53 |  (optional)

try:
    # inventoryregularvportpost
    api_response = api_instance.inventory_regularvport_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->inventory_regularvport_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body53**](Body53.md)|  | [optional] 

### Return type

[**InventoryregularvportpostResponse**](InventoryregularvportpostResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_vnf_vport_post**
> InventoryvnfvportpostResponse inventory_vnf_vport_post(body=body)

inventoryvnfvportpost

Create VNF VPort

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.VportsApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.Body56() # Body56 |  (optional)

try:
    # inventoryvnfvportpost
    api_response = api_instance.inventory_vnf_vport_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->inventory_vnf_vport_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body56**](Body56.md)|  | [optional] 

### Return type

[**InventoryvnfvportpostResponse**](InventoryvnfvportpostResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_vport_by_vportuuid_get**
> EndpointPort inventory_vport_by_vportuuid_get(vportuuid)

inventoryvportvportuuidget

Get information about the specified VPort

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
configuration = TelstraTPN.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.VportsApi(TelstraTPN.ApiClient(configuration))
vportuuid = 'vportuuid_example' # str | Unique identifier representing a specific virtual port

try:
    # inventoryvportvportuuidget
    api_response = api_instance.inventory_vport_by_vportuuid_get(vportuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->inventory_vport_by_vportuuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vportuuid** | **str**| Unique identifier representing a specific virtual port | 

### Return type

[**EndpointPort**](EndpointPort.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

