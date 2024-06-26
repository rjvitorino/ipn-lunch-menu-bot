from config.config import Config

class FacebookAPI:
    def __init__(self) -> None:
        self.access_token: str = Config.FACEBOOK_ACCESS_TOKEN
        self.base_url: str = "https://graph.facebook.com/v11.0"

    def fetch_photo() -> None:
        pass
