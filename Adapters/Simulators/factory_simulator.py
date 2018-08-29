from Common.Contracts import ServiceFactory

from Adapters.Simulators import ResourceServiceSimulator, TableStorageSimulator

class ServiceFactorySimulator(ServiceFactory):
   
    def table_storage(self):
        return TableStorageSimulator()
    
    def queue(self, name):
        return None
    
    def resource_service(self, subscription_id):
        return ResourceServiceSimulator()
