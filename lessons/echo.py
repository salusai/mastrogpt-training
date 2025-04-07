#--web true
def main(args):
    out = args.get("input", "")
    return {
        "body": { "output": out }
    }