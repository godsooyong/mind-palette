import argparse
import os
from mind_palette import app

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument(
    '-p', '--port', type=int, default=int(os.environ.get('PORT', 2028))
)
parser.add_argument('-d', '--debug', action='store_true', default=False)


def run():
    args = parser.parse_args()
    host = '0.0.0.0'
    port = args.port

    if args.debug:
        app.run(host=host, port=port, debug=True)
    else:
        app.run(host=host, port=port, debug=False)


if __name__ == '__main__':
    run()
