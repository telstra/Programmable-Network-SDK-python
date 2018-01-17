# TelstraTPN.EndpointsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eis100_endpoints_assign_topology_tag_by_endpointuuid_post**](EndpointsApi.md#eis100_endpoints_assign_topology_tag_by_endpointuuid_post) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | Assign a Topology Tag to an Endpoint
[**inventory_endpoint_by_endpointuuid_get**](EndpointsApi.md#inventory_endpoint_by_endpointuuid_get) | **GET** /1.0.0/inventory/endpoint/{endpointuuid} | Get information about the specified endpoint
[**inventory_endpoints_customeruuid_by_customeruuid_get**](EndpointsApi.md#inventory_endpoints_customeruuid_by_customeruuid_get) | **GET** /1.0.0/inventory/endpoints/customeruuid/{customeruuid} | Get list of endpoints for a customer
[**inventory_regularendpoint_post**](EndpointsApi.md#inventory_regularendpoint_post) | **POST** /1.0.0/inventory/regularendpoint | Create Physical (Port) Endpoint
[**inventory_vnfendpoint_post**](EndpointsApi.md#inventory_vnfendpoint_post) | **POST** /1.0.0/inventory/vnfendpoint | Create VNF Endpoint


# **eis100_endpoints_assign_topology_tag_by_endpointuuid_post**
> list[SuccessFragment] eis100_endpoints_assign_topology_tag_by_endpointuuid_post(endpointuuid, body=body)

Assign a Topology Tag to an Endpoint

Assign a Topology Tag to an Endpoint

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint
body = TelstraTPN.Eis100EndpointsAssignTopologyTagRequest() # Eis100EndpointsAssignTopologyTagRequest |  (optional)

try:
    # Assign a Topology Tag to an Endpoint
    api_response = api_instance.eis100_endpoints_assign_topology_tag_by_endpointuuid_post(endpointuuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->eis100_endpoints_assign_topology_tag_by_endpointuuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 
 **body** | [**Eis100EndpointsAssignTopologyTagRequest**](Eis100EndpointsAssignTopologyTagRequest.md)|  | [optional] 

### Return type

[**list[SuccessFragment]**](SuccessFragment.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_endpoint_by_endpointuuid_get**
> InventoryEndpointResponse inventory_endpoint_by_endpointuuid_get(endpointuuid)

Get information about the specified endpoint

Get information about the specified endpoint

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint

try:
    # Get information about the specified endpoint
    api_response = api_instance.inventory_endpoint_by_endpointuuid_get(endpointuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_endpoint_by_endpointuuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 

### Return type

[**InventoryEndpointResponse**](InventoryEndpointResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_endpoints_customeruuid_by_customeruuid_get**
> InventoryEndpointsCustomeruuidResponse inventory_endpoints_customeruuid_by_customeruuid_get(customeruuid)

Get list of endpoints for a customer

Get list of endpoints for a customer

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try:
    # Get list of endpoints for a customer
    api_response = api_instance.inventory_endpoints_customeruuid_by_customeruuid_get(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_endpoints_customeruuid_by_customeruuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**InventoryEndpointsCustomeruuidResponse**](InventoryEndpointsCustomeruuidResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_regularendpoint_post**
> list[InventoryRegularendpointResponse] inventory_regularendpoint_post(body=body)

Create Physical (Port) Endpoint

Create Physical (Port) Endpoint

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.InventoryRegularendpointRequest() # InventoryRegularendpointRequest |  (optional)

try:
    # Create Physical (Port) Endpoint
    api_response = api_instance.inventory_regularendpoint_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_regularendpoint_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryRegularendpointRequest**](InventoryRegularendpointRequest.md)|  | [optional] 

### Return type

[**list[InventoryRegularendpointResponse]**](InventoryRegularendpointResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_vnfendpoint_post**
> list[InventoryVnfendpointResponse] inventory_vnfendpoint_post(body=body)

Create VNF Endpoint

Create VNF Endpoint

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.InventoryVnfendpointRequest() # InventoryVnfendpointRequest |  (optional)

try:
    # Create VNF Endpoint
    api_response = api_instance.inventory_vnfendpoint_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_vnfendpoint_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InventoryVnfendpointRequest**](InventoryVnfendpointRequest.md)|  | [optional] 

### Return type

[**list[InventoryVnfendpointResponse]**](InventoryVnfendpointResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

