import logging
import os
from flask import Flask, request, config

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
    logger.info(f'Starting app in environment')
    app = Flask(__name__)
    # app.conf.from_object('conf')
    return app


app = create_app()


@app.route("/")
def hello():
    return """
    <html>
    <body>
      hello ml
   </body>
   </html>
"""


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
