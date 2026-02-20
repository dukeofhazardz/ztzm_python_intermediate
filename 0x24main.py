def requires_role(required_role):
    def decorator_function(original_function):
        def wrapper_function(user):
            if user.get("role") == required_role:
                return original_function(user)
            else:
                print("Access denied: insufficient permissions")
        return wrapper_function
    return decorator_function

@requires_role("admin")
def view_dashboard(user):
    print(f"Welcome, {user['name']}! You can view the admin dashboard.")

admin_user = {"name": "Alice", "role": "admin"}
guest_user = {"name": "Bob", "role": "guest"}

view_dashboard(admin_user)
view_dashboard(guest_user)
