# TelstraTPN.EndpointsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**100_inventory_endpoint_by_endpointuuid_get**](EndpointsApi.md#100_inventory_endpoint_by_endpointuuid_get) | **GET** /1.0.0/inventory/endpoint/{endpointuuid} | Get information about the specified endpoint
[**100_inventory_endpoints_customeruuid_by_customeruuid_get**](EndpointsApi.md#100_inventory_endpoints_customeruuid_by_customeruuid_get) | **GET** /1.0.0/inventory/endpoints/customeruuid/{customeruuid} | Get list of endpoints for a customer
[**100_inventory_regularendpoint_post**](EndpointsApi.md#100_inventory_regularendpoint_post) | **POST** /1.0.0/inventory/regularendpoint | Create Physical (Port) Endpoint
[**100_inventory_vnfendpoint_post**](EndpointsApi.md#100_inventory_vnfendpoint_post) | **POST** /1.0.0/inventory/vnfendpoint | Create VNF Endpoint
[**eis100_endpoints_assign_topology_tag_by_endpointuuid_post**](EndpointsApi.md#eis100_endpoints_assign_topology_tag_by_endpointuuid_post) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | Assign a Topology Tag to an Endpoint


# **100_inventory_endpoint_by_endpointuuid_get**
> Model100InventoryEndpointResponse 100_inventory_endpoint_by_endpointuuid_get(endpointuuid)

Get information about the specified endpoint

Get information about the specified endpoint

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.EndpointsApi()
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint

try: 
    # Get information about the specified endpoint
    api_response = api_instance.100_inventory_endpoint_by_endpointuuid_get(endpointuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->100_inventory_endpoint_by_endpointuuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 

### Return type

[**Model100InventoryEndpointResponse**](Model100InventoryEndpointResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **100_inventory_endpoints_customeruuid_by_customeruuid_get**
> Model100InventoryEndpointsCustomeruuidResponse 100_inventory_endpoints_customeruuid_by_customeruuid_get(customeruuid)

Get list of endpoints for a customer

Get list of endpoints for a customer

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.EndpointsApi()
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try: 
    # Get list of endpoints for a customer
    api_response = api_instance.100_inventory_endpoints_customeruuid_by_customeruuid_get(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->100_inventory_endpoints_customeruuid_by_customeruuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**Model100InventoryEndpointsCustomeruuidResponse**](Model100InventoryEndpointsCustomeruuidResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **100_inventory_regularendpoint_post**
> Model100InventoryRegularendpointResponse 100_inventory_regularendpoint_post(body=body)

Create Physical (Port) Endpoint

Create Physical (Port) Endpoint

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.EndpointsApi()
body = TelstraTPN.Model100InventoryRegularendpointRequest() # Model100InventoryRegularendpointRequest |  (optional)

try: 
    # Create Physical (Port) Endpoint
    api_response = api_instance.100_inventory_regularendpoint_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->100_inventory_regularendpoint_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model100InventoryRegularendpointRequest**](Model100InventoryRegularendpointRequest.md)|  | [optional] 

### Return type

[**Model100InventoryRegularendpointResponse**](Model100InventoryRegularendpointResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **100_inventory_vnfendpoint_post**
> Model100InventoryVnfendpointResponse 100_inventory_vnfendpoint_post(body=body)

Create VNF Endpoint

Create VNF Endpoint

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.EndpointsApi()
body = TelstraTPN.Model100InventoryVnfendpointRequest() # Model100InventoryVnfendpointRequest |  (optional)

try: 
    # Create VNF Endpoint
    api_response = api_instance.100_inventory_vnfendpoint_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->100_inventory_vnfendpoint_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model100InventoryVnfendpointRequest**](Model100InventoryVnfendpointRequest.md)|  | [optional] 

### Return type

[**Model100InventoryVnfendpointResponse**](Model100InventoryVnfendpointResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eis100_endpoints_assign_topology_tag_by_endpointuuid_post**
> SuccessFragment eis100_endpoints_assign_topology_tag_by_endpointuuid_post(endpointuuid, body=body)

Assign a Topology Tag to an Endpoint

Assign a Topology Tag to an Endpoint

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.EndpointsApi()
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

[**SuccessFragment**](SuccessFragment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

