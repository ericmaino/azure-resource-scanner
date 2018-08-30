import Common

from azure.storage.blob.blockblobservice import BlockBlobService
from .Config import AzureStorageConfig


class AzureStorageContainer(Common.Contracts.StorageContainer):

    def __init__(self, container_name, config:AzureStorageConfig):
        self._container_name = container_name
        self._blob_service = BlockBlobService(
            account_name=config.account_name,
            account_key=config.account_key
        )
        self._blob_service.create_container(self._container_name)

    def upload_text(self, blob_name, text):
        self._blob_service.create_blob_from_text(self._container_name, blob_name, text)



