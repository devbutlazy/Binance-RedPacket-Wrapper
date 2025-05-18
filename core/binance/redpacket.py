import asyncio
import httpx
import random
from datetime import datetime

from core.binance.api import BinanceAPI

from typing import Literal


class RedpacketHandler:
    TYPES = Literal[
        "processed", "claimed", "captcha", "too_many_requests", "session_expired"
    ]

    def __init__(self) -> None:
        self.LAST_TIMESTAMP = 0
        self.PROCESSED_CODES: list = []
        self.IS_TIMEOUT: bool = False
        self.IS_LAST_PROCESSED: bool = True

    async def handle_response(self, response: httpx.Response) -> TYPES:
        """
        Handle the response codes/messages/data an return the according type.

        :response: httpx.Response
        :return: Literal[...]
        """
        response_json = response.json()
        data = response_json.get("data", None)
        code = response_json.get("code", None)

        if response_json["success"]:
            currency = response_json["data"]["currency"]
            amount = response_json["data"]["grabAmountStr"]
            print(f"[ CLAIMED ] {amount} {currency}")
            return "claimed"

        elif data and "validateId" in data:
            print(f"[ WARNING ] Captcha detected: sleeping for 1 hour.")
            return "captcha"

        elif code not in [
            "100002001",
            "403067",
            "403802",
            "403803",
            "PAY4001COM000",
        ]:
            print(f"[ ERROR] An unexpected return type: {response_json}")
            return "processed"

        match code:
            case "100002001":
                print(
                    "Session expired, please re-enter new credentials in core/config.py"
                )
                return "session_expired"
            case "403067":
                print("Too many requests: sleeping for 1 hour")
                return "too_many_requests"
            case "403802":
                print("Redpacket is already fully-claimed.")
                return "processed"
            case "403803":
                print("Invalid repacket code entered.")
                return "processed"
            case "PAY4001COM000":
                print("Invalid repacket code entered.")
                return "processed"

    async def handle_codes(self, code: str) -> None:
        """
        Handle codes fetched from telegram channels

        :code: str
        :return: None
        """
        timestamp = (
            datetime.now().replace(minute=0, second=0, microsecond=0).timestamp()
        )

        if timestamp > self.LAST_TIMESTAMP:
            self.PROCESSED_CODES.clear()
            self.IS_LAST_PROCESSED = True
            self.IS_TIMEOUT = False
            self.LAST_TIMESTAMP = timestamp

        if (code in self.PROCESSED_CODES) or (not self.IS_LAST_PROCESSED):
            return

        if not self.IS_TIMEOUT:
            self.PROCESSED_CODES.append(code)
            self.IS_LAST_PROCESSED = False

            print(f"> Processing {code}...")

            await asyncio.sleep(random.randint(1, 5))
            result: RedpacketHandler.TYPES = await self.handle_response(
                await BinanceAPI.request_redpacket(code)
            )

            match result:
                case "captcha" | "too_many_requests" | "session_expired":
                    self.IS_LAST_PROCESSED = False
                    self.IS_TIMEOUT = True

                case "claimed" | "processed":
                    self.IS_LAST_PROCESSED = True
                    self.PROCESSED_CODES.append(code)

        else:
            print("[ INFO] Sleeping for one hour.")
            self.IS_TIMEOUT = True
            self.IS_LAST_PROCESSED = False
            self.PROCESSED_CODES.clear()
