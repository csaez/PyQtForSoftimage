import sip
import sys
from PyQt4.QtGui import QWidget, QInputDialog

# Add this plug-in path to python path
if __sipath__ not in sys.path:
    sys.path.append(__sipath__)


def XSILoadPlugin(in_reg):
    in_reg.Name = "PyQt_KeyboardMapping"
    in_reg.Author = "Cesar Saez"
    in_reg.RegisterCommand("PyQt_SetKeyboardMapping")


def PyQt_SetKeyboardMapping_Execute():
    import key_mapping as km
    sianchor = Application.getQtSoftimageAnchor()
    sianchor = sip.wrapinstance(long(sianchor), QWidget)
    languages = km.list_languages()
    lang, ok = QInputDialog.getItem(
        sianchor, "Set PyQt Keyboard Mapping", "Keyboard Mapping",
        languages, languages.index(km.get_language()))
    if ok:
        km.set_language(str(lang))
        Application.UpdatePlugins()
