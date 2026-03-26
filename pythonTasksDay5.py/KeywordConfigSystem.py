
def system_config(**settings):
    for key, value in settings.items():
        print(key, ":", value)
system_config(mode="debug", version="1.0")