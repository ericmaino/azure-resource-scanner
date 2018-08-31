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
    azureConfig = AzureConfig(config)
    factory = AzureServiceFactory(azureConfig)
    nextQueue = factory.queue(azureConfig.get_payload_queue_name())
    ResourceScanner(factory, nextQueue).execute(read_as_json(msg))
