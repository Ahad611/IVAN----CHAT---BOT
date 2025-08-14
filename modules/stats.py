from collections import defaultdict

stats_data = defaultdict(int)

def log_message(user_id: int):
    stats_data[user_id] += 1

def get_stats():
    return dict(stats_data)
