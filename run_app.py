from aiohttp.web import run_app
from application.app import setup_application
from application.utils.argparser import setup_args


if __name__ == "__main__":
    args = setup_args()
    myApp = setup_application(pg_url=args.pg_url)
    run_app(myApp, host=args.host, port=args.port)
