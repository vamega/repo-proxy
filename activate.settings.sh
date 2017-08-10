#!/usr/bin/env bash
# App settings go here, they're validated in app.settings

# the AIO_ env variables are used by `adev runserver` when serving your app for development
export AIO_APP_PATH="app/"
export AIO_STATIC_PATH="static/"


# also activate the python virtualenv for convenience, you can remove this if you're python another way
. ~/.miniconda3/bin/activate repo-proxy
