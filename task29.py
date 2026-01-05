def get_active_users(users):
    result = []

    for name, info in users.items():
        if info["active"] == True:
            result.append(name)

    return result

users = {
    "Ali": {"active": True, "email": "ali@gmail.com"},
    "Vali": {"active": False, "email": "vali@gmail.com"},
    "Sami": {"active": True, "email": "sami@gmail.com"}
}

result = get_active_users(users)
print(result)
