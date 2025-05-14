from typing import List, Dict


def payout(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    sorted_data = sorted(data, key=lambda x: (x['department'], x['hourly_rate']))
    return sorted_data
