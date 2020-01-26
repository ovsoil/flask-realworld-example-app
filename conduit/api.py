#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import time
from random import randint
from datetime import datetime
from flask import Blueprint, url_for, current_app, send_file, request
from conduit.extensions import cache


blueprint = Blueprint('api', __name__)
JSON_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'json')


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


@blueprint.route('/api/json/<name>', methods=('GET',))
def get_json(name):
    fname = name
    if not fname.endswith('.json'):
        fname += fname + '.json'
    try:
        with open(os.path.join(JSON_DIR, fname), 'r') as fh:
            return json.load(fh)
    except Exception:
        return "json not found", 404


@blueprint.route('/api/json/<name>', methods=('POST',))
def post_json(name):
    fname = name
    if not fname.endswith('.json'):
        fname += fname + '.json'
    data = json.loads(request.data.decode('utf-8'))
    print(fname, data)
    try:
        with open(os.path.join(JSON_DIR, fname), 'w') as fh:
            json.dump(data, fh, indent=2, ensure_ascii=False)
        return data
    except Exception as e:
        print(e)
        return "save json failed", 404
