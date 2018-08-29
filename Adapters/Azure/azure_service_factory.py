from Common.Contracts import ServiceFactory, QueueService, TableStorage
from .Config import AzureConfig
from . import AzureCosmosDb, AzureStorageQueue, AzureResourceService, AzureResourceServiceConfig

class AzureServiceFactory(ServiceFactory):
    def __init__(self, config:AzureConfig):
        self._config = config
        self._resource_services = dict()

    def table_storage(self):
        return AzureCosmosDb(self._config.get_cosmos_storage_config())

    def queue(self, name):
        return AzureStorageQueue(
            self._config.get_queue_name(),
            self._config.get_storage_config())

    def _create_resource_service(self, subscription_id):
        return AzureResourceService(self._config.get_resource_config(subscription_id))
    
    def resource_service(self, subscription_id):
        if subscription_id not in self._resource_services:
            self._resource_services[subscription_id] = self._create_resource_service(subscription_id)
        return self._resource_services[subscription_id]
