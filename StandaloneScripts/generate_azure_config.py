import json
from datetime import datetime
from Common import Config
from Adapters.Azure import AzureConfig

import click

from Adapters.Azure.azure_service_factory import AzureServiceFactory


def create_blob(azure_factory, json):
    blob_name = 'config-{date:%Y-%m-%d-%H-%M-%S}.json'.format(date=datetime.now())
    config_container = azure_factory.config_container()
    config_container.upload_text(blob_name, json)


@click.command()
@click.option('-t', '--types', type=click.STRING, required=True,
              help="Resource types for which to scan in Azure subscriptions, separated by comma")
@click.option('-f', '--output', type=click.File('w'),
              help="File to store the generated config (default stdout)")
def generate_config_cli(types, output):
    generate_config(types, output)


def generate_config(types, output=None):
    """
    Generate a c7n-org subscriptions config file
    """
    azure_config = AzureConfig(Config())
    azure_factory = AzureServiceFactory(azure_config)
    subscriptions = []
    sub_service = azure_factory.subscription_service()
    for sub in sub_service.get_accounts():
        subscriptions.append({
            'subscriptionId': sub['subscriptionId'],
            'displayName': sub['displayName']
        })
    resource_types = []
    type_list = types.split(',')
    for t in type_list:
        resource_types.append({
            'typeName': t
        })
    create_blob(json.dumps(
        {'subscriptions': subscriptions,
         'resourceTypes': resource_types})
    )
    if output is not None:
        json.dump(
            {'subscriptions': subscriptions,
             'resourceTypes': resource_types}, output)


if __name__ == '__main__':
    generate_config_cli()  # pylint: disable=E1120
