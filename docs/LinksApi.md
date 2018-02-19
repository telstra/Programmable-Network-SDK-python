# TelstraTPN.LinksApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventorylinkpost**](LinksApi.md#inventorylinkpost) | **POST** /1.0.0/inventory/link | Create Link and initial Contract
[**inventorylinkscustomercustomeruuidget**](LinksApi.md#inventorylinkscustomercustomeruuidget) | **GET** /1.0.0/inventory/links/customer/{customeruuid} | Get active Links
[**inventorylinkshistorylinkidget**](LinksApi.md#inventorylinkshistorylinkidget) | **GET** /1.0.0/inventory/links/history/{linkid} | Get Link history
[**inventorylinkslinkidget**](LinksApi.md#inventorylinkslinkidget) | **GET** /1.0.0/inventory/links/{linkid} | Get details of specified link


# **inventorylinkpost**
> inventorylinkpost(body=body)

Create Link and initial Contract

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.Body() # Body |  (optional)

try:
    # Create Link and initial Contract
    api_instance.inventorylinkpost(body=body)
except ApiException as e:
    print("Exception when calling LinksApi->inventorylinkpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventorylinkscustomercustomeruuidget**
> list[Link] inventorylinkscustomercustomeruuidget(customeruuid)

Get active Links

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
customeruuid = 'customeruuid_example' # str | Unique identifier representing a specific customer

try:
    # Get active Links
    api_response = api_instance.inventorylinkscustomercustomeruuidget(customeruuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventorylinkscustomercustomeruuidget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customeruuid** | **str**| Unique identifier representing a specific customer | 

### Return type

[**list[Link]**](Link.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventorylinkshistorylinkidget**
> InlineResponse2003 inventorylinkshistorylinkidget(linkid)

Get Link history

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link

try:
    # Get Link history
    api_response = api_instance.inventorylinkshistorylinkidget(linkid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventorylinkshistorylinkidget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventorylinkslinkidget**
> InlineResponse2004 inventorylinkslinkidget(linkid)

Get details of specified link

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
api_instance = TelstraTPN.LinksApi(TelstraTPN.ApiClient(configuration))
linkid = 'linkid_example' # str | Unique identifier representing a specific link

try:
    # Get details of specified link
    api_response = api_instance.inventorylinkslinkidget(linkid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinksApi->inventorylinkslinkidget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linkid** | **str**| Unique identifier representing a specific link | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

