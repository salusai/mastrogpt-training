
import chat

def assistant(args):
    print(args)
    ch = chat.Chat(args)
    output = f"Welcome to {chat.MODEL}"
    input = args.get("input", "")
    if input != "":
        ch.prompt("user", input)
        output = ch.chat(input)
    return { "output": output, "state": ch.state() }
