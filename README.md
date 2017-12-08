# TelstraTPN
Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.

- API version: 2.1.2
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

# Configure OAuth2 access token for authorization: auth
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = TelstraTPN.AuthenticationApi()
grant_type = 'grant_type_example' # str | 
username = 'username_example' # str | 
password = 'password_example' # str | 

try:
    # Create an authentication token
    api_response = api_instance.create_an_authentication_token(grant_type, username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->create_an_authentication_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://penapi.pacnetconnect.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**create_an_authentication_token**](docs/AuthenticationApi.md#create_an_authentication_token) | **POST** /1.0.0/auth/generatetoken | Create an authentication token
*AuthenticationApi* | [**validate_authentication_token**](docs/AuthenticationApi.md#validate_authentication_token) | **GET** /1.0.0/auth/validatetoken | Validate authentication token
*ContractsApi* | [**create_new_contract_on_specified_link**](docs/ContractsApi.md#create_new_contract_on_specified_link) | **POST** /1.0.0/inventory/links/{linkid}/contract | Create new Contract on specified link
*ContractsApi* | [**get_active_contract_by_contract_id**](docs/ContractsApi.md#get_active_contract_by_contract_id) | **GET** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Get active Contract by ContractID
*ContractsApi* | [**update_active_contract_by_contract_id**](docs/ContractsApi.md#update_active_contract_by_contract_id) | **PUT** /1.0.0/inventory/links/{linkid}/contract/{contractid} | Update active Contract by ContractID
*CustomersApi* | [**get_account_information_details**](docs/CustomersApi.md#get_account_information_details) | **GET** /1.0.0/account/{customeruuid} | Get account information details
*CustomersApi* | [**list_users**](docs/CustomersApi.md#list_users) | **GET** /1.0.0/account/{customeruuid}/user | List users
*DatacentresApi* | [**get_list_of_all_the_data_centers**](docs/DatacentresApi.md#get_list_of_all_the_data_centers) | **GET** /1.0.0/inventory/datacenters | Get list of all the data centers
*EndpointsApi* | [**create_physical__port_endpoint**](docs/EndpointsApi.md#create_physical__port_endpoint) | **POST** /1.0.0/inventory/regularendpoint | Create Physical (Port) Endpoint
*EndpointsApi* | [**create_vnf_endpoint**](docs/EndpointsApi.md#create_vnf_endpoint) | **POST** /1.0.0/inventory/vnfendpoint | Create VNF Endpoint
*EndpointsApi* | [**get_information_about_the_specified_endpoint**](docs/EndpointsApi.md#get_information_about_the_specified_endpoint) | **GET** /1.0.0/inventory/endpoint/{endpointuuid} | Get information about the specified endpoint
*EndpointsApi* | [**get_list_of_endpoints_for_a_customer**](docs/EndpointsApi.md#get_list_of_endpoints_for_a_customer) | **GET** /1.0.0/inventory/endpoints/customeruuid/{customeruuid} | Get list of endpoints for a customer
*LinksApi* | [**create_link_and_initial_contract**](docs/LinksApi.md#create_link_and_initial_contract) | **POST** /1.0.0/inventory/link | Create Link and initial Contract
*LinksApi* | [**get_active_links**](docs/LinksApi.md#get_active_links) | **GET** /1.0.0/inventory/links/customer/{customeruuid} | Get active Links
*LinksApi* | [**get_details_of_specified_link**](docs/LinksApi.md#get_details_of_specified_link) | **GET** /1.0.0/inventory/links/{linkid} | Get details of specified link
*LinksApi* | [**get_link_history**](docs/LinksApi.md#get_link_history) | **GET** /1.0.0/inventory/links/history/{linkid} | Get Link history
*TopologiesApi* | [**create_a_named_topology_tag**](docs/TopologiesApi.md#create_a_named_topology_tag) | **POST** /ttms/1.0.0/topology_tag | Create a named topology tag
*TopologiesApi* | [**get_information_about_the_specified_topology_tag**](docs/TopologiesApi.md#get_information_about_the_specified_topology_tag) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/ | Get information about the specified topology tag
*TopologiesApi* | [**list_all_topology_tags**](docs/TopologiesApi.md#list_all_topology_tags) | **GET** /ttms/1.0.0/topology_tag | List all topology tags
*TopologiesApi* | [**list_objects_for_topology**](docs/TopologiesApi.md#list_objects_for_topology) | **GET** /ttms/1.0.0/topology_tag/{topotaguuid}/objects/ | List objects for Topology
*VnfsApi* | [**list_images_in_the_marketplace**](docs/VnfsApi.md#list_images_in_the_marketplace) | **GET** /1.0.0/marketplace/image | List images in the Marketplace
*VportsApi* | [**create_v_port_for_physical_endpoint**](docs/VportsApi.md#create_v_port_for_physical_endpoint) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
*VportsApi* | [**create_vnf_v_port**](docs/VportsApi.md#create_vnf_v_port) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
*VportsApi* | [**get_information_about_the_specified_v_port**](docs/VportsApi.md#get_information_about_the_specified_v_port) | **GET** /1.0.0/inventory/vport/{vportuuid} | Get information about the specified VPort


## Documentation For Models

 - [Billing](docs/Billing.md)
 - [Classification](docs/Classification.md)
 - [Contract](docs/Contract.md)
 - [Datacenter](docs/Datacenter.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointPort](docs/EndpointPort.md)
 - [Endpointlist](docs/Endpointlist.md)
 - [Error](docs/Error.md)
 - [Error70](docs/Error70.md)
 - [Flavor](docs/Flavor.md)
 - [GlanceImage](docs/GlanceImage.md)
 - [Link](docs/Link.md)
 - [Link62](docs/Link62.md)
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
 - [Model100InventoryLinksContractRequest35](docs/Model100InventoryLinksContractRequest35.md)
 - [Model100InventoryLinksContractResponse](docs/Model100InventoryLinksContractResponse.md)
 - [Model100InventoryLinksContractResponse31](docs/Model100InventoryLinksContractResponse31.md)
 - [Model100InventoryLinksContractResponse36](docs/Model100InventoryLinksContractResponse36.md)
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
 - [Object50](docs/Object50.md)
 - [Params](docs/Params.md)
 - [Params29](docs/Params29.md)
 - [Params32](docs/Params32.md)
 - [Params37](docs/Params37.md)
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
- **Scopes**: N/A
