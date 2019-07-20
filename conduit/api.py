#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from random import randint
from datetime import datetime
from flask import Blueprint, url_for
from conduit.extensions import cache


blueprint = Blueprint('api', __name__)


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
    return str(ret)
