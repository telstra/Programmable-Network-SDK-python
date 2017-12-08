# TelstraTPN.EndpointsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_physical__port_endpoint**](EndpointsApi.md#create_physical__port_endpoint) | **POST** /1.0.0/inventory/regularendpoint | Create Physical (Port) Endpoint
[**create_vnf_endpoint**](EndpointsApi.md#create_vnf_endpoint) | **POST** /1.0.0/inventory/vnfendpoint | Create VNF Endpoint
[**get_information_about_the_specified_endpoint**](EndpointsApi.md#get_information_about_the_specified_endpoint) | **GET** /1.0.0/inventory/endpoint/{endpointuuid} | Get information about the specified endpoint
[**get_list_of_endpoints_for_a_customer**](EndpointsApi.md#get_list_of_endpoints_for_a_customer) | **GET** /1.0.0/inventory/endpoints/customeruuid/{customeruuid} | Get list of endpoints for a customer


# **create_physical__port_endpoint**
> Model100InventoryRegularendpointResponse create_physical__port_endpoint(body=body)

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.EndpointsApi()
body = TelstraTPN.Model100InventoryRegularendpointRequest() # Model100InventoryRegularendpointRequest |  (optional)

try: 
    # Create Physical (Port) Endpoint
    api_response = api_instance.create_physical__port_endpoint(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->create_physical__port_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model100InventoryRegularendpointRequest**](Model100InventoryRegularendpointRequest.md)|  | [optional] 

### Return type

[**Model100InventoryRegularendpointResponse**](Model100InventoryRegularendpointResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vnf_endpoint**
> Model100InventoryVnfendpointResponse create_vnf_endpoint(body=body)

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.EndpointsApi()
body = TelstraTPN.Model100InventoryVnfendpointRequest() # Model100InventoryVnfendpointRequest |  (optional)

try: 
    # Create VNF Endpoint
    api_response = api_instance.create_vnf_endpoint(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->create_vnf_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model100InventoryVnfendpointRequest**](Model100InventoryVnfendpointRequest.md)|  | [optional] 

### Return type

[**Model100InventoryVnfendpointResponse**](Model100InventoryVnfendpointResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_information_about_the_specified_endpoint**
> Model100InventoryEndpointResponse get_information_about_the_specified_endpoint(endpointuuid)

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.EndpointsApi()
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint

try: 
    # Get information about the specified endpoint
    api_response = api_instance.get_information_about_the_specified_endpoint(endpointuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_information_about_the_specified_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 

### Return type

[**Model100InventoryEndpointResponse**](Model100InventoryEndpointResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_of_endpoints_for_a_customer**
> Model100InventoryEndpointsCustomeruuidResponse get_list_of_endpoints_for_a_customer(customeruuid)

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
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.EndpointsApi()
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try: 
    # Get list of endpoints for a customer
    api_response = api_instance.get_list_of_endpoints_for_a_customer(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->get_list_of_endpoints_for_a_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**Model100InventoryEndpointsCustomeruuidResponse**](Model100InventoryEndpointsCustomeruuidResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

