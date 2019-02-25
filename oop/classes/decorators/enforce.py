def enforce(*types):
    def decorator(f):
        def new_func(*args,**kwargs):
            newargs = []
            for (a,t) in zip(args, types):
                newargs.append(t(a))
            return f(*newargs,**kwargs)
        return new_func
    return decorator

@enforce(str,int)
def repeat_msg(msg,times):
    for time in range(times):
        print(msg)

repeat_msg('hello','3')
repeat_msg('hello',3)


def new_repeat_msg(msg,times):
    for time in range(int(times)):
        print(str(msg))

new_repeat_msg(5,'5')
