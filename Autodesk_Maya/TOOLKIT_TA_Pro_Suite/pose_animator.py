import maya.cmds as cmds
from pose_library import PoseLibrary
from pose_ai import PoseAI

class PoseAnimator:

    def __init__(self):
        self.lib = PoseLibrary()
        self.ai = PoseAI()

    # =========================
    # 🧠 GENERAR SECUENCIA
    # =========================
    def generate_sequence(self, prompt):

    poses = self.lib.list_poses()

    # IA decide secuencia completa

    # =========================
    # 🎬 APLICAR ANIMACIÓN
    # =========================
    def apply_animation(self, poses, start_frame=1, spacing=10):

        current_frame = start_frame

        for pose_name in poses:

            cmds.currentTime(current_frame)

            # aplicar pose
            self.lib.load_pose(pose_name)

            # keyframear todo lo seleccionado
            controls = cmds.ls(selection=True)

            if not controls:
                controls = cmds.ls(type="transform")

            for ctrl in controls:
                cmds.setKeyframe(ctrl)

            print(f"[KEY] {pose_name} @ frame {current_frame}")

            current_frame += spacing

    # =========================
    # 🚀 MAIN FEATURE
    # =========================
    def animate_from_prompt(self, prompt):

        print(f"[AI] Prompt: {prompt}")

        poses = self.generate_sequence(prompt)

        print(f"[AI] Sequence: {poses}")

        self.apply_animation(poses)