from django.test import TestCase
from .models import Image , Profile ,Comment
# Create your tests here.
class  ImageTestClass(TestCase):
    #setup method
    def setUp(self):
        self.image = Image(image_name = 'Image')
    #test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image , Image))
    #save method
    def  test_save_method(self):
        self.image.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) >0)

    #delete image
    def test_delete_method(self):
        self.image.save_image()
        image = Image.objects.all()
        self.image.objects.filter(id = self.image.id).delete()