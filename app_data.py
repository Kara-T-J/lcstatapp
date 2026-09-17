from services.data_access import load_data
from services.workload_service import data_preparation

import config as cfg

tasks_df = data_preparation(load_data(cfg.CSV_NAME, cfg.CSV_PATH, cfg.COLUMNS), cfg.PROJECT_MAPPING, cfg.TASK_MAPPING, cfg.WORKLOAD_MAPPING)