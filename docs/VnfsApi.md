# TelstraTPN.VnfsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventoryvnfendpointpost**](VnfsApi.md#inventoryvnfendpointpost) | **POST** /1.0.0/inventory/vnfendpoint | Instantiate Virtual Network Function
[**inventoryvnfvportpost**](VnfsApi.md#inventoryvnfvportpost) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
[**marketplaceimageget**](VnfsApi.md#marketplaceimageget) | **GET** /1.0.0/marketplace/image | List images in the Marketplace
[**marketplaceimageimageidaddtomyimagespost**](VnfsApi.md#marketplaceimageimageidaddtomyimagespost) | **POST** /1.0.0/marketplace/image/{imageid}/add_to_my_images/ | Add specified image to \&quot;My Images\&quot;
[**marketplaceimageimageidget**](VnfsApi.md#marketplaceimageimageidget) | **GET** /1.0.0/marketplace/image/{imageid}/ | Get information about the specified image
[**marketplaceimageimageidremovefrommyimagespost**](VnfsApi.md#marketplaceimageimageidremovefrommyimagespost) | **POST** /1.0.0/marketplace/image/{imageid}/remove_from_my_images/ | Remove specified image from \&quot;My Images\&quot;
[**marketplaceimagemyimagesget**](VnfsApi.md#marketplaceimagemyimagesget) | **GET** /1.0.0/marketplace/image/my_images/ | List images in \&quot;My Images\&quot;
[**vnfdsvnfvnfuuidget**](VnfsApi.md#vnfdsvnfvnfuuidget) | **GET** /vnfds/1.0.0/vnf/{vnfuuid}/ | Get status information about the specified VNF
[**vnfdsvnfvnfuuidrebootpost**](VnfsApi.md#vnfdsvnfvnfuuidrebootpost) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/reboot | Reboot the specified VNF
[**vnfdsvnfvnfuuidresumepost**](VnfsApi.md#vnfdsvnfvnfuuidresumepost) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/resume | Resume the specified VNF
[**vnfdsvnfvnfuuidsuspendpost**](VnfsApi.md#vnfdsvnfvnfuuidsuspendpost) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/suspend | Suspend the specified VNF


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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.Body7() # Body7 |  (optional)

try:
    # Instantiate Virtual Network Function
    api_instance.inventoryvnfendpointpost(body=body)
except ApiException as e:
    print("Exception when calling VnfsApi->inventoryvnfendpointpost: %s\n" % e)
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

# **inventoryvnfvportpost**
> InlineResponse2005 inventoryvnfvportpost(body=body)

Create VNF VPort

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
body = TelstraTPN.Body6() # Body6 |  (optional)

try:
    # Create VNF VPort
    api_response = api_instance.inventoryvnfvportpost(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->inventoryvnfvportpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplaceimageget**
> InlineResponse2006 marketplaceimageget()

List images in the Marketplace

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))

try:
    # List images in the Marketplace
    api_response = api_instance.marketplaceimageget()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplaceimageget: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplaceimageimageidaddtomyimagespost**
> InlineResponse2007 marketplaceimageimageidaddtomyimagespost(imageid, body=body)

Add specified image to \"My Images\"

Note that trailing / is required, body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
imageid = 56 # int | Identifier representing a specific VNF image
body = NULL # object |  (optional)

try:
    # Add specified image to \"My Images\"
    api_response = api_instance.marketplaceimageimageidaddtomyimagespost(imageid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplaceimageimageidaddtomyimagespost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageid** | **int**| Identifier representing a specific VNF image | 
 **body** | **object**|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplaceimageimageidget**
> Image marketplaceimageimageidget(imageid)

Get information about the specified image

Note that trailing / is required

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
imageid = 56 # int | Identifier representing a specific VNF image

try:
    # Get information about the specified image
    api_response = api_instance.marketplaceimageimageidget(imageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplaceimageimageidget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageid** | **int**| Identifier representing a specific VNF image | 

### Return type

[**Image**](Image.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplaceimageimageidremovefrommyimagespost**
> InlineResponse2007 marketplaceimageimageidremovefrommyimagespost(imageid, body=body)

Remove specified image from \"My Images\"

Note that trailing / is required, body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
imageid = 56 # int | Identifier representing a specific VNF image
body = NULL # object |  (optional)

try:
    # Remove specified image from \"My Images\"
    api_response = api_instance.marketplaceimageimageidremovefrommyimagespost(imageid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplaceimageimageidremovefrommyimagespost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageid** | **int**| Identifier representing a specific VNF image | 
 **body** | **object**|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplaceimagemyimagesget**
> InlineResponse2006 marketplaceimagemyimagesget()

List images in \"My Images\"

Note that trailing / is required

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))

try:
    # List images in \"My Images\"
    api_response = api_instance.marketplaceimagemyimagesget()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplaceimagemyimagesget: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnfdsvnfvnfuuidget**
> InlineResponse20010 vnfdsvnfvnfuuidget(vnfuuid)

Get status information about the specified VNF

'Possible return values:   ACTIVE,   BUILD,   SHUTOFF,   VERIFY_RESIZE,   PAUSED,   SUSPENDED,   RESCUE,   ERROR,   DELETED,   SOFT_DELETED,   SHELVED,   SHELVED_OFFLOADED'

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # Get status information about the specified VNF
    api_response = api_instance.vnfdsvnfvnfuuidget(vnfuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->vnfdsvnfvnfuuidget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnfdsvnfvnfuuidrebootpost**
> vnfdsvnfvnfuuidrebootpost(vnfuuid, body=body)

Reboot the specified VNF

reboot_type is 'warm' or 'cold'

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function
body = TelstraTPN.Body14() # Body14 |  (optional)

try:
    # Reboot the specified VNF
    api_instance.vnfdsvnfvnfuuidrebootpost(vnfuuid, body=body)
except ApiException as e:
    print("Exception when calling VnfsApi->vnfdsvnfvnfuuidrebootpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 
 **body** | [**Body14**](Body14.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnfdsvnfvnfuuidresumepost**
> vnfdsvnfvnfuuidresumepost(vnfuuid)

Resume the specified VNF

Note that body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # Resume the specified VNF
    api_instance.vnfdsvnfvnfuuidresumepost(vnfuuid)
except ApiException as e:
    print("Exception when calling VnfsApi->vnfdsvnfvnfuuidresumepost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnfdsvnfvnfuuidsuspendpost**
> vnfdsvnfvnfuuidsuspendpost(vnfuuid)

Suspend the specified VNF

Note that body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # Suspend the specified VNF
    api_instance.vnfdsvnfvnfuuidsuspendpost(vnfuuid)
except ApiException as e:
    print("Exception when calling VnfsApi->vnfdsvnfvnfuuidsuspendpost: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

