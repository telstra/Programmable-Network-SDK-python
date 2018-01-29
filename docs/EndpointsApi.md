# TelstraTPN.EndpointsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eis100_endpoint_endpointuuid_by_endpointuuid_put**](EndpointsApi.md#eis100_endpoint_endpointuuid_by_endpointuuid_put) | **PUT** /eis/1.0.0/endpoint/endpointuuid/{endpointuuid} | eisendpointendpointuuidendpointuuidput
[**eis100_endpoints_assign_topology_tag_by_endpointuuid_post**](EndpointsApi.md#eis100_endpoints_assign_topology_tag_by_endpointuuid_post) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | eisendpointsendpointuuidassigntopologytagpost
[**eis100_endpoints_topology_tag_uuid_by_topotaguuid_get**](EndpointsApi.md#eis100_endpoints_topology_tag_uuid_by_topotaguuid_get) | **GET** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid} | eisendpointstopologytaguuidtopotaguuidget
[**eis100_endpoints_topology_tag_uuid_endpoint_by_topotaguuid_and_endpointuuid_delete**](EndpointsApi.md#eis100_endpoints_topology_tag_uuid_endpoint_by_topotaguuid_and_endpointuuid_delete) | **DELETE** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid} | eisendpointstopologytaguuiddelete
[**inventory_endpoint_by_endpointuuid_get**](EndpointsApi.md#inventory_endpoint_by_endpointuuid_get) | **GET** /1.0.0/inventory/endpoint/{endpointuuid} | inventoryendpointendpointuuidget
[**inventory_endpoints_customeruuid_by_customeruuid_get**](EndpointsApi.md#inventory_endpoints_customeruuid_by_customeruuid_get) | **GET** /1.0.0/inventory/endpoints/customeruuid/{customeruuid} | inventoryendpointscustomeruuidcustomeruuidget
[**inventory_regularendpoint_post**](EndpointsApi.md#inventory_regularendpoint_post) | **POST** /1.0.0/inventory/regularendpoint | inventoryregularendpointpost
[**inventory_vnfendpoint_post**](EndpointsApi.md#inventory_vnfendpoint_post) | **POST** /1.0.0/inventory/vnfendpoint | inventoryvnfendpointpost


# **eis100_endpoint_endpointuuid_by_endpointuuid_put**
> SuccessFragment eis100_endpoint_endpointuuid_by_endpointuuid_put(endpointuuid, body=body)

eisendpointendpointuuidendpointuuidput

Update Endpoint name

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
body = TelstraTPN.Body67() # Body67 |  (optional)

try:
    # eisendpointendpointuuidendpointuuidput
    api_response = api_instance.eis100_endpoint_endpointuuid_by_endpointuuid_put(endpointuuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->eis100_endpoint_endpointuuid_by_endpointuuid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 
 **body** | [**Body67**](Body67.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eis100_endpoints_assign_topology_tag_by_endpointuuid_post**
> SuccessFragment eis100_endpoints_assign_topology_tag_by_endpointuuid_post(endpointuuid, body=body)

eisendpointsendpointuuidassigntopologytagpost

Assign an Endpoint to a Topology

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
body = TelstraTPN.Body71() # Body71 |  (optional)

try:
    # eisendpointsendpointuuidassigntopologytagpost
    api_response = api_instance.eis100_endpoints_assign_topology_tag_by_endpointuuid_post(endpointuuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->eis100_endpoints_assign_topology_tag_by_endpointuuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 
 **body** | [**Body71**](Body71.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eis100_endpoints_topology_tag_uuid_by_topotaguuid_get**
> EisendpointstopologytaguuidtopotaguuidgetResponse eis100_endpoints_topology_tag_uuid_by_topotaguuid_get(topotaguuid)

eisendpointstopologytaguuidtopotaguuidget

List all Endpoints associated with the topology tag.

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
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # eisendpointstopologytaguuidtopotaguuidget
    api_response = api_instance.eis100_endpoints_topology_tag_uuid_by_topotaguuid_get(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->eis100_endpoints_topology_tag_uuid_by_topotaguuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

[**EisendpointstopologytaguuidtopotaguuidgetResponse**](EisendpointstopologytaguuidtopotaguuidgetResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eis100_endpoints_topology_tag_uuid_endpoint_by_topotaguuid_and_endpointuuid_delete**
> eis100_endpoints_topology_tag_uuid_endpoint_by_topotaguuid_and_endpointuuid_delete(topotaguuid, endpointuuid)

eisendpointstopologytaguuiddelete

Remove Endpoint from a Topology

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
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint

try:
    # eisendpointstopologytaguuiddelete
    api_instance.eis100_endpoints_topology_tag_uuid_endpoint_by_topotaguuid_and_endpointuuid_delete(topotaguuid, endpointuuid)
except ApiException as e:
    print("Exception when calling EndpointsApi->eis100_endpoints_topology_tag_uuid_endpoint_by_topotaguuid_and_endpointuuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_endpoint_by_endpointuuid_get**
> InventoryendpointendpointuuidgetResponse inventory_endpoint_by_endpointuuid_get(endpointuuid)

inventoryendpointendpointuuidget

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
    # inventoryendpointendpointuuidget
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

[**InventoryendpointendpointuuidgetResponse**](InventoryendpointendpointuuidgetResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_endpoints_customeruuid_by_customeruuid_get**
> InventoryendpointscustomeruuidcustomeruuidgetResponse inventory_endpoints_customeruuid_by_customeruuid_get(customeruuid)

inventoryendpointscustomeruuidcustomeruuidget

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
    # inventoryendpointscustomeruuidcustomeruuidget
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

[**InventoryendpointscustomeruuidcustomeruuidgetResponse**](InventoryendpointscustomeruuidcustomeruuidgetResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_regularendpoint_post**
> InventoryregularendpointpostResponse inventory_regularendpoint_post(body=body)

inventoryregularendpointpost

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
body = TelstraTPN.Body51() # Body51 |  (optional)

try:
    # inventoryregularendpointpost
    api_response = api_instance.inventory_regularendpoint_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_regularendpoint_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body51**](Body51.md)|  | [optional] 

### Return type

[**InventoryregularendpointpostResponse**](InventoryregularendpointpostResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_vnfendpoint_post**
> InventoryvnfendpointpostResponse inventory_vnfendpoint_post(body=body)

inventoryvnfendpointpost

Instantiate Virtual Network Function

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
body = TelstraTPN.Body58() # Body58 |  (optional)

try:
    # inventoryvnfendpointpost
    api_response = api_instance.inventory_vnfendpoint_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventory_vnfendpoint_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body58**](Body58.md)|  | [optional] 

### Return type

[**InventoryvnfendpointpostResponse**](InventoryvnfendpointpostResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

