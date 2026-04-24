# ==========================================
# TA DASHBOARD PRO+ FINAL (AAA COMPLETE)
# ==========================================

import maya.cmds as cmds

TA_RESULTS = {}
ASSET_TYPE = "PROP"
HIGHLIGHTED = []

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

# ------------------------------
# ASSET TYPE
# ------------------------------
def set_asset_type():
    global ASSET_TYPE
    ASSET_TYPE = cmds.optionMenu("assetTypeMenu", q=True, value=True)

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

def fix_joint_naming(obj):
    base = strip_prefix(obj.split("|")[-1])
    expected = "jnt_" + base
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
    return [m for m in meshes if cmds.listHistory(m) and len(cmds.listHistory(m)) > 1]

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
# RIG VALIDATION
# ------------------------------
def check_rig_structure():
    issues = []
    if not cmds.objExists("jnt_root"):
        issues.append("Missing jnt_root")
    for j in cmds.ls(type="joint") or []:
        if not cmds.listRelatives(j, parent=True):
            issues.append(j)
    return issues

def check_groups():
    issues = []
    if not cmds.objExists("geo_grp"):
        issues.append("Missing geo_grp")
    if not cmds.objExists("rig_grp"):
        issues.append("Missing rig_grp")
    return issues

def check_parenting(meshes):
    issues = []
    for m in meshes:
        p = cmds.listRelatives(m, parent=True, fullPath=True)
        if p and "geo_grp" not in p[0]:
            issues.append(m)
    for j in cmds.ls(type="joint") or []:
        p = cmds.listRelatives(j, parent=True, fullPath=True)
        if p and "rig_grp" not in p[0]:
            issues.append(j)
    return issues

def check_skin(meshes):
    issues = []
    for m in meshes:
        hist = cmds.listHistory(m) or []
        if not cmds.ls(hist, type="skinCluster"):
            issues.append(m)
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
    "Joints": 18,
    "Rig_Structure": 4,
    "Groups": 4,
    "Parenting": 4,
    "Skin": 4
}

def get_shapes(obj):
    return cmds.listRelatives(obj, shapes=True, fullPath=True) or []

def apply_color(node, color):
    try:
        cmds.setAttr(node + ".overrideEnabled", 1)
        cmds.setAttr(node + ".overrideColor", color)
    except:
        pass

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
        if not cmds.objExists(obj):
            continue

        shapes = get_shapes(obj)
        if shapes:
            for s in shapes:
                apply_color(s, color)
                HIGHLIGHTED.append(s)
        else:
            apply_color(obj, color)
            HIGHLIGHTED.append(obj)

def highlight_all_issues():
    clear_highlight()
    for cat in TA_RESULTS:
        highlight_category(cat)

# ------------------------------
# INTERACTION
# ------------------------------
def select_and_frame(obj):
    if not cmds.objExists(obj):
        return

    cmds.select(obj, r=True)

    # frame camera
    try:
        cmds.viewFit()
    except:
        pass

    # isolate
    panel = cmds.getPanel(withFocus=True)
    if "modelPanel" in panel:
        try:
            cmds.isolateSelect(panel, state=1)
            cmds.isolateSelect(panel, addSelected=True)
        except:
            pass

# ------------------------------
# VALIDATE
# ------------------------------
def run_validation():
    global TA_RESULTS

    meshes = get_mesh_transforms()

    results = {
        "History": check_history(meshes),
        "Freeze": check_freeze(meshes),
        "NonManifold": check_non_manifold(meshes),
        "Lamina": check_lamina(meshes),
        "Naming": check_naming(meshes)
    }

    if ASSET_TYPE == "CHARACTER":
        results["Joints"] = [j for j in cmds.ls(type="joint") or []
                             if not j.split("|")[-1].startswith("jnt_")]
        results["Rig_Structure"] = check_rig_structure()
        results["Groups"] = check_groups()
        results["Parenting"] = check_parenting(meshes)
        results["Skin"] = check_skin(meshes)

    TA_RESULTS = results
    update_ui()

