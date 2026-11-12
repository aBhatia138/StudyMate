import math
from datetime import date 

def compound_interest_calculator(
        principal: float,
        annual_rate: float,
        years: float
) -> dict:
    if not all(
        math.isfinite(x) for x in [principal, annual_rate, years]
    ):
        raise ValueError(
            "Inputs must be finite numbers. "
        )

    if principal < 0:
        raise ValueError(
            "Principal cannot be negative. "
        )

    if annual_rate < 0:
        raise ValueError(
            "annual rate of compounding cannot be negative. "
        )

    if years < 0:
        raise ValueError(
            "Years cannot be negative. "
        )

    final_amount = principal *(
        1 + annual_rate / 100
    ) ** years

    interest_earned = final_amount - principal

    return {
        "principal": round(principal,3),
        "annual_rate": annual_rate,
        "years": years,
        "final_amount": round(final_amount,3),
        "interest_earned": round(interest_earned,3)
    }


def percentage_calculator(
        value: float,
        percentage: float
) -> dict:
    #calculate percewntage of a given value

    if not all(math.isfinite(x) for x in [value, percentage]):
        raise ValueError(
            "Imputs must be finite numbers. "
        )

    result = value * percentage / 100

    return {
        "value": value,
        "percentage": percentage,
        "result": round(result,2)
    }


def days_until_exam(exam_date: str) -> dict:
    #Calculate number of days till exam. Dates must be in YYYY-MM-DD format

    try:
        exam = date.fromisoformat(exam_date)

    except:
        raise ValueError(
            "Invalid date. Use YYYY-MM-DD format. "
        )

    today = date.today()

    remaining_days = (exam - today).days

    return {
        "exam_date": exam.isoformat(),
        "days_remaining": remaining_days,
        "exam_has_passed": remaining_days < 0
    }


def generate_study_plan(
        subjects: list,
        available_days: int,
        hours_per_day: float
) -> dict:
    #Generate a simple study plan based on the round-robin strategy
    if not isinstance(subjects, list) or not subjects:
        raise ValueError(
            "Provide atleat one subject. "
        )

    if any(not isinstance(s, str) or not s.strip() for s in subjects):
        raise ValueError(
            "Every subject must be a non-empty string. "
        )

    if (isinstance(available_days, bool) or not isinstance(available_days, int)
        or available_days < 0):
        raise ValueError(
            "Available days must be a positive integer. "
        )

    if isinstance(hours_per_day, bool) or not isinstance(hours_per_day, (int, float)):
        raise ValueError(
            "Hours per day has to be a numeric. "
        )

    if not math.isfinite(hours_per_day) or hours_per_day <= 0:
        raise ValueError(
            "Hours per day must be positive and finite. "
        )

    subjects = list(dict.fromkeys(
        subject.strip() for subject in subjects
    ))

    study_plan = []

    for day in range(available_days):

        subject = subjects[day % len(subjects)];

        study_plan.append({
            "day": day + 1,
            "subject": subject,
            "hours": hours_per_day
        })

    return {
        "total_days": available_days,
        "hours_per_day": hours_per_day,
        "study_plan": study_plan
    }



