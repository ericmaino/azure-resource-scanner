from . import AzureCredentialConfig


class AzureSubscriptionServiceConfig:
    def __init__(self, creds:AzureCredentialConfig):
        self.CREDENTIALS = creds.get_credentials()
