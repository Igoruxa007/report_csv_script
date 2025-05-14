from scripts.reports import payout


def test_payout_sorting():
    data = [
        {'department': 'Design', 'name': 'Carol Williams', 'hours_worked': '140', 'hourly_rate': '60'},
        {'department': 'Marketing', 'name': 'Alice Johnson', 'hours_worked': '160', 'hourly_rate': '50'},
        {'department': 'Design', 'name': 'Bob Smith', 'hours_worked': '150', 'hourly_rate': '40'},
    ]

    sorted_data = payout(data)

    expected_sorted_data = [
        {'department': 'Design', 'name': 'Bob Smith', 'hours_worked': '150', 'hourly_rate': '40'},
        {'department': 'Design', 'name': 'Carol Williams', 'hours_worked': '140', 'hourly_rate': '60'},
        {'department': 'Marketing', 'name': 'Alice Johnson', 'hours_worked': '160', 'hourly_rate': '50'},
    ]

    assert sorted_data == expected_sorted_data
