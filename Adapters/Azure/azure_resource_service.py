from azure.mgmt.resource import ResourceManagementClient
from Common.Contracts import ResourceService, ResourceFilter
from .Config import AzureResourceServiceConfig
import logging

class NoFilter(ResourceFilter):
    def normalized_filter(self):
        return None

class AzureResourceTypeFilter(ResourceFilter):
    def __init__(self, resourceType):
        self._filter = "resourceType eq '" + resourceType + "'"
    
    def normalized_filter(self):
        return self._filter

class AzureResourceService(ResourceService):
    def __init__(self, config:AzureResourceServiceConfig):
        self._client = ResourceManagementClient(config.CREDENTIALS, config.SUBSCRIPTION_ID)
        self._resource_type_apis = dict()
        
        self._knownTypes = {
            'vm' : 'Microsoft.Compute/virtualMachines',
            'storage' : 'Microsoft.Storage/storageAccounts'
        }

    def get_resources(self, filter:ResourceFilter):
        result = [resource.serialize(True) for resource in self._client.resources.list(expand="tags", filter=filter.normalized_filter())]
        return result
    
    def get_filter(self, payload):
        try:
            resourceType = self._knownTypes[payload.lower()]
            return AzureResourceTypeFilter(resourceType)
        except AttributeError:
            return NoFilter()
        except KeyError:
            logging.warn("The filter " + payload + " is not supported and will be ignored")
            return NoFilter()            
        else:
            raise NotImplementedError("The payload " + payload + " is not a supported filter")
    
    def update_resource(self, resource):
        api_version = self._resolve_api_for_resource_type(resource['type'])
        if api_version is None:
            raise Exception(f"Unabled to find api version to update {resource['id']}")
        
        self._client.resources.update_by_id(resource['id'], api_version, resource)
    

    # Internal Helper function to resolve API version to access Azure with
    def _resolve_api_for_resource_type(self, resource_type):
        if resource_type in self._resource_type_apis:
            return self._resource_type_apis[resource_type]
        
        resource_type_info = resource_type.split('/', 1)
        resource_provider = resource_type_info[0]
        resource_provider_type = resource_type_info[1]

        provider = self._client.providers.get(resource_provider)
        provider_details = next((t for t in provider.resource_types
            if t.resource_type == resource_provider_type), None)
        
        if provider_details and 'api_versions' in provider_details.__dict__:
            # Remove preview API versions
            api_version = [v for v in provider_details.__dict__['api_versions'] if 'preview' not in v.lower()]
            # Get most recent remaining API
            chosen_api = api_version[0] if api_version else provider_details.__dict__['api_versions'][0]
            self._resource_type_apis[resource_type] = chosen_api

            return chosen_api

        return None
