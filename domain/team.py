def workload_by_member(df):
    return (
        df.groupby(
            ["Due Date", "Owned By"],
            as_index=False,
        )["Workload"]
        .sum()
    )

def member_per_day(df):
    return (
        df.groupby(
            "Due Date",
            as_index=False,
        )
        .agg(Headcount=("Owned By", "nunique"))
    )