import maya.cmds as cmds
import json
import os

POSE_FOLDER = os.path.join(os.path.dirname(__file__), "poses")

class PoseBlender:

    def load_pose_data(self, name):

        path = os.path.join(POSE_FOLDER, f"{name}.json")

        with open(path) as f:
            return json.load(f)

    def blend_poses(self, poseA, poseB, weight=0.5):

        dataA = self.load_pose_data(poseA)
        dataB = self.load_pose_data(poseB)

        controls = set(dataA["controls"]) & set(dataB["controls"])

        for ctrl in controls:

            rotA = dataA["controls"][ctrl]
            rotB = dataB["controls"][ctrl]

            blended = [
                rotA[i] * (1 - weight) + rotB[i] * weight
                for i in range(3)
            ]

            if cmds.objExists(ctrl):
                cmds.rotate(blended[0], blended[1], blended[2], ctrl, absolute=True)