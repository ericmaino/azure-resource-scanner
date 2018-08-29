from Common.Contracts import ResourceService

class ResourceServiceSimulator(ResourceService):
    def get_resources(self):
        return [{
                'id': '/subscriptions/808b8977-950a-4a96-8229-b48d708aa455/resourceGroups/ericmai-vsts-devcrews-teams/providers/microsoft.insights/components/devcrewengnot',
                'name': 'devcrewengnot',
                'type': 'microsoft.insights/components',
                'location': 'southcentralus',
                'tags': {
                    'hidden-link:/subscriptions/808b8977-950a-4a96-8229-b48d708aa455/resourceGroups/ericmai-vsts-devcrews-teams/providers/Microsoft.Web/sites/devcrewengnot': 'Resource'
                },
                'kind': 'web'
                }, {
                'id': '/subscriptions/808b8977-950a-4a96-8229-b48d708aa455/resourceGroups/ericmai-vsts-devcrews-teams/providers/Microsoft.ServiceBus/namespaces/csedevcrew',
                'name': 'csedevcrew',
                'type': 'Microsoft.ServiceBus/namespaces',
                'location': 'southcentralus',
                'tags': {},
                'sku': {
                    'name': 'Standard',
                    'tier': 'Standard'
                }
                }, {
                'id': '/subscriptions/808b8977-950a-4a96-8229-b48d708aa455/resourceGroups/ericmai-vsts-devcrews-teams/providers/Microsoft.Storage/storageAccounts/devcrewengnotab6f',
                'name': 'devcrewengnotab6f',
                'type': 'Microsoft.Storage/storageAccounts',
                'location': 'southcentralus',
                'tags': {},
                'kind': 'Storage',
                'sku': {
                    'name': 'Standard_LRS',
                    'tier': 'Standard'
                }
                }, {
                'id': '/subscriptions/808b8977-950a-4a96-8229-b48d708aa455/resourceGroups/ericmai-vsts-devcrews-teams/providers/Microsoft.Web/serverFarms/SouthCentralUSPlan',
                'name': 'SouthCentralUSPlan',
                'type': 'Microsoft.Web/serverFarms',
                'location': 'southcentralus',
                'kind': 'functionapp'
                }, {
                'id': '/subscriptions/808b8977-950a-4a96-8229-b48d708aa455/resourceGroups/ericmai-vsts-devcrews-teams/providers/Microsoft.Web/sites/devcrewengnot',
                'name': 'devcrewengnot',
                'type': 'Microsoft.Web/sites',
                'location': 'southcentralus',
                'kind': 'functionapp'
                }]

    def get_filter(self, payload):
        return None
    
    def update_resource(self, resource):
        return None
