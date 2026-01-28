import bpy


class OBJECT_OT_set_emission_material(bpy.types.Operator):
    """Convert materials to emission using existing diffuse colors"""

    bl_idname = "object.set_emission_material"
    bl_label = "Set Emission Material"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        # Iterate over all objects in the scene
        for obj in bpy.data.objects:
            # Checks if the object is of type 'CURVE' or 'MESH'
            if obj.type in {"CURVE", "MESH"}:
                # Ensures the object has materials
                if getattr(obj.data, "materials", None):
                    for mat in obj.data.materials:
                        if not mat:
                            continue

                        # STEP 1: Save the original material color BEFORE activating 'use_nodes'
                        original_color = getattr(mat, "diffuse_color", None)
                        if original_color is None:
                            continue

                        # STEP 2: Enable the use of nodes AFTER saving the color
                        if not mat.use_nodes:
                            mat.use_nodes = True

                        # Remove all existing nodes to ensure complete cleanliness
                        nodes = mat.node_tree.nodes
                        for node in list(nodes):
                            nodes.remove(node)

                        # Create emission + output nodes
                        emission_node = nodes.new(type="ShaderNodeEmission")
                        material_output_node = nodes.new(type="ShaderNodeOutputMaterial")

                        # STEP 3: Set emission parameters
                        emission_node.inputs["Color"].default_value = original_color
                        emission_node.inputs["Strength"].default_value = 1.0  # Adjust as needed

                        # STEP 4: Link emission to output surface
                        mat.node_tree.links.new(
                            emission_node.outputs["Emission"],
                            material_output_node.inputs["Surface"],
                        )

        return {"FINISHED"}

