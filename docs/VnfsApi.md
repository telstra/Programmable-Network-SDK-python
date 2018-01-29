# TelstraTPN.VnfsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**marketplace_image_add_to_my_images_by_imageid_post**](VnfsApi.md#marketplace_image_add_to_my_images_by_imageid_post) | **POST** /1.0.0/marketplace/image/{imageid}/add_to_my_images/ | marketplaceimageimageidaddtomyimagespost
[**marketplace_image_by_imageid_get**](VnfsApi.md#marketplace_image_by_imageid_get) | **GET** /1.0.0/marketplace/image/{imageid}/ | marketplaceimageimageidget
[**marketplace_image_get**](VnfsApi.md#marketplace_image_get) | **GET** /1.0.0/marketplace/image | marketplaceimageget
[**marketplace_image_my_images_get**](VnfsApi.md#marketplace_image_my_images_get) | **GET** /1.0.0/marketplace/image/my_images/ | marketplaceimagemyimagesget
[**marketplace_image_remove_from_my_images_by_imageid_post**](VnfsApi.md#marketplace_image_remove_from_my_images_by_imageid_post) | **POST** /1.0.0/marketplace/image/{imageid}/remove_from_my_images/ | marketplaceimageimageidremovefrommyimagespost
[**vnfds100_vnf_by_vnfuuid_get**](VnfsApi.md#vnfds100_vnf_by_vnfuuid_get) | **GET** /vnfds/1.0.0/vnf/{vnfuuid}/ | vnfdsvnfvnfuuidget
[**vnfds100_vnf_reboot_by_vnfuuid_post**](VnfsApi.md#vnfds100_vnf_reboot_by_vnfuuid_post) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/reboot | vnfdsvnfvnfuuidrebootpost
[**vnfds100_vnf_resume_by_vnfuuid_post**](VnfsApi.md#vnfds100_vnf_resume_by_vnfuuid_post) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/resume | vnfdsvnfvnfuuidresumepost
[**vnfds100_vnf_suspend_by_vnfuuid_post**](VnfsApi.md#vnfds100_vnf_suspend_by_vnfuuid_post) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/suspend | vnfdsvnfvnfuuidsuspendpost


# **marketplace_image_add_to_my_images_by_imageid_post**
> MarketplaceimageimageidaddtomyimagespostResponse marketplace_image_add_to_my_images_by_imageid_post(imageid, body=body)

marketplaceimageimageidaddtomyimagespost

Note that trailing / is required, body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
imageid = 56 # int | Identifier representing a specific VNF image
body = NULL # object |  (optional)

try:
    # marketplaceimageimageidaddtomyimagespost
    api_response = api_instance.marketplace_image_add_to_my_images_by_imageid_post(imageid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_add_to_my_images_by_imageid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageid** | **int**| Identifier representing a specific VNF image | 
 **body** | **object**|  | [optional] 

### Return type

[**MarketplaceimageimageidaddtomyimagespostResponse**](MarketplaceimageimageidaddtomyimagespostResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_image_by_imageid_get**
> Image marketplace_image_by_imageid_get(imageid)

marketplaceimageimageidget

Note that trailing / is required

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
imageid = 56 # int | Identifier representing a specific VNF image

try:
    # marketplaceimageimageidget
    api_response = api_instance.marketplace_image_by_imageid_get(imageid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_by_imageid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageid** | **int**| Identifier representing a specific VNF image | 

### Return type

[**Image**](Image.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_image_get**
> MarketplaceimagegetResponse marketplace_image_get()

marketplaceimageget

List images in the Marketplace

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))

try:
    # marketplaceimageget
    api_response = api_instance.marketplace_image_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketplaceimagegetResponse**](MarketplaceimagegetResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_image_my_images_get**
> MarketplaceimagemyimagesgetResponse marketplace_image_my_images_get()

marketplaceimagemyimagesget

Note that trailing / is required

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))

try:
    # marketplaceimagemyimagesget
    api_response = api_instance.marketplace_image_my_images_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_my_images_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MarketplaceimagemyimagesgetResponse**](MarketplaceimagemyimagesgetResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **marketplace_image_remove_from_my_images_by_imageid_post**
> MarketplaceimageimageidremovefrommyimagespostResponse marketplace_image_remove_from_my_images_by_imageid_post(imageid, body=body)

marketplaceimageimageidremovefrommyimagespost

Note that trailing / is required, body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
imageid = 56 # int | Identifier representing a specific VNF image
body = NULL # object |  (optional)

try:
    # marketplaceimageimageidremovefrommyimagespost
    api_response = api_instance.marketplace_image_remove_from_my_images_by_imageid_post(imageid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->marketplace_image_remove_from_my_images_by_imageid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imageid** | **int**| Identifier representing a specific VNF image | 
 **body** | **object**|  | [optional] 

### Return type

[**MarketplaceimageimageidremovefrommyimagespostResponse**](MarketplaceimageimageidremovefrommyimagespostResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnfds100_vnf_by_vnfuuid_get**
> VnfdsvnfvnfuuidgetResponse vnfds100_vnf_by_vnfuuid_get(vnfuuid)

vnfdsvnfvnfuuidget

'Possible return values:   ACTIVE,   BUILD,   SHUTOFF,   VERIFY_RESIZE,   PAUSED,   SUSPENDED,   RESCUE,   ERROR,   DELETED,   SOFT_DELETED,   SHELVED,   SHELVED_OFFLOADED'

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # vnfdsvnfvnfuuidget
    api_response = api_instance.vnfds100_vnf_by_vnfuuid_get(vnfuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VnfsApi->vnfds100_vnf_by_vnfuuid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

[**VnfdsvnfvnfuuidgetResponse**](VnfdsvnfvnfuuidgetResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnfds100_vnf_reboot_by_vnfuuid_post**
> vnfds100_vnf_reboot_by_vnfuuid_post(vnfuuid, body=body)

vnfdsvnfvnfuuidrebootpost

reboot_type is 'warm' or 'cold'

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function
body = TelstraTPN.Body80() # Body80 |  (optional)

try:
    # vnfdsvnfvnfuuidrebootpost
    api_instance.vnfds100_vnf_reboot_by_vnfuuid_post(vnfuuid, body=body)
except ApiException as e:
    print("Exception when calling VnfsApi->vnfds100_vnf_reboot_by_vnfuuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 
 **body** | [**Body80**](Body80.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnfds100_vnf_resume_by_vnfuuid_post**
> vnfds100_vnf_resume_by_vnfuuid_post(vnfuuid)

vnfdsvnfvnfuuidresumepost

Note that body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # vnfdsvnfvnfuuidresumepost
    api_instance.vnfds100_vnf_resume_by_vnfuuid_post(vnfuuid)
except ApiException as e:
    print("Exception when calling VnfsApi->vnfds100_vnf_resume_by_vnfuuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vnfds100_vnf_suspend_by_vnfuuid_post**
> vnfds100_vnf_suspend_by_vnfuuid_post(vnfuuid)

vnfdsvnfvnfuuidsuspendpost

Note that body must be {}

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
api_instance = TelstraTPN.VnfsApi(TelstraTPN.ApiClient(configuration))
vnfuuid = 'vnfuuid_example' # str | Unique identifier representing a specific virtual network function

try:
    # vnfdsvnfvnfuuidsuspendpost
    api_instance.vnfds100_vnf_suspend_by_vnfuuid_post(vnfuuid)
except ApiException as e:
    print("Exception when calling VnfsApi->vnfds100_vnf_suspend_by_vnfuuid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vnfuuid** | **str**| Unique identifier representing a specific virtual network function | 

### Return type

void (empty response body)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

