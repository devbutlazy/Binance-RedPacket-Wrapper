from dataclasses import dataclass
from typing import Union


@dataclass
class BaseConfig:
    CHATS = [
        -1001515379979,  # Binance Crypto Box Code
        -1001813092752,  # Binance Red packet crypto box
        -1001610472708,  # 🐋 Chat Whale Box 🎁
    ]

    CLIENT_NAME: str = "ClientName"  # Client name | Can be left as now or changed
    API_ID: int = ...  # Telegram API ID
    API_HASH: str = ...  # Telegram API hash

    HEADERS = {
        "User-Agent": "",  # Constant value if logged in from one device
        "bnc-uuid": "",  # Constant value
        "device-info": "",  # Constant value if logged in from one device
        "clienttype": "web",  # Constant value
        "csrftoken": "",
        "fvideo-id": "",  # Constant value
        "fvideo-token": "",
        "x-trace-id": "",
        "x-ui-request-trace": "",
        "lang": "uk-UA",  # Constant value
        "Referer": "https://www.binance.com/uk-UA/my/wallet/account/payment/cryptobox",  # Constant value
        "Cookie": "",
    }

    def __getelement__(self, element: str) -> Union[int, float, bool, str]:
        return getattr(self, element, None)


config = BaseConfig()
