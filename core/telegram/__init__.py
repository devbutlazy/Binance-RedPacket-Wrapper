from telethon import TelegramClient, events

from source import Config
from source import custom_print
from lib.manipulator import ManipulateToken


class BaseClient:
    def __init__(self):
        self.config: Config = Config()
        self.client: TelegramClient = TelegramClient(
            self.config.CLIENT_NAME, self.config.API_ID, self.config.API_HASH
        )
        self.manipulator = ManipulateToken()
        self.setup_event_handler()

    def setup_event_handler(self):
        @self.client.on(events.NewMessage(chats=self.config.CHATS))
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
                        return
                    token = event.raw_text.strip()

                await self.manipulator.main(token)
            except TimeoutError:
                custom_print(
                    "An unexpected error occurred while fetching a message", "error"
                )
                await self.manipulator.main(token)
            except TimeoutError:
                custom_print(
                    "An unexpected error occurred while fetching a message", "error"
                )

    def start(self):
        custom_print("Starting the proccesses...", "info")
        self.client.start()
        custom_print("Telethon started, waiting for messages", "info")
        self.client.run_until_disconnected()
