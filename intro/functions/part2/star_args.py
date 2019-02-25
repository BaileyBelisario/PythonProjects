def ensure_correct_info(*args):
    print(args)
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"
    return "Not sure who you are"

print(ensure_correct_info())

print(ensure_correct_info(1,True,"Steele","Colt"))
