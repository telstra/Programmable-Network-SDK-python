# TelstraTPN.EndpointsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eisendpointendpointuuidendpointuuidput**](EndpointsApi.md#eisendpointendpointuuidendpointuuidput) | **PUT** /eis/1.0.0/endpoint/endpointuuid/{endpointuuid} | Update Endpoint name
[**eisendpointsendpointuuidassigntopologytagpost**](EndpointsApi.md#eisendpointsendpointuuidassigntopologytagpost) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | Assign an Endpoint to a Topology
[**eisendpointstopologytaguuiddelete**](EndpointsApi.md#eisendpointstopologytaguuiddelete) | **DELETE** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid} | Remove Endpoint from a Topology
[**eisendpointstopologytaguuidtopotaguuidget**](EndpointsApi.md#eisendpointstopologytaguuidtopotaguuidget) | **GET** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid} | List Endpoints for Topology
[**inventoryendpointendpointuuidget**](EndpointsApi.md#inventoryendpointendpointuuidget) | **GET** /1.0.0/inventory/endpoint/{endpointuuid} | Get information about the specified endpoint
[**inventoryendpointscustomeruuidcustomeruuidget**](EndpointsApi.md#inventoryendpointscustomeruuidcustomeruuidget) | **GET** /1.0.0/inventory/endpoints/customeruuid/{customeruuid} | Get list of endpoints for a customer
[**inventoryregularendpointpost**](EndpointsApi.md#inventoryregularendpointpost) | **POST** /1.0.0/inventory/regularendpoint | Create Physical (Port) Endpoint
[**inventoryregularvportpost**](EndpointsApi.md#inventoryregularvportpost) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
[**inventoryvnfendpointpost**](EndpointsApi.md#inventoryvnfendpointpost) | **POST** /1.0.0/inventory/vnfendpoint | Instantiate Virtual Network Function


# **eisendpointendpointuuidendpointuuidput**
> SuccessFragment eisendpointendpointuuidendpointuuidput(endpointuuid, body=body)

Update Endpoint name

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint
body = TelstraTPN.Body8() # Body8 |  (optional)

try:
    # Update Endpoint name
    api_response = api_instance.eisendpointendpointuuidendpointuuidput(endpointuuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->eisendpointendpointuuidendpointuuidput: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 
 **body** | [**Body8**](Body8.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eisendpointsendpointuuidassigntopologytagpost**
> SuccessFragment eisendpointsendpointuuidassigntopologytagpost(endpointuuid, body=body)

Assign an Endpoint to a Topology

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint
body = TelstraTPN.Body9() # Body9 |  (optional)

try:
    # Assign an Endpoint to a Topology
    api_response = api_instance.eisendpointsendpointuuidassigntopologytagpost(endpointuuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->eisendpointsendpointuuidassigntopologytagpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 
 **body** | [**Body9**](Body9.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eisendpointstopologytaguuiddelete**
> eisendpointstopologytaguuiddelete(topotaguuid, endpointuuid)

Remove Endpoint from a Topology

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint

try:
    # Remove Endpoint from a Topology
    api_instance.eisendpointstopologytaguuiddelete(topotaguuid, endpointuuid)
except ApiException as e:
    print("Exception when calling EndpointsApi->eisendpointstopologytaguuiddelete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eisendpointstopologytaguuidtopotaguuidget**
> InlineResponse2008 eisendpointstopologytaguuidtopotaguuidget(topotaguuid)

List Endpoints for Topology

List all Endpoints associated with the topology tag.

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # List Endpoints for Topology
    api_response = api_instance.eisendpointstopologytaguuidtopotaguuidget(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->eisendpointstopologytaguuidtopotaguuidget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventoryendpointendpointuuidget**
> DatacenterResponse inventoryendpointendpointuuidget(endpointuuid)

Get information about the specified endpoint

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint

try:
    # Get information about the specified endpoint
    api_response = api_instance.inventoryendpointendpointuuidget(endpointuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventoryendpointendpointuuidget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 

### Return type

[**DatacenterResponse**](DatacenterResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventoryendpointscustomeruuidcustomeruuidget**
> Endpointone inventoryendpointscustomeruuidcustomeruuidget(customeruuid)

Get list of endpoints for a customer

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try:
    # Get list of endpoints for a customer
    api_response = api_instance.inventoryendpointscustomeruuidcustomeruuidget(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventoryendpointscustomeruuidcustomeruuidget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**Endpointone**](Endpointone.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventoryregularendpointpost**
> SuccessFragment2 inventoryregularendpointpost(body=body)

Create Physical (Port) Endpoint

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.Body4() # Body4 |  (optional)

try:
    # Create Physical (Port) Endpoint
    api_response = api_instance.inventoryregularendpointpost(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventoryregularendpointpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)|  | [optional] 

### Return type

[**SuccessFragment2**](SuccessFragment2.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.Body5() # Body5 |  (optional)

try:
    # Create VPort for physical endpoint
    api_instance.inventoryregularvportpost(body=body)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventoryregularvportpost: %s\n" % e)
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

# **inventoryvnfendpointpost**
> inventoryvnfendpointpost(body=body)

Instantiate Virtual Network Function

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
api_instance = TelstraTPN.EndpointsApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.Body7() # Body7 |  (optional)

try:
    # Instantiate Virtual Network Function
    api_instance.inventoryvnfendpointpost(body=body)
except ApiException as e:
    print("Exception when calling EndpointsApi->inventoryvnfendpointpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body7**](Body7.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

