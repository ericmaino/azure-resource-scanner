import json
import os
import uuid

from Common.Contracts import TableStorage


class TableStorageSimulator(TableStorage):

    def __init__(self):
        self._data = dict()

    def prepare_entry_for_insert(self, json_entry):

        # using location as the partition key. This will keep all the data from
        # the same location on the same node for fastest access
        location = json_entry['location']
        json_entry['PartitionKey'] = location
        json_entry['RowKey'] = str(uuid.uuid3(uuid.NAMESPACE_DNS, json_entry['id']))
        data_to_write = json.dumps(json_entry)
        dict = json.loads(data_to_write)

        # cosmos does not allow for an entry with key 'id'
        modified_data = {}
        for key, value in dict.items():
            if key == 'id':
                modified_data['resourceid'] = str(value)
            else:
                modified_data[key] = str(value)

        return modified_data

    # entry is of json type
    def write(self, entry):
        prepared = self.prepare_entry_for_insert(entry)
        key = entry['PartitionKey'] + '-' + entry['RowKey']
        self._data[key] = entry

    def query(self, partitionkey, rowkey):
        task = self._data[partitionkey + '-' + rowkey]
        return task

    def delete(self, partitionkey, rowkey):
        del self._data[partitionkey + '-' + rowkey]
