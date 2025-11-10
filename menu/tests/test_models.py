import pytest
from django.core.exceptions import ValidationError

from menu.models import Menu, MenuItem


@pytest.fixture
def menu(db) -> Menu:
    return Menu.objects.create(name="main_menu")


@pytest.fixture
def menu_item(db, menu) -> MenuItem:
    return MenuItem.objects.create(
        menu=menu,
        title="Test Item",
        url="https://example.com",
        named_url=False,
    )


@pytest.mark.django_db
def test_get_not_named_absolute_url(menu_item: MenuItem) -> None:
    assert menu_item.get_absolute_url() == "https://example.com"


@pytest.mark.django_db
def test_get_named_absolute_url(menu_item: MenuItem) -> None:
    menu_item.url = "dashbord:about"
    menu_item.named_url = True
    menu_item.save()

    assert menu_item.get_absolute_url() == "#"


def test_element_parent_of_himself_fail(menu_item: MenuItem) -> None:
    menu_item.parent = menu_item
    with pytest.raises(ValidationError):
        menu_item.full_clean()


def test_element_parent_circular_fail(menu: Menu, menu_item: MenuItem) -> None:
    menu_item2 = MenuItem.objects.create(
        menu=menu,
        parent=menu_item,
        title="Test Item",
        url="https://example.com",
        named_url=False,
    )
    menu_item.parent = menu_item2
    with pytest.raises(ValidationError):
        menu_item.full_clean()


def test_element_parent_menu_is_not_item_menu_fail(menu_item: MenuItem) -> None:
    menu_item2 = MenuItem.objects.create(
        menu=Menu.objects.create(name="new_menu"),
        title="Test Item",
        url="https://example.com",
        named_url=False,
    )
    menu_item.parent = menu_item2
    with pytest.raises(ValidationError):
        menu_item.full_clean()
