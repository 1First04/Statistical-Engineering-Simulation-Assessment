import unittest
from stat_engine import StatEngine


class TestStatEngine(unittest.TestCase):

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Test Mean & Median (Odd List)
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def test_mean_median_odd(self):
        data = [1, 2, 3, 4, 5]
        engine = StatEngine(data)

        self.assertEqual(engine.get_mean(), 3)
        self.assertEqual(engine.get_median(), 3)

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Test Mean & Median (Even List)
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def test_mean_median_even(self):
        data = [1, 2, 3, 4]
        engine = StatEngine(data)

        self.assertEqual(engine.get_mean(), 2.5)
        self.assertEqual(engine.get_median(), 2.5)

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Test Empty List Handling
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def test_empty_list(self):
        data = []
        with self.assertRaises(ValueError):
            StatEngine(data)

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Test Standard Deviation (Known Value)
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def test_standard_deviation(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        engine = StatEngine(data)

        # Known population std = 2
        std = engine.get_standard_deviation(is_sample=False)

        self.assertAlmostEqual(std, 2.0, places=5)

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Test Mode (Multimodal Case)
   # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def test_mode_multiple(self):
        data = [1, 2, 2, 3, 3]
        engine = StatEngine(data)

        modes = engine.get_mode()
        self.assertCountEqual(modes, [2, 3])

   # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Test No Mode Case
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def test_no_mode(self):
        data = [1, 2, 3, 4]
        engine = StatEngine(data)

        self.assertEqual(engine.get_mode(), "No mode")

   # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Test Outlier Detection
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def test_outliers(self):
        data = [10, 12, 14, 15, 1000]
        engine = StatEngine(data)

        outliers = engine.get_outliers(threshold=2)
        self.assertIn(1000, outliers)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Run Tests
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
if __name__ == "__main__":
    unittest.main()
