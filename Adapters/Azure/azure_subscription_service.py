from Common.Contracts.account_service import AccountService
from azure.mgmt.resource.subscriptions import SubscriptionClient
from .Config import AzureCredentialConfig


class AzureSubscriptionService(AccountService):

    def __init__(self, config:AzureCredentialConfig):
        self._client = SubscriptionClient(config.get_credentials())

    def get_accounts(self):
        return [sub.serialize(True) for sub in self._client.subscriptions.list()]
