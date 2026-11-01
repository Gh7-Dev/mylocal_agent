import ollama

message = []


while True:
    usersays = input("Enter you message and press (quit) when done\n")
    if usersays == "quit":
        break
    message.append({"role": "user", "content": usersays})
    response = ollama.chat(model="qwen2.5-coder:3b", messages=message)
    reply = response["message"]["content"]
    message.append({"role": "assistant", "content": reply})
    print("Sending: ", message)
    print("Agent: ", reply)
