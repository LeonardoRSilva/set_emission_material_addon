bl_info = {
    "name": "Set Emission Material",
    "author": "Leonardo Silva(leonardo.rsil@gmail.com)",
    "wiki_url": "https://github.com/LeonardoRSilva/set_emission_material_addon#readme",
	"tracker_url": "https://github.com/LeonardoRSilva/set_emission_material_addon/issues",
	"doc_url": "https://github.com/LeonardoRSilva/set_emission_material_addon#readme",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Emission",
    "description": "Convert the materials of the objects in the scene of Difuse BSDF to Emission type while preserving the original color.",
    "category": "Material",
}

from .operators import OBJECT_OT_set_emission_material
from .ui import VIEW3D_PT_set_emission_material

classes = (
    OBJECT_OT_set_emission_material,
    VIEW3D_PT_set_emission_material,
)


def register():
    import bpy

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    import bpy

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

