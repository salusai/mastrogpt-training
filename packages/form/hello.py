def main(args):
    print("Token:", args.get("token", "<none>"))
    out = f"Hello, {args.get("input", "world")}"
    return {
        "body": out 
    }
