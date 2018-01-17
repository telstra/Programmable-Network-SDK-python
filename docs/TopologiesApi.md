# TelstraTPN.TopologiesApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ttms100_topology_tag_by_topotaguuid_delete**](TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_delete) | **DELETE** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Delete a topology tag
[**ttms100_topology_tag_by_topotaguuid_get**](TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_get) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Get information about the specified topology tag
[**ttms100_topology_tag_by_topotaguuid_put**](TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_put) | **PUT** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Update a topology tag&#39;s name and/or description
[**ttms100_topology_tag_get**](TopologiesApi.md#ttms100_topology_tag_get) | **GET** /ttms/1.0.0/topology_tag | List all topology tags
[**ttms100_topology_tag_objects_by_topotaguuid_get**](TopologiesApi.md#ttms100_topology_tag_objects_by_topotaguuid_get) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/objects/ | List objects for Topology
[**ttms100_topology_tag_post**](TopologiesApi.md#ttms100_topology_tag_post) | **POST** /ttms/1.0.0/topology_tag | Create a named topology tag


# **ttms100_topology_tag_by_topotaguuid_delete**
> ttms100_topology_tag_by_topotaguuid_delete(topotaguuid)

Delete a topology tag

Delete a topology tag

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.TopologiesApi()
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # Delete a topology tag
    api_instance.ttms100_topology_tag_by_topotaguuid_delete(topotaguuid)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttms100_topology_tag_by_topotaguuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttms100_topology_tag_by_topotaguuid_get**
> Topology ttms100_topology_tag_by_topotaguuid_get(topotaguuid)

Get information about the specified topology tag

Get information about the specified topology tag

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.TopologiesApi()
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # Get information about the specified topology tag
    api_response = api_instance.ttms100_topology_tag_by_topotaguuid_get(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttms100_topology_tag_by_topotaguuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttms100_topology_tag_by_topotaguuid_put**
> Topology ttms100_topology_tag_by_topotaguuid_put(topotaguuid, body=body)

Update a topology tag's name and/or description

Update a topology tag's name and/or description

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.TopologiesApi()
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag
body = TelstraTPN.Ttms100TopologyTagRequest() # Ttms100TopologyTagRequest |  (optional)

try:
    # Update a topology tag's name and/or description
    api_response = api_instance.ttms100_topology_tag_by_topotaguuid_put(topotaguuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttms100_topology_tag_by_topotaguuid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 
 **body** | [**Ttms100TopologyTagRequest**](Ttms100TopologyTagRequest.md)|  | [optional] 

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttms100_topology_tag_get**
> list[Topology] ttms100_topology_tag_get()

List all topology tags

List all topology tags

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.TopologiesApi()

try:
    # List all topology tags
    api_response = api_instance.ttms100_topology_tag_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttms100_topology_tag_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Topology]**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttms100_topology_tag_objects_by_topotaguuid_get**
> Ttms100TopologyTagObjectsResponse ttms100_topology_tag_objects_by_topotaguuid_get(topotaguuid)

List objects for Topology

List all objects (Endpoints, Links, VPorts, etc.) associated with the topology tag.

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.TopologiesApi()
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # List objects for Topology
    api_response = api_instance.ttms100_topology_tag_objects_by_topotaguuid_get(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttms100_topology_tag_objects_by_topotaguuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

[**Ttms100TopologyTagObjectsResponse**](Ttms100TopologyTagObjectsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttms100_topology_tag_post**
> Topology ttms100_topology_tag_post(body=body)

Create a named topology tag

Create a named topology tag

### Example
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.TopologiesApi()
body = TelstraTPN.Ttms100TopologyTagRequest() # Ttms100TopologyTagRequest |  (optional)

try:
    # Create a named topology tag
    api_response = api_instance.ttms100_topology_tag_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttms100_topology_tag_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ttms100TopologyTagRequest**](Ttms100TopologyTagRequest.md)|  | [optional] 

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

