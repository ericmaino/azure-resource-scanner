import logging

from Common import ResourceScanner
from Common.Contracts import Queue
from Adapters.Simulators import ServiceFactorySimulator, QueueSimulator
from Common.Test import TestCase

class TestScanner(TestCase):

    def test_scanner(self):
        data = {
            "subscriptionId" : "12345678-0000-0000-0000-123412341234",
            "typeName" : "storage"
        }
        factory = ServiceFactorySimulator()
        queue = factory.queue("test_queue")

        ResourceScanner(factory, queue).execute(data)

        try:
            # Trying to peek an empty queue will throw an exception
            queue.peek()
        except:
            logging.error("Expected queue to have a message")
            assert(False)
        
        # Can't implement more detailed tests until we expand resource service simulator
