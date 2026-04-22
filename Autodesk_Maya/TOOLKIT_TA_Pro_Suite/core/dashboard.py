import maya.cmds as cmds

class Dashboard:

    def scan_scene(self):

        data = {
            "meshes": len(cmds.ls(type='mesh')),
            "joints": len(cmds.ls(type='joint')),
            "cameras": len(cmds.ls(type='camera')),
            "total_nodes": len(cmds.ls())
        }

        report = "\n--- SCENE REPORT ---\n\n"
        for k, v in data.items():
            report += f"{k}: {v}\n"

        return report