from telegram.client import Telegram, AuthorizationState
import logging

tg = Telegram(
    api_id='4880490',
    api_hash='f823748c0978b3067fd4c355d2ce58ed',
    phone='+375295179613',
    database_encryption_key='changeme1234',
)

state = tg.login(blocking=False)

if state == AuthorizationState.WAIT_CODE:
    # Telegram expects a pin code
    tg.send_code(input('Code: '))
    state = tg.login(blocking=False)  # continue the login process

if state == AuthorizationState.WAIT_REGISTRATION:
    logging.warning('registration')
    state = tg.register_user('test', 'name')
    logging.warning(state)


# docker build . -t testingfork:latest --platform linux/amd64

