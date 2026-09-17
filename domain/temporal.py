import pandas as pd


scale_aliases = {
    "minute": "minutes",
    "minutes": "minutes",
    "heure": "hours",
    "heures": "hours",
    "hour": "hours",
    "hours": "hours",
    "jour": "days",
    "jours": "days",
    "day": "days",
    "days": "days",
    "semaine": "weeks",
    "semaines": "weeks",
    "week": "weeks",
    "weeks": "weeks",
    "mois": "months",
    "month": "months",
    "months": "months",
    "année": "years",
    "années": "years",
    "annee": "years",
    "annees": "years",
    "an": "years",
    "ans": "years",
    "year": "years",
    "years": "years",
}

def last_date(df):
    return df["Due Date"].dropna().max()

def time_slide(start, range, scale):
    normalized_scale = str(scale).strip().lower()

    try:
        offset_name = scale_aliases[normalized_scale]
    except KeyError as error:
        raise ValueError(f"Unsupported time scale: {scale}") from error

    return pd.Timestamp(start) + pd.DateOffset(**{offset_name: range})

def start_month(date):
    return pd.Timestamp(date).normalize().replace(day=1)

def end_month(date):
    return pd.Timestamp(date).normalize().replace(day=pd.Timestamp(date).days_in_month)

def to_date_str(value):
    return pd.Timestamp(value).strftime("%Y-%m-%d")

def set_due_date_filter_model(start_date, end_date):
    return {
        "Due Date": {
            "filterType": "date",
            "type": "inRange",
            "dateFrom": to_date_str(start_date),
            "dateTo": to_date_str(end_date),
        }
    }

def min_max_date(df):
    return {"min":df["Due Date"].min(),"max":df["Due Date"].max()}