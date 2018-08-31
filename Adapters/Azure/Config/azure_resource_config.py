from . import AzureCredentialConfig


class AzureResourceServiceConfig:
    def __init__(self, subscription_id, creds: AzureCredentialConfig):
        self.CREDENTIALS = creds.get_credentials()
        self.SUBSCRIPTION_ID = subscription_id
