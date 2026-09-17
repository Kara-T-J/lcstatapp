import pandas as pd

import domain.temporal as temporal
import config as cfg


def default_due_date_filter_model():
    return {
        "Due Date": {
            "filterType": "date",
            "type": "greaterThan",
            "dateFrom": temporal.to_date_str(cfg.START_DATE)
        }
    }

def set_prev_month(date):
    prev_month=temporal.time_slide(date, -1, "month")
    start_prev_month = temporal.start_month(prev_month)
    end_prev_month = temporal.end_month(prev_month)
    return temporal.set_due_date_filter_model(start_prev_month, end_prev_month)

def set_next_month(date):
    next_month=temporal.time_slide(date, 1, "month")
    start_next_month = temporal.start_month(next_month)
    end_next_month = temporal.end_month(next_month)
    return temporal.set_due_date_filter_model(start_next_month, end_next_month)