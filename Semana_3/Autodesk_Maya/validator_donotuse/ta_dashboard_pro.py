# ==========================================
# TA DASHBOARD PRO - CLEAN VERSION (FIXED)
# ==========================================

import maya.cmds as cmds

TA_RESULTS = {}
HIGHLIGHTED = []
ASSET_TYPE = "PROP"

# ------------------------------
# UTILS
# ------------------------------
def remove_duplicates(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

def get_mesh_transforms():
    meshes = cmds.ls(type="mesh", noIntermediate=True)
    transforms = []
    for m in meshes:
        p = cmds.listRelatives(m, parent=True, fullPath=True)
        if p:
            transforms.append(p[0])
    return remove_duplicates(transforms)

def get_clean_name(name):
    return name.split("  →")[0]

# ------------------------------
# NAMING
# ------------------------------
PREFIXES = ["geo_", "grp_", "jnt_"]

def strip_prefix(name):
    for p in PREFIXES:
        if name.startswith(p):
            return name[len(p):]
    return name

def get_expected_name(obj):
    short = obj.split("|")[-1]
    base = strip_prefix(short)

    shapes = cmds.listRelatives(obj, shapes=True) or []
    if shapes and cmds.nodeType(shapes[0]) == "mesh":
        return "geo_" + base

    if cmds.nodeType(obj) == "joint":
        return "jnt_" + base

    return "grp_" + base

def check_naming(meshes):
    return [m for m in meshes if m.split("|")[-1] != get_expected_name(m)]

def store_original_name(obj):
    if not cmds.attributeQuery("origName", node=obj, exists=True):
        cmds.addAttr(obj, ln="origName", dt="string")
        cmds.setAttr(obj + ".origName", obj.split("|")[-1], type="string")

def fix_naming(obj):
    expected = get_expected_name(obj)
    if obj.split("|")[-1] != expected:
        store_original_name(obj)
        try:
            cmds.rename(obj, expected)
        except:
            pass

def revert_name(obj):
    if cmds.attributeQuery("origName", node=obj, exists=True):
        try:
            cmds.rename(obj, cmds.getAttr(obj + ".origName"))
        except:
            pass

# ------------------------------
# VALIDATIONS
# ------------------------------
def check_history(meshes):
    bad = []
    for m in meshes:
        hist = cmds.listHistory(m) or []
        hist = cmds.ls(hist, type=["polyExtrudeFace","polyBevel","polySplit"]) or []
        if hist:
            bad.append(m)
    return bad

def check_freeze(meshes):
    bad = []
    for obj in meshes:
        t = cmds.xform(obj, q=True, ws=True, t=True)
        r = cmds.xform(obj, q=True, ws=True, ro=True)
        s = cmds.xform(obj, q=True, r=True, s=True)

        if any(abs(v) > 0.001 for v in t+r) or any(abs(v-1) > 0.001 for v in s):
            bad.append(obj)
    return bad

def check_non_manifold(meshes):
    return [m for m in meshes if cmds.polyInfo(m, nonManifoldVertices=True)]

def check_lamina(meshes):
    return [m for m in meshes if cmds.polyInfo(m, laminaFaces=True)]

# ------------------------------
# SAFE CLEANUP
# ------------------------------
def cleanup_mesh(obj):
    try:
        cmds.polyCleanup(obj,
            constructionHistory=False,
            nonManifoldGeometry=True,
            laminaFaces=True,
            zeroAreaFaces=True,
            zeroLengthEdges=True,
            zeroAreaUV=True
        )
    except:
        pass

# ------------------------------
# RIG VALIDATION
# ------------------------------
def is_under_group(obj, group_name):
    parents = cmds.listRelatives(obj, parent=True, fullPath=True) or []
    while parents:
        p = parents[0]
        if group_name in p:
            return True
        parents = cmds.listRelatives(p, parent=True, fullPath=True) or []
    return False

def check_parenting(meshes):
    issues = []
    for m in meshes:
        if not is_under_group(m, "geo_grp"):
            issues.append(m)

    for j in cmds.ls(type="joint") or []:
        if not is_under_group(j, "rig_grp"):
            issues.append(j)

    return issues

# ------------------------------
# HIGHLIGHT
# ------------------------------
COLOR_MAP = {
    "History": 17,
    "Freeze": 21,
    "NonManifold": 13,
    "Lamina": 9,
    "Naming": 6,
    "Parenting": 4
}

def apply_color(node, color):
    if not cmds.objExists(node):
        return False

    if not cmds.attributeQuery("overrideEnabled", node=node, exists=True):
        return False

    try:
        cmds.setAttr(node + ".overrideEnabled", 1)
        cmds.setAttr(node + ".overrideColor", color)
        return True
    except:
        return False

def clear_highlight():
    global HIGHLIGHTED
    for n in HIGHLIGHTED:
        if cmds.objExists(n):
            try:
                cmds.setAttr(n + ".overrideEnabled", 0)
            except:
                pass
    HIGHLIGHTED = []

def highlight_category(category):
    global HIGHLIGHTED
    color = COLOR_MAP.get(category, 13)

    for obj in TA_RESULTS.get(category, []):
        shapes = cmds.listRelatives(obj, shapes=True, fullPath=True) or []

        if shapes:
            for s in shapes:
                if apply_color(s, color):
                    HIGHLIGHTED.append(s)
        else:
            if apply_color(obj, color):
                HIGHLIGHTED.append(obj)

# ------------------------------
# INTERACTION
# ------------------------------
def select_and_frame(obj):
    if not cmds.objExists(obj):
        return
    cmds.select(obj, r=True)
    try:
        cmds.viewFit()
    except:
        pass

# ------------------------------
# VALIDATE
# ------------------------------
def run_validation():
    global TA_RESULTS

    meshes = get_mesh_transforms()

    TA_RESULTS = {
        "History": check_history(meshes),
        "Freeze": check_freeze(meshes),
        "NonManifold": check_non_manifold(meshes),
        "Lamina": check_lamina(meshes),
        "Naming": check_naming(meshes),
        "Parenting": check_parenting(meshes)
    }

    update_ui()

# ------------------------------
# FIXES
# ------------------------------
def fix_object(obj, category):
    if category == "History":
        cmds.delete(obj, ch=True)
    elif category == "Freeze":
        cmds.makeIdentity(obj, apply=True, t=True, r=True, s=True)
    elif category in ["NonManifold", "Lamina"]:
        cleanup_mesh(obj)
    elif category == "Naming":
        fix_naming(obj)

def fix_selected():
    for cat in TA_RESULTS:
        sel = cmds.textScrollList(cat+"_list", q=True, si=True)
        if sel:
            for obj in sel:
                fix_object(get_clean_name(obj), cat)
    run_validation()

def fix_all():
    for obj in get_mesh_transforms():
        try:
            if not cmds.listConnections(obj, type="skinCluster"):
                cmds.delete(obj, ch=True)
        except:
            pass

        try:
            cmds.makeIdentity(obj, apply=True, t=True, r=True, s=True)
        except:
            pass

        fix_naming(obj)

    run_validation()

# ------------------------------
# REVERT
# ------------------------------
def revert_selected():
    for cat in TA_RESULTS:
        sel = cmds.textScrollList(cat+"_list", q=True, si=True)
        if sel:
            for obj in sel:
                revert_name(get_clean_name(obj))

def revert_all():
    for obj in get_mesh_transforms():
        revert_name(obj)

# ------------------------------
# UI
# ------------------------------
def update_ui():
    for key in TA_RESULTS:
        cmds.textScrollList(key+"_list", e=True, removeAll=True)

        items = TA_RESULTS[key]

        if not items:
            cmds.text(key+"_status", e=True, label="OK", bgc=(0.2,0.6,0.2))
        else:
            cmds.text(key+"_status", e=True,
                      label=f"{len(items)} issues",
                      bgc=(0.6,0.2,0.2))

            for obj in items:
                display = obj
                if key == "Naming":
                    display = f"{obj.split('|')[-1]}  →  {get_expected_name(obj)}"

                cmds.textScrollList(key+"_list", e=True, append=display)

def create_ui():
    if cmds.window("taProWin", exists=True):
        cmds.deleteUI("taProWin")

    cmds.window("taProWin", title="TA Dashboard PRO", widthHeight=(500,550))
    cmds.columnLayout(adjustableColumn=True)

    cmds.text(label="TA VALIDATOR", align="center")

    sections = ["History","Freeze","NonManifold","Lamina","Naming","Parenting"]

    for s in sections:
        cmds.frameLayout(label=s)
        cmds.columnLayout()

        cmds.text(s+"_status", label="...")

        cmds.textScrollList(
            s+"_list",
            height=80,
            selectCommand=lambda _, cat=s: highlight_category(cat),
            doubleClickCommand=lambda _, cat=s: select_and_frame(
                get_clean_name(cmds.textScrollList(cat+"_list", q=True, si=True)[0])
            )
        )

        cmds.setParent("..")
        cmds.setParent("..")

    cmds.button(label="VALIDATE", h=40, command=lambda *_: run_validation())
    cmds.button(label="CLEAR HIGHLIGHT", command=lambda *_: clear_highlight())
    cmds.button(label="FIX SELECTED", command=lambda *_: fix_selected())
    cmds.button(label="FIX ALL", command=lambda *_: fix_all())
    cmds.button(label="REVERT SELECTED", command=lambda *_: revert_selected())
    cmds.button(label="REVERT ALL", command=lambda *_: revert_all())

    cmds.showWindow("taProWin")

# ------------------------------
# RUN
# ------------------------------
create_ui()