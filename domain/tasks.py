import pandas as pd

def clean_tasks(df):
    df = df.copy()
    df["Creation Date"] = pd.to_datetime(df["Creation Date"], errors="coerce", dayfirst=True).dt.normalize()
    df["Due Date"] = pd.to_datetime(df["Due Date"], errors="coerce", dayfirst=True).dt.normalize()
    external_mask = df["Owned By"].str.startswith("EXTERNAL", na=False)
    df["Owned By"] = df["Owned By"].mask(external_mask, df["Owned By"].str[9:]).str.replace(r"\s*\(.*$", "", regex=True).str.strip()
    return df

def parse_summary(df,prj_mapping,tsk_mapping):
    df = df.copy()
    pattern = r'^\[(?P<project>[^\]]+)\]\[(?P<type>[^\]]+)\]\[(?P<size>[^\]]+)\](?P<name>.*)$'
    parts = df["Summary"].astype("string").str.extract(pattern)
    df[["Project", "Type", "Size"]] = parts[["project", "type", "size"]]
    df["Summary"] = parts["name"].str.strip()
    df["Project"] = df["Project"].replace(prj_mapping)
    df["Type"] = df["Type"].replace(tsk_mapping)
    df["Size"] = df["Size"].astype("string").str.upper()
    df["Type"]=df["Type"].astype("string").str.strip().str.capitalize()
    df["Project"] = df["Project"].astype("string").str.upper()
    return df

def filter_owner(df, owner):
    return df[df["Owned By"] == owner]

def filter_size(df, size):
    return df[df["Size"] == size]

def filter_type(df, type):
    return df[df["Type"] == type]
