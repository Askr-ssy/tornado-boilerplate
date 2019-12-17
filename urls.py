from handlers.foo import FooHandler
from handlers.ping import PingHandler


url_patterns = [
    (r"/foo", FooHandler),
    (r"/ping",PingHandler)
]
