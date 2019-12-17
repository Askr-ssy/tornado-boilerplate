from handlers.base import BaseHandler
import logging

class PingHandler(BaseHandler):
    def get(self):
        logging.info("ping")
        self.write("pong")