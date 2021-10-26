import bpy

for empty in bpy.context.selected_objects:
    Name = empty.name
    Coll = bpy.data.collections.new(Name)
    bpy.context.scene.collection.children.link(Coll)
    OldColl = empty.users_collection
    Coll.objects.link(empty)
    OldColl[0].objects.unlink(empty)
    for child in empty.children:
        Coll.objects.link(child)
        OldColl[0].objects.unlink(child)
    Coll.instance_offset = empty.location
         
    
