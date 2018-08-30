from Common.Contracts import ServiceFactory
from Adapters.Azure.Config import AzureConfig
from . import TableStorageSimulator, ResourceServiceSimulator


class ServiceFactorySimulator(ServiceFactory):

    def table_storage(self):
        return TableStorageSimulator()

    def resource_service(self, subscription_id):
        return ResourceServiceSimulator()

    def account_service(self):
        raise NotImplementedError("account_service is not implemented")

    def queue(self, name):
        raise NotImplementedError("queue is not implemented")

    def config_container(self):
        raise NotImplementedError("config_container is not implemented")

    def config_generator(self):
        raise NotImplementedError("config_generator is not implemented")

