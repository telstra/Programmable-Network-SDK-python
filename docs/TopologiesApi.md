# TelstraTPN.TopologiesApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_a_named_topology_tag**](TopologiesApi.md#create_a_named_topology_tag) | **POST** /ttms/1.0.0/topology_tag | Create a named topology tag
[**get_information_about_the_specified_topology_tag**](TopologiesApi.md#get_information_about_the_specified_topology_tag) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Get information about the specified topology tag
[**list_all_topology_tags**](TopologiesApi.md#list_all_topology_tags) | **GET** /ttms/1.0.0/topology_tag | List all topology tags
[**list_objects_for_topology**](TopologiesApi.md#list_objects_for_topology) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/objects/ | List objects for Topology


# **create_a_named_topology_tag**
> Topology create_a_named_topology_tag(body=body)

Create a named topology tag

Create a named topology tag

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
api_instance = TelstraTPN.TopologiesApi()
body = TelstraTPN.Ttms100TopologyTagRequest() # Ttms100TopologyTagRequest |  (optional)

try: 
    # Create a named topology tag
    api_response = api_instance.create_a_named_topology_tag(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->create_a_named_topology_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Ttms100TopologyTagRequest**](Ttms100TopologyTagRequest.md)|  | [optional] 

### Return type

[**Topology**](Topology.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_information_about_the_specified_topology_tag**
> Topology get_information_about_the_specified_topology_tag(topotaguuid)

Get information about the specified topology tag

Get information about the specified topology tag

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
api_instance = TelstraTPN.TopologiesApi()
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try: 
    # Get information about the specified topology tag
    api_response = api_instance.get_information_about_the_specified_topology_tag(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->get_information_about_the_specified_topology_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

[**Topology**](Topology.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_topology_tags**
> list[Topology] list_all_topology_tags()

List all topology tags

List all topology tags

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
api_instance = TelstraTPN.TopologiesApi()

try: 
    # List all topology tags
    api_response = api_instance.list_all_topology_tags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->list_all_topology_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Topology]**](Topology.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_objects_for_topology**
> Ttms100TopologyTagObjectsResponse list_objects_for_topology(topotaguuid)

List objects for Topology

List all objects (Endpoints, Links, VPorts, etc.) associated with the topology tag.

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
api_instance = TelstraTPN.TopologiesApi()
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try: 
    # List objects for Topology
    api_response = api_instance.list_objects_for_topology(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->list_objects_for_topology: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

[**Ttms100TopologyTagObjectsResponse**](Ttms100TopologyTagObjectsResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

