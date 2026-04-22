import maya.cmds as cmds
from pose_library import PoseLibrary
from pose_ai import PoseAI
from pose_blender import PoseBlender

class PoseLibraryUI:

    def __init__(self):
        self.lib = PoseLibrary()
        self.ai = PoseAI()
        self.blender = PoseBlender()

    def build(self):

        if cmds.window("PoseLibUI", exists=True):
            cmds.deleteUI("PoseLibUI")

        win = cmds.window("PoseLibUI", title="Pose Library AI", widthHeight=(300, 400))
        col = cmds.columnLayout(adj=True)

        cmds.text(label="Guardar Pose")
        cmds.button(label="Save Pose", command=self.save_pose)

        cmds.separator(h=10)

        cmds.text(label="Lista de Poses")
        self.pose_list = cmds.textScrollList(allowMultiSelection=False)
        self.refresh_list()

        cmds.button(label="Load Pose", command=self.load_pose)

        cmds.separator(h=10)

        cmds.button(label="AI Apply Pose", command=self.ai_pose)

        cmds.separator(h=10)

        cmds.button(label="Blend Selected with AI", command=self.blend_pose)

        cmds.showWindow(win)

    def refresh_list(self):
        cmds.textScrollList(self.pose_list, edit=True, removeAll=True)
        for p in self.lib.list_poses():
            cmds.textScrollList(self.pose_list, edit=True, append=p)

    def save_pose(self, *args):
        name = cmds.promptDialog(
            title="Guardar Pose",
            message="Nombre:",
            button=["OK", "Cancel"]
        )
        if name == "OK":
            pose_name = cmds.promptDialog(query=True, text=True)
            self.lib.save_pose(pose_name)
            self.refresh_list()

    def load_pose(self, *args):
        sel = cmds.textScrollList(self.pose_list, query=True, selectItem=True)
        if sel:
            self.lib.load_pose(sel[0])

    def ai_pose(self, *args):
        result = cmds.promptDialog(
            title="AI Pose",
            message="Describe la pose:",
            button=["OK", "Cancel"]
        )

        if result == "OK":
            prompt = cmds.promptDialog(query=True, text=True)
            pose_name = self.ai.choose_pose(prompt)
            self.lib.load_pose(pose_name)

    def blend_pose(self, *args):

        sel = cmds.textScrollList(self.pose_list, query=True, selectItem=True)
        if not sel:
            return

        poseA = sel[0]

        prompt = cmds.promptDialog(
            title="Blend AI",
            message="Describe target pose:",
            button=["OK", "Cancel"]
        )

        if prompt == "OK":
            text = cmds.promptDialog(query=True, text=True)
            poseB = self.ai.choose_pose(text)

            self.blender.blend_poses(poseA, poseB, 0.5)