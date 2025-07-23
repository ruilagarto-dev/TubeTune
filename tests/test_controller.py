import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
import unittest.mock
from modules.controller import TubeTuneController

class TestTubeTuneController(unittest.TestCase):
    def setUp(self):
        self.view = unittest.mock.MagicMock()
        self.model = unittest.mock.MagicMock()
        self.controller = TubeTuneController(self.view, self.model)

    def test_is_valid_youtube_url(self):
        self.assertTrue(self.controller.is_valid_youtube_url("https://www.youtube.com/watch?v=irnvDeFZEPA"))
        self.assertTrue(self.controller.is_valid_youtube_url("https://www.tiktok.com/@sonare8d/video/7528199877080173829?is_from_webapp=1&sender_device=pc&web_id=7520347140489610785"))

if __name__ == "__main__":
    unittest.main()