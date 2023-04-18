bl_info = {
    "name": "Texture Image Node Combiner (v1.0)",
    "description": "Combine texture images into a single image using nodes",
    "author": "Mr. Robot",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "category": "Node",
}

import os
import bpy
import random
from PIL import Image
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import StringProperty, PointerProperty, EnumProperty


def get_embedded_images(self, context):
    images = []
    for img in bpy.data.images:
        if img.name is not None:
            images.append((img.name, img.name, ""))
    
    # Add None values for the images that are not selected
    if len(images) < 4:
        images += [(None, "None", ""), (None, "None", ""), (None, "None", "")]
    elif len(images) == 4:
        images += [(None, "None", "")]
    
    return images


class TexturePaths(PropertyGroup):
    roughness_image: EnumProperty(
        name="Roughness",
        description="Select the roughness texture",
        items=get_embedded_images,
    )
    occlusion_image: EnumProperty(
        name="Occlusion",
        description="Select the occlusion texture",
        items=get_embedded_images,
    )
    metallic_image: EnumProperty(
        name="Metallic",
        description="Select the metallic texture",
        items=get_embedded_images,
    )
    alpha_image: EnumProperty(
        name="Alpha",
        description="Select the alpha texture",
        items=get_embedded_images,
    )

class NODE_OT_combine_textures(Operator):
    bl_idname = "node.combine_textures"
    bl_label = "Combine Textures"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        texture_images = {
            'roughness': context.scene.texture_paths.roughness_image,
            'occlusion': context.scene.texture_paths.occlusion_image,
            'metallic': context.scene.texture_paths.metallic_image,
            'alpha': context.scene.texture_paths.alpha_image,
        }

        images = {}
        for role, image_name in texture_images.items():
            if image_name == "":
                continue

            img = bpy.data.images[image_name]
            img_path = img.filepath

            if img.packed_file:
                import io
                img_data = io.BytesIO(img.packed_file.data)
                img = Image.open(img_data).convert('RGBA')
                images[role] = img
            elif os.path.isfile(bpy.path.abspath(img_path)):
                img = Image.open(bpy.path.abspath(img_path)).convert('RGBA')
                images[role] = img

        if len(images) == 0:
            self.report({'ERROR'}, "No images selected")
            return {'CANCELLED'}

        width, height = images['occlusion'].size if 'occlusion' in images else images['roughness'].size
        combined_img = Image.new('RGBA', (width, height))

        for x in range(width):
            for y in range(height):
                r, g, b, a = 0, 0, 0, 255

                if 'roughness' in images:
                    r = images['roughness'].getpixel((x, y))[0]

                if 'occlusion' in images:
                    g = images['occlusion'].getpixel((x, y))[1]

                if 'metallic' in images:
                    b = images['metallic'].getpixel((x, y))[2]

                if 'alpha' in images:
                    a = images['alpha'].getpixel((x, y))[3]

                combined_img.putpixel((x, y), (r, g, b, a))

        combined_img_path = bpy.path.abspath("//combined_texture.png")
        combined_img.save(combined_img_path)

        combined_node = context.space_data.edit_tree.nodes.new(type='ShaderNodeTexImage')
        combined_node.image = bpy.data.images.load(combined_img_path)
        combined_node.location = (0, 0)
        combined_node.select = True
        separate_node = context.space_data.edit_tree.nodes.new(type='ShaderNodeSeparateRGB')
        separate_node.location = (combined_node.location.x + 200, combined_node.location.y)
        separate_node.select = True
        
        context.space_data.edit_tree.links.new(combined_node.outputs['Color'], separate_node.inputs['Image'])

        return {'FINISHED'}

class NODE_PT_combine_textures(Panel):
    bl_label = "Combine Textures"
    bl_idname = "NODE_PT_combine_textures"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'RGBA Combiner'

    def draw(self, context):
        layout = self.layout
        texture_paths = context.scene.texture_paths

        # Create a Box layout to group the texture selector boxes
        box = layout.box()
        box.label(text="Texture Images:")
        box.prop(texture_paths, "roughness_image")
        box.prop(texture_paths, "occlusion_image")
        box.prop(texture_paths, "metallic_image")
        box.prop(texture_paths, "alpha_image")

        # Add the message as a label inside the Box
        box.label(text="If you do not have one of these >>")
        box.label(text="Choose a duplicate.")
        layout.operator("node.combine_textures")

def register():
    bpy.utils.register_class(TexturePaths)
    bpy.utils.register_class(NODE_OT_combine_textures)
    bpy.utils.register_class(NODE_PT_combine_textures)
    bpy.types.Scene.texture_paths = PointerProperty(type=TexturePaths)

def unregister():
    bpy.utils.unregister_class(TexturePaths)
    bpy.utils.unregister_class(NODE_OT_combine_textures)
    bpy.utils.unregister_class(NODE_PT_combine_textures)
    del bpy.types.Scene.texture_paths


if __name__ == "__main__":
    register()
