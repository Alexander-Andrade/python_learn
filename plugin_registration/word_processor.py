def register(plugins):
    def decorator_register(cls):
        plugins.append(cls)
        return cls
    return decorator_register


class WordProcessor:
    PLUGINS = []

    def process(self, text):
        for plug in self.PLUGINS:
            text = plug().cleanup(text)
        return text
