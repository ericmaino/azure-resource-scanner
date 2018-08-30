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

        self._knownTypes = {
            'vm' : 'Microsoft.Compute/virtualMachines',
            'storage' : 'Microsoft.Storage/storageAccounts'
        }

    def get_resources(self, filter:ResourceFilter=None):
        result = [resource.serialize(True) for resource in self._client.resources.list(expand="tags", filter=filter.normalized_filter())]
        return result

    def get_filter(self, payload):
        try:
            resourceType = self._knownTypes[payload.lower()]
            return AzureResourceTypeFilter(resourceType)
        except AttributeError:
            return NoFilter()
        except KeyError:
            logging.warning("The filter " + payload + " is not supported and will be ignored")
            return NoFilter()
        except Exception:
            raise NotImplementedError("The payload " + payload + " is not a supported filter")
