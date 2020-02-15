from word_processor import WordProcessor, register


@register(WordProcessor.PLUGINS)
class RemoveVowelExtension:

    def cleanup(self, text):
        import re
        return re.sub(r'[eyuioa]', '', text)
