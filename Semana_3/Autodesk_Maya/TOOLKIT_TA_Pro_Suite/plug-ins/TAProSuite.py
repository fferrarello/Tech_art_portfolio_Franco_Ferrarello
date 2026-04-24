import maya.api.OpenMaya as om
import maya.cmds as cmds
import sys
import os

# Path setup
def add_script_path():
    base_path = os.path.dirname(os.path.dirname(__file__))
    scripts_path = os.path.join(base_path, "scripts")

    if scripts_path not in sys.path:
        sys.path.append(scripts_path)

# Command
def run_tool():
    add_script_path()

    import main
    main.run()

# Plugin command class
class TAProSuiteCmd(om.MPxCommand):

    COMMAND_NAME = "TAProSuite"

    def __init__(self):
        super(TAProSuiteCmd, self).__init__()

    def doIt(self, args):
        run_tool()

# Initialize plugin
def initializePlugin(plugin):
    fnPlugin = om.MFnPlugin(plugin)

    try:
        fnPlugin.registerCommand(
            TAProSuiteCmd.COMMAND_NAME,
            TAProSuiteCmd
        )
    except:
        om.MGlobal.displayError("Error registering command")

    create_shelf_button()

# Uninitialize plugin
def uninitializePlugin(plugin):
    fnPlugin = om.MFnPlugin(plugin)

    try:
        fnPlugin.deregisterCommand(TAProSuiteCmd.COMMAND_NAME)
    except:
        om.MGlobal.displayError("Error deregistering command")

# =========================
# UI INTEGRATION (SHELF)
# =========================
def create_shelf_button():

    shelf = "Custom"

    if not cmds.shelfLayout(shelf, exists=True):
        cmds.shelfLayout(shelf)

    cmds.shelfButton(
        parent=shelf,
        label="TAPro",
        command="TAProSuite",
        annotation="TA Pro Suite",
        image="commandButton.png"
    )