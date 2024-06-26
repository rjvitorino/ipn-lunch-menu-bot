from facebook_api import FacebookAPI

def main() -> None:
    fb_api: FacebookAPI = FacebookAPI()
    fb_api.fetch_photo()

if __name__ == "__main__":
    main()