# TelstraTPN.TopologiesApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ttms100_topology_tag_by_topotaguuid_delete**](TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_delete) | **DELETE** /ttms/1.0.0/topology_tag/{topotaguuid}/ | ttmstopologytagtopotaguuiddelete
[**ttms100_topology_tag_by_topotaguuid_get**](TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_get) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/ | ttmstopologytagtopotaguuidget
[**ttms100_topology_tag_by_topotaguuid_put**](TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_put) | **PUT** /ttms/1.0.0/topology_tag/{topotaguuid}/ | ttmstopologytagtopotaguuidput
[**ttms100_topology_tag_get**](TopologiesApi.md#ttms100_topology_tag_get) | **GET** /ttms/1.0.0/topology_tag | ttmstopologytagget
[**ttms100_topology_tag_objects_by_topotaguuid_get**](TopologiesApi.md#ttms100_topology_tag_objects_by_topotaguuid_get) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/objects/ | ttmstopologytagtopotaguuidobjectsget
[**ttms100_topology_tag_post**](TopologiesApi.md#ttms100_topology_tag_post) | **POST** /ttms/1.0.0/topology_tag | ttmstopologytagpost


# **ttms100_topology_tag_by_topotaguuid_delete**
> ttms100_topology_tag_by_topotaguuid_delete(topotaguuid, body=body)

ttmstopologytagtopotaguuiddelete

Delete a topology tag

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag
body = TelstraTPN.Body72() # Body72 |  (optional)

try:
    # ttmstopologytagtopotaguuiddelete
    api_instance.ttms100_topology_tag_by_topotaguuid_delete(topotaguuid, body=body)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttms100_topology_tag_by_topotaguuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 
 **body** | [**Body72**](Body72.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttms100_topology_tag_by_topotaguuid_get**
> Topology ttms100_topology_tag_by_topotaguuid_get(topotaguuid)

ttmstopologytagtopotaguuidget

Get information about the specified topology tag

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # ttmstopologytagtopotaguuidget
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

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttms100_topology_tag_by_topotaguuid_put**
> Topology ttms100_topology_tag_by_topotaguuid_put(topotaguuid, body=body)

ttmstopologytagtopotaguuidput

Update a topology tag's name and/or description

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag
body = TelstraTPN.Body72() # Body72 |  (optional)

try:
    # ttmstopologytagtopotaguuidput
    api_response = api_instance.ttms100_topology_tag_by_topotaguuid_put(topotaguuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttms100_topology_tag_by_topotaguuid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 
 **body** | [**Body72**](Body72.md)|  | [optional] 

### Return type

[**Topology**](Topology.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttms100_topology_tag_get**
> list[Topology] ttms100_topology_tag_get()

ttmstopologytagget

List all topology tags

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))

try:
    # ttmstopologytagget
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

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttms100_topology_tag_objects_by_topotaguuid_get**
> TtmstopologytagtopotaguuidobjectsgetResponse ttms100_topology_tag_objects_by_topotaguuid_get(topotaguuid)

ttmstopologytagtopotaguuidobjectsget

List all objects (Endpoints, Links, VPorts, etc.) associated with the topology tag.

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # ttmstopologytagtopotaguuidobjectsget
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

[**TtmstopologytagtopotaguuidobjectsgetResponse**](TtmstopologytagtopotaguuidobjectsgetResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttms100_topology_tag_post**
> Topology ttms100_topology_tag_post(body=body)

ttmstopologytagpost

Create a named topology tag

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.Body72() # Body72 |  (optional)

try:
    # ttmstopologytagpost
    api_response = api_instance.ttms100_topology_tag_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttms100_topology_tag_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body72**](Body72.md)|  | [optional] 

### Return type

[**Topology**](Topology.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

