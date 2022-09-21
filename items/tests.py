"""
Testing
"""
from django.test import TestCase
from django.urls import reverse
import pytest
from  items.models import Items

# def test_homepage_access():
#     url = reverse('items')
#     assert url == "/"

#*****************tests for CRUD******************

# #fixture for db access
@pytest.fixture
def new_groc(db):
    listitem = Items.objects.create(
        groc_item='Pytest',
        notes='pytest',
        item_price=10,
        item_pprice = 20,
        owner = 'admin'
    )
    return listitem

# #actual CRUD tests
# def test_search_grocery(new_groc):
#     assert Items.objects.filter(new_groc).exists()

def test_update_grocery(new_groc):
    new_groc.groc_item = 'Pytest'
    new_groc.save()
    assert Items.objects.filter(groc_item='Pytest').exists()

def test_delete_grocery(new_groc):
    new_groc.delete()
    assert (Items.objects.filter(groc_item='Pytest').exists()) == False