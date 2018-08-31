from Adapters.Simulators import ServiceFactorySimulator
from Common.Test import TestCase
from Common import scheduler


class TestScheduler(TestCase):

    def test_latest_config_is_picked(self):

        simulated_factory = ServiceFactorySimulator()
        blob_service = simulated_factory.config_container()

        result = scheduler.read_config_from_blob(blob_service)
        self.assertFalse(result is None)

        verify = result['subscriptionId']
        self.assertFalse(verify is None)
