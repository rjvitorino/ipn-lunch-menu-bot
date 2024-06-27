from typing import Dict

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.business import Business
import requests

from config import Config

class FacebookAPI:
    def __init__(self) -> None:
        self.app_id: str = Config.FACEBOOK_APP_ID
        self.app_secret: str = Config.FACEBOOK_APP_SECRET
        self.base_url: str = "https://graph.facebook.com/v11.0"


    def get_app_access_token(self) -> str:
        """
        Get the app access token using app ID and app secret.

        :param app_id: The App ID from Facebook Developer account.
        :param app_secret: The App Secret from Facebook Developer account.
        :return: The app access token as a string.
        """
        url: str = 'https://graph.facebook.com/oauth/access_token'
        params: Dict[str, str] = {
            'client_id': self.app_id,
            'client_secret': self.app_secret,
            'grant_type': 'client_credentials'
        }
        response: requests.Response = requests.get(url, params=params)
        data: Dict[str, str] = response.json()
        if 'access_token' in data:
            return data['access_token']
        else:
            raise Exception("Could not retrieve access token: " + data.get('error', {}).get('message', 'Unknown error'))

    def get_photos_from_page(self, page_id: str, access_token: str) -> Dict[int, str]:
        """
        Get photo URLs from a Facebook page.

        :param page_id: The ID of the Facebook page.
        :param access_token: The access token to authenticate the request.
        :return: A dictionary mapping photo index to photo URL.
        """
        FacebookAdsApi.init(access_token=access_token)
        page: Business = Business(page_id)
        fields: list = ['photos{images}']
        photos = page.api_get(fields=fields)

        photo_urls: Dict[int, str] = {}
        if 'photos' in photos:
            for idx, photo in enumerate(photos['photos']['data']):
                photo_urls[idx] = photo['images'][0]['source']

        return photo_urls