# ------------------------------
# FIXES
# ------------------------------
def fix_object(obj, category):
    if category == "History":
        cmds.delete(obj, constructionHistory=True)
    elif category == "Freeze":
        cmds.makeIdentity(obj, apply=True, t=True, r=True, s=True)
    elif category in ["NonManifold", "Lamina"]:
        cmds.polyCleanup(obj)
    elif category == "Naming":
        fix_naming(obj)
    elif category == "Joints":
        if obj != "Missing jnt_root":
            fix_joint_naming(obj)

def fix_selected():
    for cat in TA_RESULTS:
        sel = cmds.textScrollList(cat+"_list", q=True, si=True)
        if sel:
            for obj in sel:
                fix_object(obj.split("  →")[0], cat)
    run_validation()

def fix_all():
    for obj in get_mesh_transforms():
        cmds.delete(obj, ch=True)
        cmds.makeIdentity(obj, apply=True, t=True, r=True, s=True)
        cmds.xform(obj, centerPivots=True)
        fix_naming(obj)
    run_validation()

# ------------------------------
# UI UPDATE
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
                if key == "Naming" and "Missing" not in obj:
                    display = f"{obj.split('|')[-1]}  →  {get_expected_name(obj)}"

                cmds.textScrollList(key+"_list", e=True, append=display)

# ------------------------------
# UI
# ------------------------------
def create_ui():

    if cmds.window("taProWin", exists=True):
        cmds.deleteUI("taProWin")

    cmds.window("taProWin", title="TA Dashboard PRO+", widthHeight=(520,600))

    cmds.paneLayout(configuration="vertical2")

    # TOP
    top = cmds.columnLayout(adjustableColumn=True)

    cmds.text(label="AAA ASSET VALIDATOR", align="center")

    cmds.optionMenu("assetTypeMenu", label="Asset Type",
                    changeCommand=lambda *_: set_asset_type())
    cmds.menuItem(label="PROP")
    cmds.menuItem(label="CHARACTER")

    cmds.separator(h=10)

    cmds.scrollLayout(height=350)
    cmds.gridLayout(numberOfColumns=2, cellWidthHeight=(240,120))

    def create_section(name):
        cmds.frameLayout(label=name)
        cmds.columnLayout(adjustableColumn=True)

        cmds.text(name+"_status", label="...")

        cmds.textScrollList(
            name+"_list",
            height=60,
            selectCommand=lambda *_: highlight_category(name),
            doubleClickCommand=lambda *_: select_and_frame(
                cmds.textScrollList(name+"_list", q=True, si=True)[0]
            )
        )

        cmds.setParent("..")
        cmds.setParent("..")

    sections = ["History","Freeze","NonManifold","Lamina","Naming",
                "Joints","Rig_Structure","Groups","Parenting","Skin"]

    for s in sections:
        create_section(s)

    cmds.setParent(top)

    # BOTTOM
    bottom = cmds.columnLayout(adjustableColumn=True)

    cmds.separator(h=10)

    cmds.button(label="VALIDATE", h=40, command=lambda *_: run_validation())

    cmds.button(label="HIGHLIGHT ALL ISSUES",
                command=lambda *_: highlight_all_issues())

    cmds.button(label="CLEAR HIGHLIGHT",
                command=lambda *_: clear_highlight())

    cmds.rowLayout(nc=2)
    cmds.button(label="FIX SELECTED", command=lambda *_: fix_selected())
    cmds.button(label="FIX ALL", command=lambda *_: fix_all())
    cmds.setParent("..")

    cmds.rowLayout(nc=2)
    cmds.button(label="REVERT SELECTED", command=lambda *_: revert_selected())
    cmds.button(label="REVERT ALL", command=lambda *_: revert_all())
    cmds.setParent("..")

    cmds.showWindow("taProWin")

# ------------------------------
# RUN
# ------------------------------
create_ui()