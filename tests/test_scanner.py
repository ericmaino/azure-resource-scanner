import logging

from Common import ResourceScanner
from Common.Contracts import Queue
from Adapters.Simulators import ServiceFactorySimulator
from Common.Test import TestCase


class LoggingQueue(Queue):
    def push(self, message):
        logging.info(message)

    def pop(self):
        raise NotImplementedError("Should have implemented pop")

    def peek(self):
        raise NotImplementedError("Should have implemented peek")


class TestScanner(TestCase):

    def test_scanner(self):
        data = {
            "subscriptionId" : "808b8977-950a-4a96-8229-b48d708aa455",
            "typeName" : "storage"
        }
        factory = ServiceFactorySimulator()
        ResourceScanner(factory, LoggingQueue()).execute(data)
