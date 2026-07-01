import re
patterns = {
    "ipv4": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",

    "domain": r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",

    "url": r"https?://[^\s]+",

    "email": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",

    "md5": r"\b[a-fA-F0-9]{32}\b",

    "sha1": r"\b[a-fA-F0-9]{40}\b",

    "sha256": r"\b[a-fA-F0-9]{64}\b",

    "cve": r"\bCVE-\d{4}-\d{4,7}\b",
}

def extract_iocs(text: str) -> dict:
    results = {}
    for ioc_type, pattern in patterns.items():
        matches = re.findall(pattern,text)
        results[ioc_type] = matches 
    return results
