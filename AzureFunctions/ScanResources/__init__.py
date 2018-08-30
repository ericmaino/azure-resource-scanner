import json
import azure.functions
from Adapters.Azure import AzureConfig, AzureServiceFactory
from Common import ResourceScanner, Config

def read_as_json(msg: azure.functions.QueueMessage):
    msg_body = msg.get_body().decode('utf-8')
    return json.loads(msg_body)

def main(msg: azure.functions.QueueMessage):
    config = Config()
    azureConfig = AzureConfig(config)
    factory = AzureServiceFactory(azureConfig)
    nextQueue = factory.queue('AZURE_STORAGE_QUEUE_NAME')
    ResourceScanner(factory, nextQueue).execute(read_as_json(msg))
