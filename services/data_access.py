import pandas as pd

def load_data(name,path,columns):

    csv_candidates = [
        p for p in path.glob("*.csv")
        if name in p.as_posix()
    ]

    if not csv_candidates:
        raise FileNotFoundError(
            f"No CSV found with path containing '{name}'"
        )

    latest_csv_path = max(csv_candidates, key=lambda p: p.stat().st_mtime)

    return pd.read_csv(latest_csv_path,sep="\t",usecols = columns,encoding="utf-16")