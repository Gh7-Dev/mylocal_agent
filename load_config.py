import tomllib

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

print(config["model"]["name"])
print(config["model"]["num_thread"])