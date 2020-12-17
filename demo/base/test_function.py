# 我们创建一个函数，定义参数中一个或多个赋予默认值后，我们可以使用比允许的更少的参数去调用此函数
def def_param_fun(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# 我们可以如下进行调用
# def_param_fun('Do you really want to quit?')


# def_param_fun('Do you really want to quit?', 2)
#
print(def_param_fun('Do you really want to quit?', 2, 'Please, yes or no!'))


# 可变参数也就是我们对于函数中定义的参数是可以一个或多个可以变化的，其中 *args代表着可以传入一个list或者tuple, **args代表着可以传入一个dict。
def variable_fun(kind, *arguments, **keywords):
    print("friend : ", kind, ";")
    print("-" * 40)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# 函数调用
variable_fun("xiaoming",
             "hello xiaoming", "nice to meet you!",
             mother="xiaoma",
             father="xiaoba",
             son="see you")

print('*'*40)
# 借用官网例子 关键字参数允许你调用函数时传入0个或任意个含参数名的参数，这样可以让我们灵活的去进行参数的调用
def key_fun(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This key_fun wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# 函数调用
key_fun(1000)                                          # 1 positional argument
key_fun(voltage=1000)                                  # 1 keyword argument
key_fun(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
key_fun(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
key_fun('a million', 'bereft of life', 'jump')         # 3 positional arguments
key_fun('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
