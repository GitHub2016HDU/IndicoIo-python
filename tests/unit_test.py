from indicoio.utils.image import image_preprocess
from PIL import Image
import os, unittest, base64, StringIO

DIR = os.path.dirname(os.path.realpath(__file__))

class ResizeTests(unittest.TestCase):
    """
    test image resizing
    """
    def test_min_axis_resize(self):
        test_image = os.path.normpath(os.path.join(DIR, "data/fear.png"))
        resized_image = image_preprocess(test_image, min_axis=360)
        image_string = StringIO.StringIO(base64.b64decode(resized_image))
        image = Image.open(image_string)
        self.assertEqual(image.size, (360.0, 360.0))
