from datetime import datetime

def year_progress_percentage():
    now = datetime.now()

    start_of_year = datetime(now.year, 1, 1)
    end_of_year = datetime(now.year + 1, 1, 1)

    elapsed = now - start_of_year
    total = end_of_year - start_of_year

    return (elapsed / total) * 100
