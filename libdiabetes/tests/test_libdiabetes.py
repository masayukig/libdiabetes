
from libdiabetes.cli import main

import testtools

class TestLibdiabetes(testtools.TestCase):

    def test_main(self):
        assert main([]) == 0
