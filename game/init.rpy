init python:
    def load_module(*paths, **kwargs):
        fpaths = [
            "{}",
            "{}/init",
        ]

        for path in paths:
            kwrgs = kwargs

            if isinstance(path, (tuple, list, set)):
                path, kwrgs = path
            
            loaded = False
            for fp in fpaths:
                fpath = fp.format(path)
                if renpy.loadable(fpath + ".rpym"):
                    renpy.load_module(fpath, **kwrgs)
                    loaded = True

                if loaded: break

            if not loaded:
                raise Exception("Module '{}' does not exist.".format(path))

init python hide:
    store._modules = ()
    try:
        with renpy.file("modules.json") as file:
            import json
            store._modules = tuple(json.load(file))
    except:
        pass

    load_module(*_modules)

label start:
    "Hello World!!!"
    return