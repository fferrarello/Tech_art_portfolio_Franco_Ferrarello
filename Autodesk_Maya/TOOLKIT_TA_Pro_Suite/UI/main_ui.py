import maya.cmds as cmds
from core.pose_ai import PoseAI
from core.dashboard import Dashboard
from core.debug import DebugTool
from pose_animator import PoseAnimator

class MainUI:

    def __init__(self):
        self.pose = PoseAI()
        self.dashboard = Dashboard()
        self.debug = DebugTool()
	self.animator = PoseAnimator()

    def build(self):

        if cmds.window("TAProSuiteUI", exists=True):
            cmds.deleteUI("TAProSuiteUI")

        window = cmds.window("TAProSuiteUI", title="TA Pro Suite", widthHeight=(400, 500))
        tabs = cmds.tabLayout()

        # POSE TAB
        col1 = cmds.columnLayout(adj=True)
	cmds.button(label="AI Animate (Blocking)",command=self.run_animation_ai)
        cmds.button(label="Pose Up", command=lambda x: self.pose.apply_directional_pose("up"))
        cmds.button(label="Random Pose", command=lambda x: self.pose.random_pose())
	cmds.button(label="AI Prompt Pose",command=lambda x: self.pose.pose_from_prompt(
        cmds.promptDialog(
            title="AI Pose",
            message="Describe la pose:",
            button=["OK", "Cancel"],
            defaultButton="OK",
            cancelButton="Cancel",
            dismissString="Cancel"
        ) == "OK" and cmds.promptDialog(query=True, text=True)
    )
)
        cmds.setParent("..")

        # DASHBOARD TAB
        col2 = cmds.columnLayout(adj=True)
        self.dashboard_field = cmds.scrollField(editable=False)
        cmds.button(label="Scan Scene", command=self.update_dashboard)
        cmds.setParent("..")

        # DEBUG TAB
        col3 = cmds.columnLayout(adj=True)
        self.debug_field = cmds.scrollField(editable=False)
        cmds.button(label="Run Debug", command=self.update_debug)
        cmds.setParent("..")

        cmds.tabLayout(tabs, edit=True, tabLabel=[
            (col1, "Pose AI"),
            (col2, "Dashboard"),
            (col3, "Debug")
        ])

        cmds.showWindow(window)

    def update_dashboard(self, *args):
        text = self.dashboard.scan_scene()
        cmds.scrollField(self.dashboard_field, edit=True, text=text)

    def update_debug(self, *args):
        text = self.debug.run()
        cmds.scrollField(self.debug_field, edit=True, text=text)

   def run_animation_ai(self, *args):

    result = cmds.promptDialog(
        title="AI Animation",
        message="Describe la animación:",
        button=["OK", "Cancel"]
    )

    if result == "OK":
        prompt = cmds.promptDialog(query=True, text=True)
        self.animator.animate_from_prompt(prompt)

   def prompt_ai_pose(self):

   	result = cmds.promptDialog(
        title="AI Pose",
        message="Describe la pose:",
        button=["OK", "Cancel"],
        defaultButton="OK",
        cancelButton="Cancel",
        dismissString="Cancel"
    )

    if result == "OK":
        prompt = cmds.promptDialog(query=True, text=True)
        self.pose.pose_from_prompt(prompt)