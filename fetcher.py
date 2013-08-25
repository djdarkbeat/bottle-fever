#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fetcher script

Created by: Rui Carmo
License: MIT (see LICENSE for details)
"""

import os, sys, time, json, logging, logging.config, itertools

# Make sure our bundled libraries take precedence
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'lib'))

import config, utils

# read configuration file
config.settings = utils.get_config(os.path.join(utils.path_for('etc'),'config.json'))

# Set up logging
logging.config.dictConfig(dict(config.settings.logging))
log = logging.getLogger()

# load modules
import models, controllers
models.setup()
models.setup_index()


import utils.jobs
import tasks.workers

def grouper(n, iterable):
    it = iter(iterable)
    while True:
       chunk = tuple(itertools.islice(it, n))
       if not chunk:
           return
       yield chunk

if __name__ == "__main__":
    log.info("Starting fetcher.")
    start = time.time()
    utils.jobs.max_workers = config.settings.fetcher.pool
    tasks.workers.control_worker()
    utils.jobs.start()
    log.info("Done in %fs" % (time.time() - start))

