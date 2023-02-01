import bpy
import os
from .utilities import *


class AssetMoveOperator(bpy.types.Operator):
    """Move Assets to a Catalog"""
    bl_idname = "asset.bulk_asset_mover"
    bl_label = "Bulk Asset Mover"
    bl_options = {'REGISTER', 'UNDO'}

    catalog: bpy.props.EnumProperty(
        name="Destination Catalog", items=item_callback)
    commands = {}
    command_count = 0
    _timer = None

    @classmethod
    def poll(cls, context):
        return context.space_data.type == 'FILE_BROWSER' and context.space_data.browse_mode == 'ASSETS'

    def modal(self, context, event: bpy.types.Event):
        return handleModal(self, context, event)

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        self.move_main(context)
        return finalizeExecute(self, context)

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)
        return {'FINISHED'}

    def move_main(self, context):
        directory = get_catalog_directory(context)
        commands = {}
        for f in bpy.context.selected_asset_files:
            if f.local_id == None:
                path = get_file_path(f.relative_path, directory)
                type_out = id_type_to_type_name(f.id_type)
                if path not in self.commands.keys():
                    self.commands[path] = []
                self.commands[path].append(
                    "bpy.data."+type_out+"['"+f.name+"'].asset_data.catalog_id =\'"+self.catalog+"\';")
            else:
                f.local_id.asset_data.catalog_id = self.catalog


def move_menu_func(self, context):
    self.layout.operator(AssetMoveOperator.bl_idname,
                         text=AssetMoveOperator.bl_label)