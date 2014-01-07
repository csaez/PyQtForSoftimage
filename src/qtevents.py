import sys
# Add this plug-in path to python path
if __sipath__ not in sys.path:
    sys.path.append(__sipath__)

import Qt
Qt.initialize()

from Qt.QtCore import Qt
from Qt.QtGui import QApplication, QCursor, QKeyEvent

from win32com.client import Dispatch as disp
from win32com.client import constants as C
si = disp("XSI.Application")

# Create a mapping of virtual keys
import key_mapping
KEY_MAPPING = key_mapping.get_mapping()


def consumeKey(ctxt, pressed):
    """
    build the proper QKeyEvent from Softimage key event and send the it along to the focused widget
    """
    kcode = ctxt.GetAttribute("KeyCode")
    mask = ctxt.GetAttribute("ShiftMask")

    # Build the modifiers
    modifier = Qt.NoModifier
    if mask and C.siShiftMask:
        if kcode + 300 in KEY_MAPPING:
            kcode += 300

        modifier |= Qt.ShiftModifier

    if mask and C.siCtrlMask:
        modifier |= Qt.ControlModifier

    if mask and C.siAltMask:
        modifier |= Qt.AltModifier

    # Offseting kcode on AltGr mask
    if mask == 6 and kcode + 600 in KEY_MAPPING:
        kcode += 600

    # Generate a Qt Key Event to be processed
    result = KEY_MAPPING.get(kcode)
    if result:
        if pressed:
            event = QKeyEvent.KeyPress
        else:
            event = QKeyEvent.KeyRelease

        if result[2]:
            modifier |= result[2]

        # Send the event along to the focused widget
        QApplication.sendEvent(
            QApplication.instance().focusWidget(), QKeyEvent(event, result[0], modifier, result[1]))


def isFocusWidget():
    """
    return true if the global qApp has any focused widgets
    """
    focus = False
    if QApplication.instance():
        if QApplication.instance().focusWidget():
            window = QApplication.instance().focusWidget().window()
            geom = window.geometry()
            focus = geom.contains(QCursor.pos())

    return focus


def xsi_version():
    """
    Calculate the version number from the string.
    """
    import re
    value = 7.0
    results = re.match(r"[^\d]*\.?(\d+)\.(\d+)", si.Version())
    if results:
        value = float(".".join(results.groups()))
    else:
        print "Softmage version is unknown!"
    del re
    return value

# Softimage plugin registration


def XSILoadPlugin(reg):
    reg.Author = "Steven Caron"
    reg.Name = "QtEvents"
    reg.Major = 0
    reg.Minor = 1

    reg.RegisterEvent("QtEvents_KeyDown", C.siOnKeyDown)
    reg.RegisterEvent("QtEvents_KeyUp", C.siOnKeyUp)

    # register all potential events
    reg.RegisterEvent("QtEvents_Activate", C.siOnActivate)

    reg.RegisterEvent("QtEvents_FileExport", C.siOnEndFileExport)
    reg.RegisterEvent("QtEvents_FileImport", C.siOnEndFileImport)
    #reg.RegisterEvent("QtEvents_CustomFileExport", C.siOnCustomFileExport)
    #reg.RegisterEvent("QtEvents_CustomFileImport", C.siOnCustomFileImport)

    reg.RegisterEvent("QtEvents_RenderFrame", C.siOnEndFrame)
    reg.RegisterEvent("QtEvents_RenderSequence", C.siOnEndSequence)
    # siOnRenderAbort added in 2012?, err v10.0
    if xsi_version() >= 10.0:
        reg.RegisterEvent("QtEvents_RenderAbort", C.siOnRenderAbort)
    reg.RegisterEvent("QtEvents_PassChange", C.siOnEndPassChange)

    reg.RegisterEvent("QtEvents_SceneOpen", C.siOnEndSceneOpen)
    reg.RegisterEvent("QtEvents_SceneSaveAs", C.siOnEndSceneSaveAs)
    reg.RegisterEvent("QtEvents_SceneSave", C.siOnEndSceneSave2)
    reg.RegisterEvent("QtEvents_ChangeProject", C.siOnChangeProject)

    # events added in 2011, err v9.0
    if xsi_version() >= 9.0:
        reg.RegisterEvent("QtEvents_ConnectShader", C.siOnConnectShader)
        reg.RegisterEvent("QtEvents_DisconnectShader", C.siOnDisconnectShader)
        reg.RegisterEvent("QtEvents_CreateShader", C.siOnCreateShader)

    reg.RegisterEvent("QtEvents_SourcePathChange", C.siOnSourcePathChange)

    # the following have a high potential to be expensive/slow
    reg.RegisterEvent("QtEvents_DragAndDrop", C.siOnDragAndDrop)
    reg.RegisterEvent("QtEvents_ObjectAdded", C.siOnObjectAdded)
    reg.RegisterEvent("QtEvents_ObjectRemoved", C.siOnObjectRemoved)
    reg.RegisterEvent("QtEvents_SelectionChange", C.siOnSelectionChange)
    reg.RegisterEvent("QtEvents_ValueChange", C.siOnValueChange)

    # mute immediately. the dialog is responsble for turning the events it
    # needs on
    events = si.EventInfos
    from sisignals import EVENT_MAPPING
    for key, value in EVENT_MAPPING.iteritems():
        event = events(value)
        if si.ClassName(event) == "EventInfo":
            event.Mute = True

    return True


