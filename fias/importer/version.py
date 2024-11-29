import datetime
import requests

from fias.models import Version

from typing import Dict

from .signals import pre_fetch_version, post_fetch_version

all_source = 'https://fias.nalog.ru/WebServices/Public/GetAllDownloadFileInfo'
last_source = 'https://fias.nalog.ru/WebServices/Public/GetLastDownloadFileInfo'

__all__ = ['fetch_version_info', 'fetch_last_version_info']


def parse_version(item: Dict, update_all=False):
    """
    Записывает строку информации об обновлении в БД
    :param item:
    :param update_all:
    :return:
    """

    ver, created = Version.objects.get_or_create(
        ver=item['VersionId'],
        dumpdate=datetime.datetime.strptime(item['Date'], '%d.%m.%Y').date(),
    )

    if created or update_all:
        setattr(ver, 'complete_gar_url', item['GarXMLFullURL'])
        setattr(ver, 'delta_gar_url', item['GarXMLDeltaURL'])

        ver.save()


def fetch_version_info(update_all=False):
    """
    Получает сведения обо всех доступных обновлениях БД
    :param update_all:
    :return:
    """

    pre_fetch_version.send(object.__class__)

    result = requests.get(all_source)
    if result.status_code == 200:
        for item in result.json():
            parse_version(item, update_all)

    post_fetch_version.send(object.__class__)


def fetch_last_version_info():
    """
    Получает сведения о последнем доступном обновлении БД
    :return:
    """
    pre_fetch_version.send(object.__class__)

    result = requests.get(last_source)
    if result.status_code == 200:
        parse_version(result.json(), update_all=True)

    post_fetch_version.send(object.__class__)
