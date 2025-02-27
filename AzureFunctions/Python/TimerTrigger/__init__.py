import datetime
import logging

import azure.functions as func
from azure.storage.blob import BlockBlobService


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    logging.info('Função bkp executada as: %s', utc_timestamp)
    copy_azure_files()

def copy_azure_files():

    blob_service = BlockBlobService(account_name='estudogabriel', account_key='PhtJbbYpbiN3o9zDbYgta0TywlPekVscoUgTVSjMKOWZQ6p6o4GmH3vLRUXylQN7xlgoEjkTR3MCQZudfq0lhw==')

    copy_from_container = 'prod'
    copy_to_container = 'bkp'

    print("\nList blobs in the container")
    listagem = blob_service.list_blobs(copy_from_container)
    for blob in listagem:
        blob_url = blob_service.make_blob_url(copy_from_container, blob.name)
        blob_service.copy_blob(copy_to_container, blob.name, blob_url)
        print(blob.name)