import httpx

from core.config import config

from typing import Optional


class BinanceAPI:
    def __init__(self) -> None: ...

    async def request_redpacket(self, redpacket_code: str) -> Optional[httpx.Response]:
        """
        Send request to Binance API and call the
        """
        async with httpx.AsyncClient(headers=config.HEADERS) as client:
            try:
                response = await client.post(
                    "https://www.binance.com/bapi/pay/v1/private/binance-pay/gift-box/code/grabV2",
                    json={
                        "channel": "DEFAULT",
                        "grabCode": redpacket_code,
                        "scene": None,
                    },
                )
                return response
            except BaseException as error:
                print(
                    f"An unexpected error occured while processing the POST request to Binance API:\n{error=}"
                )
                return None
