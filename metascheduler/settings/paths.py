import os
import sys
import env

PROJECT_PATH  = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(PROJECT_PATH)
sys.path.insert(0, os.path.join(BASE_DIR, "lib"))

if env.DEV_ENV:
    PIPELINE_PATH = "/home/lairdm/workspace/metascheduler/pipelines"
else:
    PIPELINE_PATH = "/data/Modules/MetaScheduler/pipeline/"
