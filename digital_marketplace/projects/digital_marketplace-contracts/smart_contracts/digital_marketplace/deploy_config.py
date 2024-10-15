import logging

import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient

logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.digital_marketplace.digital_marketplace_client import (
        DigitalMarketplaceClient,
    )

    app_client = DigitalMarketplaceClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client,
    )

    asset_id = 724221228  # The asset id we want to list
    price = 5000000  # The price we want to list the asset for

    app_client.create_create_application(asset_id=asset_id, unitary_price=price)
    logger.info(f"App {app_client.app_id} deployed by {deployer.address}")
