from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    request = context["request"]
    current_path = request.path

    menu_items = MenuItem.objects.filter(menu__name=menu_name)

    items_by_id = {item.id: item for item in menu_items}

    active_item = None
    for item in menu_items:
        item.children_list = []
        item.is_active = False
        if item.get_absolute_url() == current_path:
            item.is_active = True
            active_item = item

    if active_item:  # make all parents of an active item active
        parent = items_by_id.get(active_item.parent_id)
        while parent:
            parent.is_active = True
            parent = items_by_id.get(parent.parent_id)

    root_items = []

    for item in menu_items:
        if item.parent_id:
            parent = items_by_id.get(item.parent_id)
            if parent:
                parent.children_list.append(item)
        else:
            root_items.append(item)

    return {"root_items": root_items}

