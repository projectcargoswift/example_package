# files/packages/example_package/commands.py  

def greet(user_name):  
    """Vytiskne pozdrav uživateli."""  
    print(f"Hello, {user_name}! Welcome to the example package.")  

# A registrace pro dynamické načítání příkazů  
def register_commands(command_registry):  
    command_registry["greet user"] = greet  
