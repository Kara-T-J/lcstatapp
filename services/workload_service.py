import domain.tasks as tasks
import domain.workload as workload
import domain.temporal as temporal
import domain.team as team
import pandas as pd

def data_preparation(df, project_mapping, task_mapping, workload_mapping):
    cleaned = tasks.clean_tasks(df)
    parsed = tasks.parse_summary(cleaned, project_mapping, task_mapping)
    return workload.add_workload(parsed, workload_mapping)

def apply_filters(df, filter_state):
    if not filter_state:
        return df

    filtered = df

    owner_filter = filter_state.get("Owned By")
    if owner_filter:
        owner = owner_filter.get("filter")

        if owner:
            filtered = tasks.filter_owner(
                filtered,
                owner,
            )

    type_filter = filter_state.get("Type")
    if type_filter:
        task_type = type_filter.get("filter")

        if task_type:
            filtered = tasks.filter_type(
                filtered,
                task_type,
            )

    date_filter = filter_state.get("Due Date")

    if date_filter:
        date_from = date_filter.get("dateFrom")
        date_to = date_filter.get("dateTo")

        if date_from:
            filtered = filtered[
                filtered["Due Date"] >= pd.Timestamp(date_from)
            ]

        if date_to:
            filtered = filtered[
                filtered["Due Date"] <= pd.Timestamp(date_to)
            ]

    return filtered

def get_overview(df, filter_state=None):
    filtered_df = apply_filters(df, filter_state)

    return {
        "task_count": workload.task_count(filtered_df),
        "total_workload": workload.total_workload(filtered_df),
        "average_workload": workload.average_workload(filtered_df),

        "workload_timeline": workload.workload_by_date(filtered_df),
        "headcount_timeline": team.member_per_day(filtered_df),
        "teamload_timeline":workload.teamload_by_date(filtered_df),
        "by_member": team.workload_by_member(filtered_df),
        "min_date": temporal.min_max_date(filtered_df)["min"].strftime("%d/%m/%Y"),
        "max_date": temporal.min_max_date(filtered_df)["max"].strftime("%d/%m/%Y"),
    }

