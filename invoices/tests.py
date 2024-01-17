from rest_framework.test import APITestCase
from .models import Invoice, InvoiceDetail
from django.urls import reverse


class InvoiceTests(APITestCase):
    def setUp(self):
        self.invoice = Invoice.objects.create(
            date="2023-12-31", customer_name="Test Customer"
        )
        self.detail = InvoiceDetail.objects.create(
            invoice=self.invoice,
            description="Test Description",
            quantity=2,
            unit_price=10,
        )
        self.base_name = "invoices-api-view"
        self.url_list = reverse(f"{self.base_name}-list")
        self.url_detail = reverse(f"{self.base_name}-detail", args=[self.invoice.id])

    def test_get_invoices(self):
        response = self.client.get(self.url_list)
        self.assertEqual(response.status_code, 200)
        # Test if the created invoice is present in the response data
        self.assertContains(response, "Test Customer")

    def test_get_specific_invoice(self):
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, 200)
        # Test if the retrieved invoice data matches the created invoice
        self.assertEqual(response.data["customer_name"], "Test Customer")

    def test_create_invoice(self):
        new_invoice_data = {"date": "2024-01-03", "customer_name": "New Test Customer"}
        response = self.client.post(self.url_list, new_invoice_data)
        self.assertEqual(response.status_code, 201)  # 201: Created
        # Test if the new invoice is created with correct data
        self.assertEqual(response.data["customer_name"], "New Test Customer")

    def test_update_invoice(self):
        updated_invoice_data = {
            "date": "2023-12-30",
            "customer_name": "Updated Customer",
        }
        response = self.client.put(self.url_detail, updated_invoice_data)
        self.assertEqual(response.status_code, 200)
        # Fetch the updated invoice from the database
        updated_invoice = Invoice.objects.get(pk=self.invoice.pk)
        # Test if the invoice data is updated correctly
        self.assertEqual(updated_invoice.customer_name, "Updated Customer")

    def test_delete_invoice(self):
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, 204)  # 204: No content
        # Test if the invoice is deleted from the database
        with self.assertRaises(Invoice.DoesNotExist):
            Invoice.objects.get(pk=self.invoice.pk)
