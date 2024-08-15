
import inspect

def introspection_info(obj):
    specifications = {}
    specifications['type'] = type(obj).__name__
    attrs = []
    methods = []
    for item in dir(obj):
        value = getattr(obj, item)
        if callable(value):
            methods.append(item)
        else:
            attrs.append(item)
    specifications['attributes'] = attrs
    specifications['methods'] = methods
    some_obj_module = inspect.getmodule(obj)
    if some_obj_module is not None:
        specifications['module'] = some_obj_module.__name__
    else:
        specifications['module'] = 'built-in'
    return specifications

class We_define_Class():

    def __init__(self, name_obj):
        self.name_obj = name_obj

    def any_action(self):
        return self.name_obj ** 2

number_info = introspection_info(42)
print(number_info)

any_string = introspection_info('Hi, hi!')
print(number_info)

any_obj = We_define_Class(25)
any_obj_info = introspection_info(any_obj)
print(any_obj_info)