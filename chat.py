import ollama
import tomllib
with open("config.toml","rb") as f:
    config = tomllib.load(f)

message = []


while True:
    usersays = input("Enter you message and press (quit) when done\n")
    if usersays == "quit":
        break
    message.append({"role": "user", "content":usersays})
    print("Sending: ", message)
    response = ollama.chat(model=config["model"]["name"],messages=message,options={"num_ctx": config["model"]["num_ctx"],"num_thread" : config["model"]["num_thread"]})
    reply = response["message"]["content"]
    message.append({"role": "assistant", "content": reply})
    print("Agent: ", reply)
