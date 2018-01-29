[![Build Status](https://travis-ci.org/telstra/Programmable-Network-SDK-python.svg?branch=master)](https://travis-ci.org/telstra/Programmable-Network-SDK-python)

# TelstraTPN
Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.

- API version: 2.3.2
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/Telstra/Programmable-Network-SDK-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Telstra/Programmable-Network-SDK-python.git`)

Then import the package:
```python
import TelstraTPN 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import TelstraTPN
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = TelstraTPN.AuthenticationApi()
grant_type = 'password' # str | 
username = 'username_example' # str | 
password = 'password_example' # str | 

try:
    # authgeneratetokenpost
    api_response = api_instance.auth_generatetoken_post(grant_type, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_generatetoken_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://penapi.pacnetconnect.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**auth_generatetoken_post**](docs/AuthenticationApi.md#auth_generatetoken_post) | **POST** /1.0.0/auth/generatetoken | authgeneratetokenpost
*AuthenticationApi* | [**auth_validatetoken_get**](docs/AuthenticationApi.md#auth_validatetoken_get) | **GET** /1.0.0/auth/validatetoken | authvalidatetokenget
*ContractsApi* | [**inventory_links_contract_by_linkid_and_contractid_get**](docs/ContractsApi.md#inventory_links_contract_by_linkid_and_contractid_get) | **GET** /1.0.0/inventory/links/{linkid}/contract/{contractid} | inventorylinksget
*ContractsApi* | [**inventory_links_contract_by_linkid_and_contractid_put**](docs/ContractsApi.md#inventory_links_contract_by_linkid_and_contractid_put) | **PUT** /1.0.0/inventory/links/{linkid}/contract/{contractid} | inventorylinksput
*ContractsApi* | [**inventory_links_contract_by_linkid_post**](docs/ContractsApi.md#inventory_links_contract_by_linkid_post) | **POST** /1.0.0/inventory/links/{linkid}/contract | inventorylinkslinkidcontractpost
*CustomersApi* | [**account_by_customeruuid_get**](docs/CustomersApi.md#account_by_customeruuid_get) | **GET** /1.0.0/account/{customeruuid} | accountcustomeruuidget
*CustomersApi* | [**account_user_by_customeruuid_get**](docs/CustomersApi.md#account_user_by_customeruuid_get) | **GET** /1.0.0/account/{customeruuid}/user | accountcustomeruuiduserget
*DatacentresApi* | [**inventory_datacenters_get**](docs/DatacentresApi.md#inventory_datacenters_get) | **GET** /1.0.0/inventory/datacenters | inventorydatacentersget
*EndpointsApi* | [**eis100_endpoint_endpointuuid_by_endpointuuid_put**](docs/EndpointsApi.md#eis100_endpoint_endpointuuid_by_endpointuuid_put) | **PUT** /eis/1.0.0/endpoint/endpointuuid/{endpointuuid} | eisendpointendpointuuidendpointuuidput
*EndpointsApi* | [**eis100_endpoints_assign_topology_tag_by_endpointuuid_post**](docs/EndpointsApi.md#eis100_endpoints_assign_topology_tag_by_endpointuuid_post) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | eisendpointsendpointuuidassigntopologytagpost
*EndpointsApi* | [**eis100_endpoints_topology_tag_uuid_by_topotaguuid_get**](docs/EndpointsApi.md#eis100_endpoints_topology_tag_uuid_by_topotaguuid_get) | **GET** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid} | eisendpointstopologytaguuidtopotaguuidget
*EndpointsApi* | [**eis100_endpoints_topology_tag_uuid_endpoint_by_topotaguuid_and_endpointuuid_delete**](docs/EndpointsApi.md#eis100_endpoints_topology_tag_uuid_endpoint_by_topotaguuid_and_endpointuuid_delete) | **DELETE** /eis/1.0.0/endpoints/topology_tag_uuid/{topotaguuid}/endpoint/{endpointuuid} | eisendpointstopologytaguuiddelete
*EndpointsApi* | [**inventory_endpoint_by_endpointuuid_get**](docs/EndpointsApi.md#inventory_endpoint_by_endpointuuid_get) | **GET** /1.0.0/inventory/endpoint/{endpointuuid} | inventoryendpointendpointuuidget
*EndpointsApi* | [**inventory_endpoints_customeruuid_by_customeruuid_get**](docs/EndpointsApi.md#inventory_endpoints_customeruuid_by_customeruuid_get) | **GET** /1.0.0/inventory/endpoints/customeruuid/{customeruuid} | inventoryendpointscustomeruuidcustomeruuidget
*EndpointsApi* | [**inventory_regularendpoint_post**](docs/EndpointsApi.md#inventory_regularendpoint_post) | **POST** /1.0.0/inventory/regularendpoint | inventoryregularendpointpost
*EndpointsApi* | [**inventory_vnfendpoint_post**](docs/EndpointsApi.md#inventory_vnfendpoint_post) | **POST** /1.0.0/inventory/vnfendpoint | inventoryvnfendpointpost
*LinksApi* | [**inventory_link_post**](docs/LinksApi.md#inventory_link_post) | **POST** /1.0.0/inventory/link | inventorylinkpost
*LinksApi* | [**inventory_links_by_linkid_get**](docs/LinksApi.md#inventory_links_by_linkid_get) | **GET** /1.0.0/inventory/links/{linkid} | inventorylinkslinkidget
*LinksApi* | [**inventory_links_customer_by_customeruuid_get**](docs/LinksApi.md#inventory_links_customer_by_customeruuid_get) | **GET** /1.0.0/inventory/links/customer/{customeruuid} | inventorylinkscustomercustomeruuidget
*LinksApi* | [**inventory_links_history_by_linkid_get**](docs/LinksApi.md#inventory_links_history_by_linkid_get) | **GET** /1.0.0/inventory/links/history/{linkid} | inventorylinkshistorylinkidget
*TopologiesApi* | [**ttms100_topology_tag_by_topotaguuid_delete**](docs/TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_delete) | **DELETE** /ttms/1.0.0/topology_tag/{topotaguuid}/ | ttmstopologytagtopotaguuiddelete
*TopologiesApi* | [**ttms100_topology_tag_by_topotaguuid_get**](docs/TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_get) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/ | ttmstopologytagtopotaguuidget
*TopologiesApi* | [**ttms100_topology_tag_by_topotaguuid_put**](docs/TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_put) | **PUT** /ttms/1.0.0/topology_tag/{topotaguuid}/ | ttmstopologytagtopotaguuidput
*TopologiesApi* | [**ttms100_topology_tag_get**](docs/TopologiesApi.md#ttms100_topology_tag_get) | **GET** /ttms/1.0.0/topology_tag | ttmstopologytagget
*TopologiesApi* | [**ttms100_topology_tag_objects_by_topotaguuid_get**](docs/TopologiesApi.md#ttms100_topology_tag_objects_by_topotaguuid_get) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/objects/ | ttmstopologytagtopotaguuidobjectsget
*TopologiesApi* | [**ttms100_topology_tag_post**](docs/TopologiesApi.md#ttms100_topology_tag_post) | **POST** /ttms/1.0.0/topology_tag | ttmstopologytagpost
*VnfsApi* | [**marketplace_image_add_to_my_images_by_imageid_post**](docs/VnfsApi.md#marketplace_image_add_to_my_images_by_imageid_post) | **POST** /1.0.0/marketplace/image/{imageid}/add_to_my_images/ | marketplaceimageimageidaddtomyimagespost
*VnfsApi* | [**marketplace_image_by_imageid_get**](docs/VnfsApi.md#marketplace_image_by_imageid_get) | **GET** /1.0.0/marketplace/image/{imageid}/ | marketplaceimageimageidget
*VnfsApi* | [**marketplace_image_get**](docs/VnfsApi.md#marketplace_image_get) | **GET** /1.0.0/marketplace/image | marketplaceimageget
*VnfsApi* | [**marketplace_image_my_images_get**](docs/VnfsApi.md#marketplace_image_my_images_get) | **GET** /1.0.0/marketplace/image/my_images/ | marketplaceimagemyimagesget
*VnfsApi* | [**marketplace_image_remove_from_my_images_by_imageid_post**](docs/VnfsApi.md#marketplace_image_remove_from_my_images_by_imageid_post) | **POST** /1.0.0/marketplace/image/{imageid}/remove_from_my_images/ | marketplaceimageimageidremovefrommyimagespost
*VnfsApi* | [**vnfds100_vnf_by_vnfuuid_get**](docs/VnfsApi.md#vnfds100_vnf_by_vnfuuid_get) | **GET** /vnfds/1.0.0/vnf/{vnfuuid}/ | vnfdsvnfvnfuuidget
*VnfsApi* | [**vnfds100_vnf_reboot_by_vnfuuid_post**](docs/VnfsApi.md#vnfds100_vnf_reboot_by_vnfuuid_post) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/reboot | vnfdsvnfvnfuuidrebootpost
*VnfsApi* | [**vnfds100_vnf_resume_by_vnfuuid_post**](docs/VnfsApi.md#vnfds100_vnf_resume_by_vnfuuid_post) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/resume | vnfdsvnfvnfuuidresumepost
*VnfsApi* | [**vnfds100_vnf_suspend_by_vnfuuid_post**](docs/VnfsApi.md#vnfds100_vnf_suspend_by_vnfuuid_post) | **POST** /vnfds/1.0.0/vnf/{vnfuuid}/suspend | vnfdsvnfvnfuuidsuspendpost
*VportsApi* | [**inventory_regularvport_post**](docs/VportsApi.md#inventory_regularvport_post) | **POST** /1.0.0/inventory/regularvport | inventoryregularvportpost
*VportsApi* | [**inventory_vnf_vport_post**](docs/VportsApi.md#inventory_vnf_vport_post) | **POST** /1.0.0/inventory/vnf/vport | inventoryvnfvportpost
*VportsApi* | [**inventory_vport_by_vportuuid_get**](docs/VportsApi.md#inventory_vport_by_vportuuid_get) | **GET** /1.0.0/inventory/vport/{vportuuid} | inventoryvportvportuuidget


## Documentation For Models

 - [AccountcustomeruuidgetResponse](docs/AccountcustomeruuidgetResponse.md)
 - [AuthgeneratetokenpostResponse](docs/AuthgeneratetokenpostResponse.md)
 - [AuthvalidatetokengetResponse](docs/AuthvalidatetokengetResponse.md)
 - [Billing](docs/Billing.md)
 - [Body](docs/Body.md)
 - [Body42](docs/Body42.md)
 - [Body45](docs/Body45.md)
 - [Body51](docs/Body51.md)
 - [Body53](docs/Body53.md)
 - [Body56](docs/Body56.md)
 - [Body58](docs/Body58.md)
 - [Body67](docs/Body67.md)
 - [Body71](docs/Body71.md)
 - [Body72](docs/Body72.md)
 - [Body80](docs/Body80.md)
 - [Classification](docs/Classification.md)
 - [Contract](docs/Contract.md)
 - [Datacenter](docs/Datacenter.md)
 - [Datacenter34](docs/Datacenter34.md)
 - [EisendpointstopologytaguuidtopotaguuidgetResponse](docs/EisendpointstopologytaguuidtopotaguuidgetResponse.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointPort](docs/EndpointPort.md)
 - [Endpointlist](docs/Endpointlist.md)
 - [Error](docs/Error.md)
 - [Flavor](docs/Flavor.md)
 - [GlanceImage](docs/GlanceImage.md)
 - [Image](docs/Image.md)
 - [InventorydatacentersgetException](docs/InventorydatacentersgetException.md)
 - [InventorydatacentersgetResponse](docs/InventorydatacentersgetResponse.md)
 - [InventoryendpointendpointuuidgetResponse](docs/InventoryendpointendpointuuidgetResponse.md)
 - [InventoryendpointscustomeruuidcustomeruuidgetResponse](docs/InventoryendpointscustomeruuidcustomeruuidgetResponse.md)
 - [InventorylinkpostResponse](docs/InventorylinkpostResponse.md)
 - [InventorylinksgetResponse](docs/InventorylinksgetResponse.md)
 - [InventorylinkshistorylinkidgetResponse](docs/InventorylinkshistorylinkidgetResponse.md)
 - [InventorylinkslinkidcontractpostResponse](docs/InventorylinkslinkidcontractpostResponse.md)
 - [InventorylinkslinkidgetResponse](docs/InventorylinkslinkidgetResponse.md)
 - [InventorylinksputResponse](docs/InventorylinksputResponse.md)
 - [InventoryregularendpointpostResponse](docs/InventoryregularendpointpostResponse.md)
 - [InventoryregularvportpostResponse](docs/InventoryregularvportpostResponse.md)
 - [InventoryvnfendpointpostResponse](docs/InventoryvnfendpointpostResponse.md)
 - [InventoryvnfvportpostResponse](docs/InventoryvnfvportpostResponse.md)
 - [Link](docs/Link.md)
 - [Link78](docs/Link78.md)
 - [MarketplaceimagegetResponse](docs/MarketplaceimagegetResponse.md)
 - [MarketplaceimageimageidaddtomyimagespostResponse](docs/MarketplaceimageimageidaddtomyimagespostResponse.md)
 - [MarketplaceimageimageidremovefrommyimagespostResponse](docs/MarketplaceimageimageidremovefrommyimagespostResponse.md)
 - [MarketplaceimagemyimagesgetResponse](docs/MarketplaceimagemyimagesgetResponse.md)
 - [Meta](docs/Meta.md)
 - [Params](docs/Params.md)
 - [Params44](docs/Params44.md)
 - [Params47](docs/Params47.md)
 - [Params50](docs/Params50.md)
 - [Product](docs/Product.md)
 - [Role](docs/Role.md)
 - [SuccessFragment](docs/SuccessFragment.md)
 - [Topology](docs/Topology.md)
 - [TtmstopologytagtopotaguuidobjectsgetResponse](docs/TtmstopologytagtopotaguuidobjectsgetResponse.md)
 - [User](docs/User.md)
 - [Vlan](docs/Vlan.md)
 - [VnfTag](docs/VnfTag.md)
 - [VnfdsvnfvnfuuidgetResponse](docs/VnfdsvnfvnfuuidgetResponse.md)
 - [Vport](docs/Vport.md)
 - [Vportvalue](docs/Vportvalue.md)


## Documentation For Authorization


## auth

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
 - **oAuth2**: oAuth2


