import bpy
from .addon.tag_copy import *
from .addon.rename import *
from .addon.tag_add import *
from .addon.tag_remove import *
from .addon.move import *
from .addon.author import *
from .addon.description import *
from .addon.clear import *
from .addon.copyright import *
from .addon.license import *
from .addon.utilities import header_menu_func
from .addon.settings import *

bl_info = {
    "name": "Bulk Asset Tools",
    "author": "Johnny Matthews",
    "location": "Asset Viewer - Edit Menu",
    "version": (1, 4),
    "blender": (3, 5, 0),
    "description": "A set of tools for managing multiple assets at the same time",
    "doc_url": "",
    "category": "Assets",
}

classes = (
    BulkAssetToolsPreferences,
    ASSET_OT_MoveOperator,
    ASSET_OT_AuthorOperator,
    ASSET_OT_DescriptionOperator,
    ASSET_OT_TagAddOperator,
    ASSET_OT_TagCopyOperator,
    ASSET_OT_TagRemoveOperator,
    ASSET_OT_RenameOperator,
    ASSET_OT_ClearOperator,
    ASSET_OT_LicenseOperator,
    ASSET_OT_CopyrightOperator,
)

menus = (
    ASSET_MT_move_menu_func,
    ASSET_MT_author_menu_func,
    ASSET_MT_license_menu_func,
    ASSET_MT_copyright_menu_func,
    ASSET_MT_description_menu_func,
    ASSET_MT_tag_add_menu_func,
    ASSET_MT_tag_copy_menu_func,
    ASSET_MT_tag_remove_menu_func,
    ASSET_MT_rename_menu_func,
    ASSET_MT_clear_menu_func,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    if hasattr(bpy.types, "ASSETBROWSER_MT_asset"):
        bpy.types.ASSETBROWSER_MT_context_menu.append(header_menu_func)
        bpy.types.ASSETBROWSER_MT_asset.append(header_menu_func)
        for menu in menus:
            bpy.types.ASSETBROWSER_MT_asset.append(menu)
            bpy.types.ASSETBROWSER_MT_context_menu.append(menu)
    elif hasattr(bpy.types, "ASSETBROWSER_MT_edit"):
        bpy.types.ASSETBROWSER_MT_edit.append(header_menu_func)
        bpy.types.ASSETBROWSER_MT_context_menu.append(header_menu_func)
        for menu in menus:
            bpy.types.ASSETBROWSER_MT_edit.append(menu)
            bpy.types.ASSETBROWSER_MT_context_menu.append(menu)


def unregister():
    if hasattr(bpy.types, "ASSETBROWSER_MT_asset"):
        bpy.types.ASSETBROWSER_MT_context_menu.remove(header_menu_func)
        bpy.types.ASSETBROWSER_MT_asset.remove(header_menu_func)
        for menu in menus:
            bpy.types.ASSETBROWSER_MT_asset.remove(menu)
            bpy.types.ASSETBROWSER_MT_context_menu.remove(menu)
    elif hasattr(bpy.types, "ASSETBROWSER_MT_edit"):
        bpy.types.ASSETBROWSER_MT_edit.remove(header_menu_func)
        bpy.types.ASSETBROWSER_MT_context_menu.remove(header_menu_func)
        for menu in menus:
            bpy.types.ASSETBROWSER_MT_edit.remove(menu)
            bpy.types.ASSETBROWSER_MT_context_menu.remove(menu)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
