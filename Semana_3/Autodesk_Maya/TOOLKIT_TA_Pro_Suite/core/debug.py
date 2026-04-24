import maya.cmds as cmds

class DebugTool:

    def run(self):

        issues = []

        # History
        for t in cmds.ls(type='transform'):
            history = cmds.listHistory(t)
            if history and len(history) > 1:
                issues.append(f"[HISTORY] {t}")

        # Constraints
        for c in cmds.ls(type='constraint'):
            if not cmds.listConnections(c):
                issues.append(f"[BROKEN CONSTRAINT] {c}")

        # Isolated nodes
        for node in cmds.ls():
            if not cmds.listConnections(node):
                issues.append(f"[ISOLATED NODE] {node}")

        if not issues:
            return "No issues found 🎉"

        return "\n".join(issues)