# Backup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_name** | **str** | User-defined name referring to the backup | [optional] 
**uuid** | **str** | UUID of the backup instance | [optional] 
**vnf_uuid** | **str** | UUID of the VNF being backed up | [optional] 
**glance_image_id** | **str** | UUID of the underlying image id for the backup | [optional] 
**backup_schedule_uuid** | **str** |  | [optional] 
**total_interfaces** | **int** | Number of virtual interfaces active when the VNF was backed up | [optional] 
**backup_started_at** | **str** | Time at which backup was started YYYY-MM-DD HH:MM:SS.S | [optional] 
**backup_completed_at** | **str** | Time at which backup was completed YYYY-MM-DD HH:MM:SS.S | [optional] 
**backup_restored_at** | **str** | Time at which backup was most recently restored YYYY-MM-DD HH:MM:SS.S | [optional] 
**backup_restored_by** | **str** | UUID of the user who most recently restored the backup | [optional] 
**replace_backup_uuid** | **str** | UUID of the backup that the current backup replaced | [optional] 
**status** | **str** | Description of the current state of the backup | [optional] 
**status_code** | **str** | \&quot;Unique code representing the current state of the backup:   CRG&#x3D;Creating, CRE&#x3D;Created, DLG&#x3D;Deleting, DEL&#x3D;Deleted,   REG&#x3D;Restoring, ACT&#x3D;Active/Restored\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


