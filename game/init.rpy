init python:
    def load_module(*paths):
        for path in paths:
            kwargs = {}

            if isinstance(path, (tuple, list, set)):
                path, kwargs = path

            try: renpy.load_module(path, **kwargs)
            except: renpy.load_module(
                "{}/init".format(path), **kwargs)

init python hide:
    store._modules = ()
    try:
        with renpy.file("modules.json") as file:
            import json
            store._modules = tuple(json.load(file))
    except:
        pass

    load_module(*("scripts/{}".format(module) for module in _modules))

label start:
    "Hello World!!!"
    return