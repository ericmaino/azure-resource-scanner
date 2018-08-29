from Common import Config
from . import AzureResourceServiceConfig
from . import AzureCredentialConfig
from . import AzureStorageConfig
from . import AzureCosmosDbConfig

class AzureConfig:
    def __init__(self, config:Config):
        self._config = config

    def get_credentials(self):
        return AzureCredentialConfig(
            self._config.get_property('AZURE_CLIENT_ID'),
            self._config.get_property('AZURE_TENANT_ID'),
            self._config.get_property('AZURE_CLIENT_SECRET')
        )
    
    def get_resource_config(self, subscription_id):
        return AzureResourceServiceConfig(
            subscription_id,
            self.get_credentials()
        )
    
    def get_storage_config(self):
        return AzureStorageConfig(
            self._config.get_property('AZURE_STORAGE_ACCOUNT'),
            self._config.get_property('AZURE_STORAGE_KEY')
        )
    
    def get_cosmos_storage_config(self):
        return AzureCosmosDbConfig(
            self._config.get_property('AZURE_COSMOS_TABLE'),
            AzureStorageConfig(
                self._config.get_property('AZURE_COSMOS_ACCOUNT'),
                self._config.get_property('AZURE_COSMOS_KEY')
            ))

    def get_queue_name(self):
        return self._config.get_property('AZURE_STORAGE_QUEUE_NAME')
