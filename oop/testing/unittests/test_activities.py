import unittest
from activities import eat, nap, is_funny, laugh

class ActivityTests(unittest.TestCase):
    def test_eat_healthy(self):
        """eat should have a positive message for healthy eating"""
        self.assertEqual(
            eat('broccoli', is_healthy=True),
            "I'm eating broccoli, because my body is a temple"
        )

    def test_eat_unhealthy(self):
        """eat should have a negative message for unhealthy eating"""
        self.assertEqual(
            eat("pizza", is_healthy=False),
            "I'm eating pizza, because YOLO!"
        )

    def test_eat_healthy_boolean(self):
        """is healthy must be a boolean"""
        with self.assertRaises(ValueError):
            eat('pizza',is_healthy='who cares')

    def test_short_nap(self):
        """short naps should be refreshing"""
        self.assertEqual(
            nap(1),
            "I'm feeling refreshed after my 1 hour nap"
        )

    def test_long_nap(self):
        """long naps should be discouraging"""
        self.assertEqual(
            nap(3),
            "Ugh I overslept. I didn't mean to nap for 3 hours!"
        )

    def test_is_funny_tim(self):
        self.assertEqual(is_funny('tim'), False)
        #this is falsey self.assertFalse(is_funny('tim'), 'Tim should not be funny')

    def test_is_funny_anyone_else(self):
        """Everyone but tim should be funny"""
        self.assertTrue(is_funny('blue'), "Blue should be funny")
        self.assertTrue(is_funny('Tammy'), "Tammy should be funny")
        self.assertTrue(is_funny('sven'), "sven should be funny")

    def test_laugh(self):
        self.assertIn(laugh(), ('lol', 'haha', 'tehehe'))

if __name__ == '__main__':
    unittest.main()
