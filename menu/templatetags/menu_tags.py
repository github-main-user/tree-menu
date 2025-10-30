from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu/menu.html")
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related("parent")

    items_by_id = {item.id: item for item in menu_items}

    for item in menu_items:
        item.children_list = []

    root_items = []

    for item in menu_items:
        if item.parent_id:
            parent = items_by_id.get(item.parent_id)
            if parent:
                parent.children_list.append(item)
        else:
            root_items.append(item)

    return {
        "root_items": root_items,
    }
