import runpy
from unittest.mock import patch


def test_main_starts_app_with_environment_configuration(monkeypatch):
    monkeypatch.setenv('FLASK_RUN_HOST', '0.0.0.0')
    monkeypatch.setenv('FLASK_DEBUG', 'false')

    with patch('flask.Flask.run') as run:
        runpy.run_path('src/main.py', run_name='__main__')

    run.assert_called_once_with(host='0.0.0.0', port=8080, debug=False)


def test_main_uses_default_configuration(monkeypatch):
    monkeypatch.delenv('FLASK_RUN_HOST', raising=False)
    monkeypatch.delenv('FLASK_DEBUG', raising=False)

    with patch('flask.Flask.run') as run:
        runpy.run_path('src/main.py', run_name='__main__')

    run.assert_called_once_with(host='127.0.0.1', port=8080, debug=True)