print('------ args ------')


def func_args(*args):
    print('args: ', args)
    tmp = sum(args)
    print('sum = ', tmp)


func_args(0, 1, 2, 3, 4, 5, 6)
func_args(0, 1)
func_args()


print('------ dictionary ------')


def func_kwargs(**kwargs):
    print('kwargs: ', kwargs, ', type: ', type(kwargs))


func_kwargs(key1=1, key2=2, key3=3)
# kwargs:  {'key1': 1, 'key2': 2, 'key3': 3}
