from telethon import TelegramClient, events

from core.config import config
from core.binance.redpacket import RedpacketHandler


class BaseClient:
    def __init__(self):
        self.CLIENT: TelegramClient = TelegramClient(
            config.CLIENT_NAME, config.API_ID, config.API_HASH
        )
        self.HANDLER = RedpacketHandler()
        self.setup_event_handler()

    def setup_event_handler(self) -> None:
        @self.CLIENT.on(events.NewMessage(chats=config.CHATS))
        async def _(event: events.NewMessage.Event):
            try:
                token = ""
                if event.chat_id == -1001610472708:
                    token = event.raw_text[4:13:].strip()

                if event.chat_id in [-1001813092752, -1001515379979]:
                    if (
                        not len(event.raw_text) == 8
                        or len(event.raw_text.split(" ")) > 1
                    ):
                        return None
                    
                    token = event.raw_text.strip()

                await self.HANDLER.handle_codes(token)
            except TimeoutError:
                print("An unexpected error occurred while fetching a message")
                await self.HANDLER.handle_codes(token)

    def start(self)-> None:
        print("Starting the proccesses...")
        self.client.start()
        print("Telethon started, waiting for messages")
        self.client.run_until_disconnected()
