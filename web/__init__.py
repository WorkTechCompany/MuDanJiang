from application import app
from web.controller.admin.utils import create_folder

import os


APPS_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(APPS_DIR, 'static/upload')

app.config['UPLOAD_FOLDER'] = "Images"
app.config['ABS_UPLOAD_FOLDER'] = os.path.join(STATIC_DIR, app.config['UPLOAD_FOLDER'])

create_folder(app.config['ABS_UPLOAD_FOLDER'])