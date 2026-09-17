from pathlib import Path
import pandas as pd


CSV_NAME = "Followed Tasks"
CSV_PATH = Path("C:/Users/sej1abt/Downloads")

COLUMNS = ["Summary", "Creation Date", "Due Date", "Owned By"]

PROJECT_MAPPING = {
    "BWA":    "PLATFORM",
    "ESP10_PLATFORM": "PLATFORM",
    "EMB":    "PLATFORM",
    "IPB":    "PLATFORM",
    "Daimler": "MRA2",
    "HEVX":   "VAG",
    "MB":     "MBEAL",
    "MBAEL":  "MBEAL",
    "MBEA":   "MBEAL",
    "MEABL":  "MBEAL",
    "MB.EA-L": "MBEAL",
    "MB-EAL": "MBEAL",
    "MPOF":   "MOPF",
    "MRA2M":  "MOPF",
    "VANXA":  "VANEA",
    "VAN_EA": "VANEA",
    "VS20": "VSXX",
    "VS30": "VSXX"
}

TASK_MAPPING = {
    "Faiultfree" :  "Faultfree",
    "Faul_tfree" :  "Faultfree",
    "Faulfree" :    "Faultfree",
    "Faulltfree" :  "Faultfree",
    "Fault_free" :  "Faultfree",
    "Flahing" : "Flashing",
    "Flahshing" :   "Flashing",
    "Flash" :   "Flashing",
    "Manual_support" :  "Test_Support",
    "Setp" : "Setup",
    "Setu" : "Setup",
    "Test_suppport" : "Test_Support",
    "Testsupport" : "Test_Support",
    "Tools" : "Tool"
}

WORKLOAD_MAPPING = {
    "XS": 0.25,
    "S": 1,
    "M": 2,
    "L": 8
    }

START_DATE = pd.Timestamp("2026-01-06")