def XSIUnloadPlugin(reg):
    si.LogMessage("%s has been unloaded." % reg.Name, C.siVerbose)
    return True


def QtEvents_KeyDown_OnEvent(ctxt):
    # Block XSI keys from processing, pass along to Qt
    if isFocusWidget():
        consumeKey(ctxt, True)

        # Block the Signal from XSI
        ctxt.SetAttribute("Consumed", True)

    return True


def QtEvents_KeyUp_OnEvent(ctxt):
    # Block XSI keys from processing, pass along to Qt
    if isFocusWidget():
        consumeKey(ctxt, False)

        # Block the Signal from XSI
        ctxt.SetAttribute("Consumed", True)

    return True


def QtEvents_Activate_OnEvent(ctxt):
    from sisignals import signals
    signals.siActivate.emit(ctxt.GetAttribute("State"))


def QtEvents_FileExport_OnEvent(ctxt):
    from sisignals import signals
    signals.siFileExport.emit(ctxt.GetAttribute("FileName"))


def QtEvents_FileImport_OnEvent(ctxt):
    from sisignals import signals
    signals.siFileImport.emit(ctxt.GetAttribute("FileName"))

# def QtEvents_CustomFileExport_OnEvent(ctxt):

# def QtEvents_CustomFileImport_OnEvent(ctxt):


def QtEvents_RenderFrame_OnEvent(ctxt):
    from sisignals import signals
    signals.siRenderFrame.emit(
        ctxt.GetAttribute("FileName"), ctxt.GetAttribute("Frame"))


def QtEvents_RenderSequence_OnEvent(ctxt):
    from sisignals import signals
    signals.siRenderSequence.emit(
        ctxt.GetAttribute("FileName"), ctxt.GetAttribute("Frame"))


def QtEvents_RenderAbort_OnEvent(ctxt):
    from sisignals import signals
    signals.siRenderAbort.emit(
        ctxt.GetAttribute("FileName"), ctxt.GetAttribute("Frame"))


def QtEvents_PassChange_OnEvent(ctxt):
    from sisignals import signals
    signals.siPassChange.emit(ctxt.GetAttribute("TargetPass"))


def QtEvents_SceneOpen_OnEvent(ctxt):
    from sisignals import signals
    signals.siSceneOpen.emit(ctxt.GetAttribute("FileName"))


def QtEvents_SceneSaveAs_OnEvent(ctxt):
    from sisignals import signals
    signals.siSceneSaveAs.emit(ctxt.GetAttribute("FileName"))


def QtEvents_SceneSave_OnEvent(ctxt):
    from sisignals import signals
    signals.siSceneSave.emit(ctxt.GetAttribute("FileName"))


def QtEvents_ChangeProject_OnEvent(ctxt):
    from sisignals import signals
    signals.siChangeProject.emit(ctxt.GetAttribute("NewProjectPath"))


def QtEvents_ConnectShader_OnEvent(ctxt):
    from sisignals import signals
    signals.siConnectShader.emit(
        ctxt.GetAttribute("Source"), ctxt.GetAttribute("Target"))


def QtEvents_DisconnectShader_OnEvent(ctxt):
    from sisignals import signals
    signals.siDisconnectShader.emit(
        ctxt.GetAttribute("Source"), ctxt.GetAttribute("Target"))


def QtEvents_CreateShader_OnEvent(ctxt):
    from sisignals import signals
    signals.siCreateShader.emit(
        ctxt.GetAttribute("Shader"), ctxt.GetAttribute("ProgID"))


def QtEvents_SourcePathChange_OnEvent(ctxt):
    from sisignals import signals
    signals.siSourcePathChange.emit(ctxt.GetAttribute("FileName"))


def QtEvents_DragAndDrop_OnEvent(ctxt):
    from sisignals import signals
    signals.siDragAndDrop.emit(ctxt.GetAttribute("DragSource"))


def QtEvents_ObjectAdded_OnEvent(ctxt):
    from sisignals import signals
    signals.siObjectAdded.emit(ctxt.GetAttribute("Objects"))


def QtEvents_ObjectRemoved_OnEvent(ctxt):
    from sisignals import signals
    signals.siObjectRemoved.emit(ctxt.GetAttribute("Objects"))


def QtEvents_SelectionChange_OnEvent(ctxt):
    from sisignals import signals
    signals.siSelectionChange.emit(ctxt.GetAttribute("ChangeType"))


def QtEvents_ValueChange_OnEvent(ctxt):
    from sisignals import signals
    signals.siValueChange.emit(ctxt.GetAttribute("FullName"))
