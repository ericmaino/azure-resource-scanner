import json
import azure.functions
from Adapters.Azure import AzureConfig, AzureServiceFactory
from Common import ResourceScanner, Config
import logging


def read_as_json(msg: azure.functions.QueueMessage):
    msg_body = msg.get_body().decode('utf-8')
    return json.loads(msg_body)


def main(msg: azure.functions.QueueMessage):
    config = Config()
    azure_config = AzureConfig(config)
    factory = AzureServiceFactory(azure_config)
    next_queue = factory.queue('AZURE_STORAGE_QUEUE_NAME')
    ResourceScanner(factory, next_queue).execute(read_as_json(msg))
