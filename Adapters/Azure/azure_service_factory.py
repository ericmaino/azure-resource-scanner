from Common.Contracts import ServiceFactory
from . import AzureCosmosDb, AzureStorageQueue, AzureResourceService
from .azure_subscription_service import AzureSubscriptionService
from .azure_storage_container import AzureStorageContainer
from .azure_config_generator import AzureConfigGenerator

from .Config import AzureConfig


class AzureServiceFactory(ServiceFactory):

    def __init__(self, config:AzureConfig):
        self._config = config

    def table_storage(self):
        return AzureCosmosDb(self._config.get_cosmos_storage_config())

    def queue(self, name):
        return AzureStorageQueue(
            self._config.get_queue_name(),
            self._config.get_storage_config())

    def resource_service(self, subscription_id):
        return AzureResourceService(self._config.get_resource_config(subscription_id))

    def account_service(self):
        return AzureSubscriptionService(self._config.get_credential_config())

    def config_container(self):
        return AzureStorageContainer(self._config.get_config_container_name(), self._config.get_storage_config())

    def config_generator(self):
        return AzureConfigGenerator(self.account_service())
