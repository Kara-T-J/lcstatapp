import domain.team as team

def add_workload(df, workload_mapping):
    df_workload = df.copy(deep = True)
    df_workload["Workload"] = (
        df_workload["Size"].astype("string")
        .str.strip()
        .str.upper()
        .map(workload_mapping)
        .fillna(0)
    )
    return df_workload

def task_count(df):
    return len(df)

def total_workload(df):
    return df["Workload"].sum()

def workload_by_date(df):
    return (
        df.groupby(
            "Due Date",
            as_index=False,
        )["Workload"]
        .sum()
        .sort_values("Due Date")
    )

def average_workload(df):
    daily_workload = (
        df.groupby("Due Date")["Workload"]
        .sum()
    )
    if daily_workload.empty:
        return 0
    return round(daily_workload.mean(),2)

def teamload_by_date(df):
    wl = workload_by_date(df)
    hc = team.member_per_day(df)

    teamload = wl.merge(
        hc,
        on="Due Date",
        how="left",
    )
    teamload["Teamload"] = (
        teamload["Workload"] / teamload["Headcount"]
    )

    return teamload[["Due Date", "Teamload"]]
    