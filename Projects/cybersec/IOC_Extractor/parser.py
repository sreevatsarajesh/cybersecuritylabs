def clean_results(results: dict) -> dict:
    cleaned = {}
    for ioc_type,values in results.items():
        unique = set()
        for value in values:
            value = value.strip()
            if ioc_type in ("domain","email"):
                value = value.lower()
            unique.add(value)
        cleaned[ioc_type]=sorted(unique)
    return cleaned