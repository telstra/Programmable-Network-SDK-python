# TelstraTPN.TopologiesApi

All URIs are relative to *https://penapi.pacnetconnect.com/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoints_endpointuuid_assign_topology_tag_post**](TopologiesApi.md#endpoints_endpointuuid_assign_topology_tag_post) | **POST** /endpoints/{endpointuuid}/assign_topology_tag/ | Assign an Endpoint to a Topology
[**endpoints_topology_tag_uuid_topotaguuid_endpoint_endpointuuid_delete**](TopologiesApi.md#endpoints_topology_tag_uuid_topotaguuid_endpoint_endpointuuid_delete) | **DELETE** /endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid}/ | Remove Endpoint from a Topology
[**endpoints_topology_tag_uuid_topotaguuid_get**](TopologiesApi.md#endpoints_topology_tag_uuid_topotaguuid_get) | **GET** /endpoints/topology_tag_uuid/{topotaguuid}/ | List Endpoints for Topology
[**topology_tag_get**](TopologiesApi.md#topology_tag_get) | **GET** /topology_tag/ | List all topology tags
[**topology_tag_post**](TopologiesApi.md#topology_tag_post) | **POST** /topology_tag/ | Create a named topology tag
[**topology_tag_topotaguuid_delete**](TopologiesApi.md#topology_tag_topotaguuid_delete) | **DELETE** /topology_tag/{topotaguuid}/ | Delete a topology tag
[**topology_tag_topotaguuid_get**](TopologiesApi.md#topology_tag_topotaguuid_get) | **GET** /topology_tag/{topotaguuid}/ | Get information about the specified topology tag
[**topology_tag_topotaguuid_objects_get**](TopologiesApi.md#topology_tag_topotaguuid_objects_get) | **GET** /topology_tag/{topotaguuid}/objects/ | List objects for Topology
[**topology_tag_topotaguuid_put**](TopologiesApi.md#topology_tag_topotaguuid_put) | **PUT** /topology_tag/{topotaguuid}/ | Update a topology tag&#39;s name and/or description


# **endpoints_endpointuuid_assign_topology_tag_post**
> SuccessFragment endpoints_endpointuuid_assign_topology_tag_post(endpointuuid, assigntopotagrequest=assigntopotagrequest)

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint
assigntopotagrequest = TelstraTPN.Assigntopotagrequest() # Assigntopotagrequest |  (optional)

try:
    # Assign an Endpoint to a Topology
    api_response = api_instance.endpoints_endpointuuid_assign_topology_tag_post(endpointuuid, assigntopotagrequest=assigntopotagrequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->endpoints_endpointuuid_assign_topology_tag_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpointuuid** | **str**| Unique identifier representing a specific endpoint | 
 **assigntopotagrequest** | [**Assigntopotagrequest**](Assigntopotagrequest.md)|  | [optional] 

### Return type

[**SuccessFragment**](SuccessFragment.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_topology_tag_uuid_topotaguuid_endpoint_endpointuuid_delete**
> endpoints_topology_tag_uuid_topotaguuid_endpoint_endpointuuid_delete(topotaguuid, endpointuuid)

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint

try:
    # Remove Endpoint from a Topology
    api_instance.endpoints_topology_tag_uuid_topotaguuid_endpoint_endpointuuid_delete(topotaguuid, endpointuuid)
except ApiException as e:
    print("Exception when calling TopologiesApi->endpoints_topology_tag_uuid_topotaguuid_endpoint_endpointuuid_delete: %s\n" % e)
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

# **endpoints_topology_tag_uuid_topotaguuid_get**
> InlineResponse20014 endpoints_topology_tag_uuid_topotaguuid_get(topotaguuid)

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # List Endpoints for Topology
    api_response = api_instance.endpoints_topology_tag_uuid_topotaguuid_get(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->endpoints_topology_tag_uuid_topotaguuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_tag_get**
> list[Topology] topology_tag_get()

List all topology tags

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))

try:
    # List all topology tags
    api_response = api_instance.topology_tag_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->topology_tag_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Topology]**](Topology.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_tag_post**
> Topology topology_tag_post(topotagcreaterequest=topotagcreaterequest)

Create a named topology tag

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotagcreaterequest = TelstraTPN.Topotagcreaterequest() # Topotagcreaterequest |  (optional)

try:
    # Create a named topology tag
    api_response = api_instance.topology_tag_post(topotagcreaterequest=topotagcreaterequest)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->topology_tag_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotagcreaterequest** | [**Topotagcreaterequest**](Topotagcreaterequest.md)|  | [optional] 

### Return type

[**Topology**](Topology.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_tag_topotaguuid_delete**
> topology_tag_topotaguuid_delete(topotaguuid)

Delete a topology tag

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # Delete a topology tag
    api_instance.topology_tag_topotaguuid_delete(topotaguuid)
except ApiException as e:
    print("Exception when calling TopologiesApi->topology_tag_topotaguuid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_tag_topotaguuid_get**
> Topology topology_tag_topotaguuid_get(topotaguuid)

Get information about the specified topology tag

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # Get information about the specified topology tag
    api_response = api_instance.topology_tag_topotaguuid_get(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->topology_tag_topotaguuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

[**Topology**](Topology.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_tag_topotaguuid_objects_get**
> InlineResponse20013 topology_tag_topotaguuid_objects_get(topotaguuid)

List objects for Topology

List all objects (Endpoints, Links, VPorts, etc.) associated with the topology tag.

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # List objects for Topology
    api_response = api_instance.topology_tag_topotaguuid_objects_get(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->topology_tag_topotaguuid_objects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **topology_tag_topotaguuid_put**
> Topology topology_tag_topotaguuid_put(topotaguuid, topotagupdateresponse=topotagupdateresponse)

Update a topology tag's name and/or description

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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag
topotagupdateresponse = TelstraTPN.Topotagupdateresponse() # Topotagupdateresponse |  (optional)

try:
    # Update a topology tag's name and/or description
    api_response = api_instance.topology_tag_topotaguuid_put(topotaguuid, topotagupdateresponse=topotagupdateresponse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->topology_tag_topotaguuid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 
 **topotagupdateresponse** | [**Topotagupdateresponse**](Topotagupdateresponse.md)|  | [optional] 

### Return type

[**Topology**](Topology.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

