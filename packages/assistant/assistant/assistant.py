
import history

def assistant(args):
    print(args)
    ch = history.Hostory(args)
    output = f"Welcome to {history.MODEL}"
    input = args.get("input", "")
    if input != "":
        ch.prompt("user", input)
        output = ch.chat(input)
    return { "output": output, "state": ch.state() }
