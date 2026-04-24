import maya.cmds as cmds
import json
import os

POSE_FOLDER = os.path.join(os.path.dirname(__file__), "poses")

class PoseLibrary:

    def save_pose(self, name):

        controls = cmds.ls(selection=True)

        if not controls:
            cmds.warning("Seleccioná controles")
            return

        data = {
            "name": name,
            "tags": [],
            "controls": {}
        }

        for ctrl in controls:
            rot = cmds.xform(ctrl, query=True, rotation=True, worldSpace=True)
            data["controls"][ctrl] = rot

        path = os.path.join(POSE_FOLDER, f"{name}.json")

        with open(path, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Pose guardada: {name}")

    def load_pose(self, name):

        path = os.path.join(POSE_FOLDER, f"{name}.json")

        if not os.path.exists(path):
            cmds.warning("Pose no encontrada")
            return

        with open(path) as f:
            data = json.load(f)

        for ctrl, rot in data["controls"].items():
            if cmds.objExists(ctrl):
                cmds.rotate(rot[0], rot[1], rot[2], ctrl, absolute=True)

    def list_poses(self):

        return [f.replace(".json", "") for f in os.listdir(POSE_FOLDER)]