from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from inventory.models import Item

class ItemTests(APITestCase):
    def setUp(self):
        """Set up a test user and item for testing."""
        # Create a test user
        self.user = User.objects.create_user(username='test', password='1234')

        # Log in the user and get the JWT token
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'test',
            'password': '1234'  # Match the password exactly
        })
        self.token = response.data['access']
        
        # Include the token in the headers for authenticated requests
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

        # Create a test item
        self.item = Item.objects.create(
            name='Test Item',
            description='This is a test item',
            quantity=10
        )
        
        self.valid_payload = {
            'name': 'New Test Item',
            'description': 'New item description',
            'quantity': 20
        }
        self.invalid_payload = {
            'name': '',  # Invalid name
            'description': 'This is an invalid item',
            'quantity': 5
        }

        self.read_url = reverse('read_item', kwargs={'item_id': self.item.id})
        self.update_url = reverse('update_item', kwargs={'item_id': self.item.id})
        self.delete_url = reverse('delete_item', kwargs={'item_id': self.item.id})
        self.create_url = reverse('create_item')

    def test_create_item_success(self):
        """Test creating an item successfully."""
        response = self.client.post(self.create_url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.valid_payload['name'])

    def test_create_item_failure(self):
        """Test creating an item with invalid payload (error case)."""
        response = self.client.post(self.create_url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_read_item_success(self):
        """Test reading an item successfully."""
        response = self.client.get(self.read_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.item.name)

    def test_read_item_not_found(self):
        """Test reading a non-existent item (error case)."""
        response = self.client.get(reverse('read_item', kwargs={'item_id': 999}))  # Non-existent ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_item_success(self):
        """Test updating an item successfully."""
        updated_data = {
            'name': 'Updated Item',
            'description': 'Updated description',
            'quantity': 15
        }
        response = self.client.put(self.update_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], updated_data['name'])

    def test_update_item_failure(self):
        """Test updating an item with invalid payload (error case)."""
        response = self.client.put(self.update_url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_item_success(self):
        """Test deleting an item successfully."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Item.objects.filter(id=self.item.id).exists())  # Ensure the item is deleted

    def test_delete_item_not_found(self):
        """Test deleting a non-existent item (error case)."""
        response = self.client.delete(reverse('delete_item', kwargs={'item_id': 999}))  # Non-existent ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
