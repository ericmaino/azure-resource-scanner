from abc import ABC, abstractmethod


class QueueService(ABC):

    @abstractmethod
    def create_queue(self, queue_name):
        raise NotImplementedError("Should have implemented create_queue")
