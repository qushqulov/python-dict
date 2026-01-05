def get_active_users(users):
    result = []
    for name, info in users.items():
        if info["active"]:
            result.append(name)
    return result

