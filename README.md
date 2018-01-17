[![Build Status](https://travis-ci.org/telstra/Programmable-Network-SDK-python.svg?branch=master)]
(https://travis-ci.org/telstra/Programmable-Network-SDK-python)

# Telstra Programmable Network
Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.

- API version: 2.1.3
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
    # Create an authentication token
    api_response = api_instance.auth_generatetoken_post(grant_type, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->auth_generatetoken_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://penapi.pacnetconnect.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**auth_generatetoken_post**](docs/AuthenticationApi.md#auth_generatetoken_post) | **POST** /1.0.0/auth/generatetoken | Create an authentication token
*AuthenticationApi* | [**auth_validatetoken_get**](docs/AuthenticationApi.md#auth_validatetoken_get) | **GET** /1.0.0/auth/validatetoken | Validate authentication token
*ContractsApi* | [**inventory_links_contract_by_linkid_and_contractid_get**](docs/ContractsApi.md#inventory_links_contract_by_linkid_and_contractid_get) | **GET** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Get active Contract by ContractID
*ContractsApi* | [**inventory_links_contract_by_linkid_and_contractid_put**](docs/ContractsApi.md#inventory_links_contract_by_linkid_and_contractid_put) | **PUT** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Update active Contract by ContractID
*ContractsApi* | [**inventory_links_contract_by_linkid_post**](docs/ContractsApi.md#inventory_links_contract_by_linkid_post) | **POST** /1.0.0/inventory/links/{linkid}/contract | Create new Contract on specified link
*CustomersApi* | [**account_by_customeruuid_get**](docs/CustomersApi.md#account_by_customeruuid_get) | **GET** /1.0.0/account/{customeruuid} | Get account information details
*CustomersApi* | [**account_user_by_customeruuid_get**](docs/CustomersApi.md#account_user_by_customeruuid_get) | **GET** /1.0.0/account/{customeruuid}/user | List users
*DatacentresApi* | [**inventory_datacenters_get**](docs/DatacentresApi.md#inventory_datacenters_get) | **GET** /1.0.0/inventory/datacenters | Get list of all the data centers
*EndpointsApi* | [**eis100_endpoints_assign_topology_tag_by_endpointuuid_post**](docs/EndpointsApi.md#eis100_endpoints_assign_topology_tag_by_endpointuuid_post) | **POST** /eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag | Assign a Topology Tag to an Endpoint
*EndpointsApi* | [**inventory_endpoint_by_endpointuuid_get**](docs/EndpointsApi.md#inventory_endpoint_by_endpointuuid_get) | **GET** /1.0.0/inventory/endpoint/{endpointuuid} | Get information about the specified endpoint
*EndpointsApi* | [**inventory_endpoints_customeruuid_by_customeruuid_get**](docs/EndpointsApi.md#inventory_endpoints_customeruuid_by_customeruuid_get) | **GET** /1.0.0/inventory/endpoints/customeruuid/{customeruuid} | Get list of endpoints for a customer
*EndpointsApi* | [**inventory_regularendpoint_post**](docs/EndpointsApi.md#inventory_regularendpoint_post) | **POST** /1.0.0/inventory/regularendpoint | Create Physical (Port) Endpoint
*EndpointsApi* | [**inventory_vnfendpoint_post**](docs/EndpointsApi.md#inventory_vnfendpoint_post) | **POST** /1.0.0/inventory/vnfendpoint | Create VNF Endpoint
*LinksApi* | [**inventory_link_post**](docs/LinksApi.md#inventory_link_post) | **POST** /1.0.0/inventory/link | Create Link and initial Contract
*LinksApi* | [**inventory_links_by_linkid_get**](docs/LinksApi.md#inventory_links_by_linkid_get) | **GET** /1.0.0/inventory/links/{linkid} | Get details of specified link
*LinksApi* | [**inventory_links_customer_by_customeruuid_get**](docs/LinksApi.md#inventory_links_customer_by_customeruuid_get) | **GET** /1.0.0/inventory/links/customer/{customeruuid} | Get active Links
*LinksApi* | [**inventory_links_history_by_linkid_get**](docs/LinksApi.md#inventory_links_history_by_linkid_get) | **GET** /1.0.0/inventory/links/history/{linkid} | Get Link history
*TopologiesApi* | [**ttms100_topology_tag_by_topotaguuid_delete**](docs/TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_delete) | **DELETE** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Delete a topology tag
*TopologiesApi* | [**ttms100_topology_tag_by_topotaguuid_get**](docs/TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_get) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Get information about the specified topology tag
*TopologiesApi* | [**ttms100_topology_tag_by_topotaguuid_put**](docs/TopologiesApi.md#ttms100_topology_tag_by_topotaguuid_put) | **PUT** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Update a topology tag&#39;s name and/or description
*TopologiesApi* | [**ttms100_topology_tag_get**](docs/TopologiesApi.md#ttms100_topology_tag_get) | **GET** /ttms/1.0.0/topology_tag | List all topology tags
*TopologiesApi* | [**ttms100_topology_tag_objects_by_topotaguuid_get**](docs/TopologiesApi.md#ttms100_topology_tag_objects_by_topotaguuid_get) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/objects/ | List objects for Topology
*TopologiesApi* | [**ttms100_topology_tag_post**](docs/TopologiesApi.md#ttms100_topology_tag_post) | **POST** /ttms/1.0.0/topology_tag | Create a named topology tag
*VnfsApi* | [**marketplace_image_get**](docs/VnfsApi.md#marketplace_image_get) | **GET** /1.0.0/marketplace/image | List images in the Marketplace
*VportsApi* | [**inventory_regularvport_post**](docs/VportsApi.md#inventory_regularvport_post) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
*VportsApi* | [**inventory_vnf_vport_post**](docs/VportsApi.md#inventory_vnf_vport_post) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
*VportsApi* | [**inventory_vport_by_vportuuid_get**](docs/VportsApi.md#inventory_vport_by_vportuuid_get) | **GET** /1.0.0/inventory/vport/{vportuuid} | Get information about the specified VPort


## Documentation For Models

 - [Billing](docs/Billing.md)
 - [Classification](docs/Classification.md)
 - [Contract](docs/Contract.md)
 - [Datacenter](docs/Datacenter.md)
 - [Eis100EndpointsAssignTopologyTagRequest](docs/Eis100EndpointsAssignTopologyTagRequest.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointPort](docs/EndpointPort.md)
 - [Endpointlist](docs/Endpointlist.md)
 - [Error](docs/Error.md)
 - [Error74](docs/Error74.md)
 - [Flavor](docs/Flavor.md)
 - [GlanceImage](docs/GlanceImage.md)
 - [Link](docs/Link.md)
 - [Link66](docs/Link66.md)
 - [Meta](docs/Meta.md)
 - [Model100AccountResponse](docs/Model100AccountResponse.md)
 - [Model100AuthGeneratetokenResponse](docs/Model100AuthGeneratetokenResponse.md)
 - [Model100AuthValidatetokenResponse](docs/Model100AuthValidatetokenResponse.md)
 - [Model100InventoryDatacenters401Error](docs/Model100InventoryDatacenters401Error.md)
 - [Model100InventoryDatacentersResponse](docs/Model100InventoryDatacentersResponse.md)
 - [Model100InventoryEndpointResponse](docs/Model100InventoryEndpointResponse.md)
 - [Model100InventoryEndpointsCustomeruuidResponse](docs/Model100InventoryEndpointsCustomeruuidResponse.md)
 - [Model100InventoryLinkRequest](docs/Model100InventoryLinkRequest.md)
 - [Model100InventoryLinkResponse](docs/Model100InventoryLinkResponse.md)
 - [Model100InventoryLinksContractRequest](docs/Model100InventoryLinksContractRequest.md)
 - [Model100InventoryLinksContractRequest37](docs/Model100InventoryLinksContractRequest37.md)
 - [Model100InventoryLinksContractResponse](docs/Model100InventoryLinksContractResponse.md)
 - [Model100InventoryLinksContractResponse33](docs/Model100InventoryLinksContractResponse33.md)
 - [Model100InventoryLinksContractResponse38](docs/Model100InventoryLinksContractResponse38.md)
 - [Model100InventoryLinksHistoryResponse](docs/Model100InventoryLinksHistoryResponse.md)
 - [Model100InventoryLinksResponse](docs/Model100InventoryLinksResponse.md)
 - [Model100InventoryRegularendpointRequest](docs/Model100InventoryRegularendpointRequest.md)
 - [Model100InventoryRegularendpointResponse](docs/Model100InventoryRegularendpointResponse.md)
 - [Model100InventoryRegularvportRequest](docs/Model100InventoryRegularvportRequest.md)
 - [Model100InventoryRegularvportResponse](docs/Model100InventoryRegularvportResponse.md)
 - [Model100InventoryVnfVportRequest](docs/Model100InventoryVnfVportRequest.md)
 - [Model100InventoryVnfVportResponse](docs/Model100InventoryVnfVportResponse.md)
 - [Model100InventoryVnfendpointRequest](docs/Model100InventoryVnfendpointRequest.md)
 - [Model100InventoryVnfendpointResponse](docs/Model100InventoryVnfendpointResponse.md)
 - [Model100MarketplaceImageResponse](docs/Model100MarketplaceImageResponse.md)
 - [Object52](docs/Object52.md)
 - [Params](docs/Params.md)
 - [Params31](docs/Params31.md)
 - [Params34](docs/Params34.md)
 - [Params39](docs/Params39.md)
 - [Product](docs/Product.md)
 - [Role](docs/Role.md)
 - [SuccessFragment](docs/SuccessFragment.md)
 - [Topology](docs/Topology.md)
 - [Ttms100TopologyTagObjectsResponse](docs/Ttms100TopologyTagObjectsResponse.md)
 - [Ttms100TopologyTagRequest](docs/Ttms100TopologyTagRequest.md)
 - [User](docs/User.md)
 - [Vlan](docs/Vlan.md)
 - [VnfTag](docs/VnfTag.md)
 - [Vport](docs/Vport.md)
 - [Vportvalue](docs/Vportvalue.md)


## Documentation For Authorization


## auth

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
- **Oauth2**: Oauth2


