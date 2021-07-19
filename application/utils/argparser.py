import argparse
import yaml
import pathlib


def setup_args():
    parser = argparse.ArgumentParser()

    BASE_DIR = pathlib.Path(__file__).parent.parent
    with open(f"{BASE_DIR}/docs/config_app.yaml", "r") as f:
        config_app = yaml.safe_load(f)
    # app args
    parser.add_argument(
        "-H",
        "--host",
        help="Enter the ip of the server on which it will be launched,\
            only the string is accepted: {0}".format(
            config_app["HOST_APP"]
        ),
        type=str,
        default=config_app["HOST_APP"],
    )
    parser.add_argument(
        "-P",
        "--port",
        help="Enter the port of the server on which it will run: port {0}".format(
            config_app["PORT_APP"]
        ),
        type=int,
        default=config_app["PORT_APP"],
    )
    parser.add_argument(
        "-L",
        "--logger-level",
        help="select level logger. Default: DEBUG.\
            Use: INFO, ERROR, CRITICAL, FATAL",
        type=str,
        default=config_app["LOGGER_LEVEL"].upper(),
    )

    return parser.parse_args()
