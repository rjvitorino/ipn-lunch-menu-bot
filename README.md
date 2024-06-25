# IPN Lunch Menu Bot

![GitHub last commit](https://img.shields.io/github/last-commit/rjvitorino/ipn-lunch-menu-bot)
![GitHub issues](https://img.shields.io/github/issues/rjvitorino/ipn-lunch-menu-bot)
![GitHub pull requests](https://img.shields.io/github/issues-pr/rjvitorino/ipn-lunch-menu-bot)
![GitHub](https://img.shields.io/github/license/rjvitorino/ipn-lunch-menu-bot)

## Overview

`IPN Lunch Menu Bot` is an automated script that fetches the weekly lunch menu from IPN's bar, processes it using ChatGPT, and posts the formatted menu to a specified Slack channel every Monday.

## Features

- **Automated Image Fetching:** Downloads the weekly menu image from a specified Facebook URL.
- **Image Processing with ChatGPT:** Uses OpenAI's ChatGPT to extract and format the menu.
- **Slack Integration:** Posts the formatted menu to a designated Slack channel.
- **Scheduled Execution:** Runs every Monday using GitHub Actions.

## Getting Started

### Prerequisites

- Python 3.10.x
- GitHub account
- Slack workspace and API token
- OpenAI API key

### Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/yourusername/ipn-lunch-menu-bot.git
    cd ipn-lunch-menu-bot
    ```

2. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

3. **Add API Keys to GitHub Secrets**
   - OpenAI API Key: `OPENAI_API_KEY`
   - Slack API Token: `SLACK_API_TOKEN`

### Usage

The script is designed to run automatically every Monday via GitHub Actions. To trigger the workflow manually, you can use the `workflow_dispatch` event in GitHub Actions.

### Configuration

- **Image URL:** Update the URL of the menu image in the `menu_publisher.py` script.
- **Slack Channel:** Update the Slack channel ID in the `menu_publisher.py` script.

### Contributing

Contributions are welcome! Please see our [contributing guidelines](CONTRIBUTING.md) for more information.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements

- [OpenAI](https://openai.com/)
- [Slack API](https://api.slack.com/)

## Contact

If you have any questions, feel free to open an issue or contact me at @rjvitorino.

