
def authorization(required_role):
    def decorator(func):
        def wrapper(role, *args, **kwargs):
            if role != required_role:
                print("akses di tolak!")
                return
            return func(*args, **kwargs)
        return wrapper
    return decorator

@authorization("admin")
def delete_user():
    print("delete user berhasil")

@authorization("it")
def update_user():
    print("update user")

delete_user("admin")
update_user("it")