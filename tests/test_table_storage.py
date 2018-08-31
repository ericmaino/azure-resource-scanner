import json
import uuid

from Adapters.Simulators import ServiceFactorySimulator
from Common.Test import TestCase

class test_table_storage(TestCase):
    def test_entry_is_inserted(self):

        simulated_factory = ServiceFactorySimulator()
        storage_table = simulated_factory.table_storage()

        with open('Data\\sampleData.json', 'r') as json_file:
            datastore = json.load(json_file)

            # insert the entry onto Cosmos
            storage_table.write_entries(datastore)

            for data in datastore:
                location = data['location']

                # save partition and row key for access later
                PartitionKey = location
                RowKey= str(uuid.uuid3(uuid.NAMESPACE_DNS, data['id']))

                # verify the entry was written to the table
                retrieved_entry = None
                retrieved_entry = storage_table.query(PartitionKey, RowKey)

                # verify the entry was inserted on Cosmos
                self.assertIsNotNone(retrieved_entry,"No entry was inserted on Cosmos")

                # delete the entry for good practice
                storage_table.delete(PartitionKey,RowKey)
