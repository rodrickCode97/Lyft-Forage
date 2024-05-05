def add_yrs_to_date(original_date, years_to_add):
    res = original_date.replace(year=original_date.year + years_to_add)
    return res