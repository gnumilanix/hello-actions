import os
from greetings import app

if __name__ == '__main__':
    host_env = os.environ.get('FLASK_RUN_HOST', '127.0.0.1')
    is_debug = os.environ.get('FLASK_DEBUG', 'true').lower() == 'true'
    app.run(host=host_env, port=8080, debug=is_debug)