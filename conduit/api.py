#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from random import randint
from datetime import datetime
from flask import Blueprint, url_for, current_app, send_file
from conduit.extensions import cache


blueprint = Blueprint('api', __name__)


@blueprint.route('/')
def index():
    dist_dir = current_app.config['DIST_DIR']
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)


@blueprint.route('/api/random', methods=('GET',))
@cache.cached(timeout=50)
def random():
    time.sleep(2)
    timestamp = datetime.utcnow().isoformat()
    return {
        'data': str(randint(0, 100000)),
        'timestamp': timestamp
    }


@blueprint.route('/api/clear', methods=('GET', 'POST'))
def clear():
    key = 'view/{}'.format(url_for('api.random'))
    ret = cache.delete(key)
    return {
        'data': ret,
    }
