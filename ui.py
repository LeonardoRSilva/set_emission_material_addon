import bpy


class VIEW3D_PT_set_emission_material(bpy.types.Panel):
    """Panel with a button to set emission materials"""

    bl_label = "Set Emission Material"
    bl_idname = "VIEW3D_PT_set_emission_material"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Emission"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.set_emission_material", icon="LIGHT_HEMI")

