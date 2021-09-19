def make_closure():
    local_mutable = {'foo': 1}
    local_immutable = 2

    def get_foo_plus_two():
        return local_mutable['foo'] + local_immutable

    return get_foo_plus_two


a_closure = make_closure()

__import__('ipdb').set_trace()
