import os
import json


class _JSONDict(dict):

    def __init__(self, fp, *args, **kwds):
        super(_JSONDict, self).__init__(*args, **kwds)
        self.fp = fp
        if os.path.exists(fp):
            with open(self.fp) as fp:
                data = json.load(fp)
            self.update(data)

    def __setitem__(self, key, value):
        super(_JSONDict, self).__setitem__(key, value)
        self.__updatejson__()

    def __delitem__(self, key):
        super(_JSONDict, self).__delitem__(key)
        self.__updatejson__()

    def clear(self):
        super(_JSONDict, self).clear()
        self.__updatejson__()

    def update(self, other):
        super(_JSONDict, self).update(other)
        self.__updatejson__()

    def __updatejson__(self):
        with open(self.fp, "w") as fp:
            json.dump(self, fp, indent=4)

_prefs = _JSONDict(os.path.join(os.path.dirname(__file__), "prefs.json"))


def list_languages():
    return [x.split(".")[-2] for x in os.listdir(os.path.dirname(__file__))
            if not x.startswith("_") and x.endswith(".py")]


def get_mapping():
    lang = _prefs.get("language")
    __import__("key_mapping." + lang)
    return globals().get(lang).KEY_MAPPING


def set_language(lang):
    if lang not in list_languages():
        print "WARNING: " + lang + " key_mapping not found."
        return
    _prefs["language"] = lang


def get_language():
    return _prefs.get("language")
