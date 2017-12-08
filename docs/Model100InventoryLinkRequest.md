# Model100InventoryLinkRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**connections** | **list[str]** |  | [optional] 
**tag** | **str** |  | [optional] 
**latency** | **int** | Latency: 0&#x3D;Low, 1&#x3D;Standard, 2&#x3D;Best Effort | [optional] 
**duration** | **int** | Duration of contract in minutes | [optional] 
**bandwidth** | **int** | Bandwidth in kB/s | [optional] 
**renewal_option** | **int** | Renewal Option: 0&#x3D;Auto Disconnect, 1&#x3D;Auto Renew, 2&#x3D;Pay per hour | [optional] 
**link_type** | **int** | 1&#x3D;VLAN, 2&#x3D;VNF | [optional] 
**topology_tag_uuid** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


