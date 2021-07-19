from aiohttp import web
from application.app import setup_application
from application.utils.argparser import setup_args

args = setup_args()
myApp = setup_application()
web.run_app(myApp, host=args.host, port=args.port)
