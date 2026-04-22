import maya.cmds as cmds
import math
import random

# =========================
# UTILS
# =========================
def smoothstep(edge0, edge1, x):
    t = max(0.0, min((x - edge0) / (edge1 - edge0), 1.0))
    return t * t * (3 - 2 * t)

# =========================
# PERLIN (CON SEED)
# =========================
def build_permutation(seed):
    random.seed(seed)
    p = list(range(256))
    random.shuffle(p)
    return p + p

perm = build_permutation(42)

def fade(t):
    return t * t * t * (t * (t * 6 - 15) + 10)

def lerp(a, b, t):
    return a + t * (b - a)

def grad(hash, x, y):
    h = hash & 3
    u = x if h < 2 else y
    v = y if h < 2 else x
    return (u if h & 1 == 0 else -u) + (v if h & 2 == 0 else -v)

def pnoise2(x, y):
    xi = int(x) & 255
    yi = int(y) & 255

    xf = x - int(x)
    yf = y - int(y)

    u = fade(xf)
    v = fade(yf)

    aa = perm[perm[xi] + yi]
    ab = perm[perm[xi] + yi + 1]
    ba = perm[perm[xi + 1] + yi]
    bb = perm[perm[xi + 1] + yi + 1]

    x1 = lerp(grad(aa, xf, yf), grad(ba, xf - 1, yf), u)
    x2 = lerp(grad(ab, xf, yf - 1), grad(bb, xf - 1, yf - 1), u)

    return lerp(x1, x2, v)

# =========================
# MULTI-OCTAVE
# =========================
def layered_noise(x, z):
    total = 0.0
    frequency = 1.0
    amplitude = 1.0

    for i in range(5):
        total += pnoise2(x * frequency, z * frequency) * amplitude
        frequency *= 2.0
        amplitude *= 0.5

    return float(total)

# =========================
# MAIN TOOL
# =========================
class TerrainGeneratorPRO:

    def __init__(self):
        self.window = "TerrainGenPRO"

    def create_ui(self):

        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)

        self.window = cmds.window(self.window, title="Terrain Generator PRO", widthHeight=(320, 350))
        cmds.columnLayout(adjustableColumn=True)

        self.size = cmds.intFieldGrp(label="Size", value1=100)
        self.res = cmds.intFieldGrp(label="Resolution", value1=100)
        self.height = cmds.floatFieldGrp(label="Max Height", value1=40)

        self.scale = cmds.floatSliderGrp(
            label="Noise Scale",
            field=True,
            min=0.001,
            max=1.0,
            value=0.03,
            precision=3
        )

        self.seed = cmds.intFieldGrp(label="Seed", value1=42)

        self.biome = cmds.optionMenu(label="Biome")
        cmds.menuItem(label="Mountains")
        cmds.menuItem(label="Plains")
        cmds.menuItem(label="Island")

        cmds.separator(h=10)
        cmds.button(label="Generate Terrain PRO", command=self.generate)

        cmds.showWindow(self.window)

    def generate(self, *args):

        global perm

        size = cmds.intFieldGrp(self.size, q=True, value1=True)
        res = cmds.intFieldGrp(self.res, q=True, value1=True)
        max_height = cmds.floatFieldGrp(self.height, q=True, value1=True)
        scale = cmds.floatSliderGrp(self.scale, q=True, value=True)
        seed = cmds.intFieldGrp(self.seed, q=True, value1=True)
        biome = cmds.optionMenu(self.biome, q=True, value=True)

        perm = build_permutation(seed)

        plane = cmds.polyPlane(w=size, h=size, sx=res, sy=res, name="terrain_PRO")[0]
        verts = cmds.ls(f"{plane}.vtx[*]", flatten=True)

        half = size / 2.0

        for v in verts:

            pos = cmds.pointPosition(v)
            x, z = pos[0], pos[2]

            nx = x * scale
            nz = z * scale

            # BASE
            base = layered_noise(nx, nz)

            # DETAIL (suave)
            detail = layered_noise(nx * 1.5, nz * 1.5) * 0.15

            # RIDGE (protegido)
            ridge = 1 - abs(layered_noise(nx, nz))
            ridge = max(0.0, ridge)
            ridge = ridge ** 1.2
            ridge *= 0.2

            # MASK
            mask = layered_noise(nx * 0.3, nz * 0.3)
            mask = (mask + 1) / 2.0
            mask = smoothstep(0.4, 0.6, mask)

            # MEZCLA SUAVE
            terrain = base * 0.8 + detail * 0.2
            terrain += ridge * mask * 0.2

            # NORMALIZAR
            terrain = (terrain + 1) / 2.0

            # 🔥 PROTECCIÓN TOTAL
            if not isinstance(terrain, float):
                terrain = float(terrain.real)

            terrain = max(0.0, min(terrain, 1.0))

            # SUAVIZADO GLOBAL
            terrain = smoothstep(0.2, 0.8, terrain)

            # BIOMA
            dist = math.sqrt((x / half) ** 2 + (z / half) ** 2)

            if biome == "Mountains":
                terrain = terrain ** 1.1
            elif biome == "Plains":
                terrain *= 0.5
            elif biome == "Island":
                terrain *= max(0.0, 1 - dist)

            # HEIGHT SEGURO
            height = float(terrain.real if hasattr(terrain, "real") else terrain)

            # MOVER SOLO EN Y
            cmds.move(height * max_height, v, y=True, absolute=True)

        cmds.polySoftEdge(plane, angle=180)
        cmds.polySmooth(plane, divisions=1)

        print("✅ Terreno PRO estable generado")


# RUN
tool = TerrainGeneratorPRO()
tool.create_ui()