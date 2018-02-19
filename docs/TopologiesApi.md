# TelstraTPN.TopologiesApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eisendpointsendpointuuidassigntopologytagpost**](TopologiesApi.md#eisendpointsendpointuuidassigntopologytagpost) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | Assign an Endpoint to a Topology
[**eisendpointstopologytaguuiddelete**](TopologiesApi.md#eisendpointstopologytaguuiddelete) | **DELETE** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid} | Remove Endpoint from a Topology
[**eisendpointstopologytaguuidtopotaguuidget**](TopologiesApi.md#eisendpointstopologytaguuidtopotaguuidget) | **GET** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid} | List Endpoints for Topology
[**ttmstopologytagget**](TopologiesApi.md#ttmstopologytagget) | **GET** /ttms/1.0.0/topology_tag | List all topology tags
[**ttmstopologytagpost**](TopologiesApi.md#ttmstopologytagpost) | **POST** /ttms/1.0.0/topology_tag | Create a named topology tag
[**ttmstopologytagtopotaguuiddelete**](TopologiesApi.md#ttmstopologytagtopotaguuiddelete) | **DELETE** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Delete a topology tag
[**ttmstopologytagtopotaguuidget**](TopologiesApi.md#ttmstopologytagtopotaguuidget) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Get information about the specified topology tag
[**ttmstopologytagtopotaguuidobjectsget**](TopologiesApi.md#ttmstopologytagtopotaguuidobjectsget) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/objects/ | List objects for Topology
[**ttmstopologytagtopotaguuidput**](TopologiesApi.md#ttmstopologytagtopotaguuidput) | **PUT** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Update a topology tag&#39;s name and/or description


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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint
body = TelstraTPN.Body9() # Body9 |  (optional)

try:
    # Assign an Endpoint to a Topology
    api_response = api_instance.eisendpointsendpointuuidassigntopologytagpost(endpointuuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->eisendpointsendpointuuidassigntopologytagpost: %s\n" % e)
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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag
endpointuuid = 'endpointuuid_example' # str | Unique identifier representing a specific endpoint

try:
    # Remove Endpoint from a Topology
    api_instance.eisendpointstopologytaguuiddelete(topotaguuid, endpointuuid)
except ApiException as e:
    print("Exception when calling TopologiesApi->eisendpointstopologytaguuiddelete: %s\n" % e)
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
api_instance = TelstraTPN.TopologiesApi(TelstraTPN.ApiClient(configuration))
topotaguuid = 'topotaguuid_example' # str | Unique identifier representing a specific topology tag

try:
    # List Endpoints for Topology
    api_response = api_instance.eisendpointstopologytaguuidtopotaguuidget(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->eisendpointstopologytaguuidtopotaguuidget: %s\n" % e)
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

# **ttmstopologytagget**
> list[Topology] ttmstopologytagget()

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
    api_response = api_instance.ttmstopologytagget()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttmstopologytagget: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Topology]**](Topology.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttmstopologytagpost**
> Topology ttmstopologytagpost(body=body)

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
body = TelstraTPN.Body10() # Body10 |  (optional)

try:
    # Create a named topology tag
    api_response = api_instance.ttmstopologytagpost(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttmstopologytagpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body10**](Body10.md)|  | [optional] 

### Return type

[**Topology**](Topology.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttmstopologytagtopotaguuiddelete**
> ttmstopologytagtopotaguuiddelete(topotaguuid, body=body)

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
body = TelstraTPN.Body13() # Body13 |  (optional)

try:
    # Delete a topology tag
    api_instance.ttmstopologytagtopotaguuiddelete(topotaguuid, body=body)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttmstopologytagtopotaguuiddelete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 
 **body** | [**Body13**](Body13.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttmstopologytagtopotaguuidget**
> Topology ttmstopologytagtopotaguuidget(topotaguuid, body=body)

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
body = TelstraTPN.Body11() # Body11 |  (optional)

try:
    # Get information about the specified topology tag
    api_response = api_instance.ttmstopologytagtopotaguuidget(topotaguuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttmstopologytagtopotaguuidget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 
 **body** | [**Body11**](Body11.md)|  | [optional] 

### Return type

[**Topology**](Topology.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttmstopologytagtopotaguuidobjectsget**
> InlineResponse2009 ttmstopologytagtopotaguuidobjectsget(topotaguuid)

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
    api_response = api_instance.ttmstopologytagtopotaguuidobjectsget(topotaguuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttmstopologytagtopotaguuidobjectsget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ttmstopologytagtopotaguuidput**
> Topology ttmstopologytagtopotaguuidput(topotaguuid, body=body)

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
body = TelstraTPN.Body12() # Body12 |  (optional)

try:
    # Update a topology tag's name and/or description
    api_response = api_instance.ttmstopologytagtopotaguuidput(topotaguuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TopologiesApi->ttmstopologytagtopotaguuidput: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **topotaguuid** | **str**| Unique identifier representing a specific topology tag | 
 **body** | [**Body12**](Body12.md)|  | [optional] 

### Return type

[**Topology**](Topology.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

