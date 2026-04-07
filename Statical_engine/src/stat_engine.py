from typing import List, Union
import math
import random
Number = Union[int, float]

class StatEngine:
    def __init__(self, data: List[Union[Number, str, None]]):
        self.raw_data = data
        self.data = self._clean_data(data)

    # @@@@@@@@@@@@@@@@@@@@
    # Data Cleaning
    # @@@@@@@@@@@@@@@@@@@
    def _clean_data(self, data):
        cleaned = []
        for x in data:
            if isinstance(x, (int, float)):
                cleaned.append(float(x))
            elif isinstance(x, str):
                try:
                    cleaned.append(float(x))
                except:
                    continue
        if len(cleaned) == 0:
            raise ValueError("Dataset is empty after cleaning.")
        return cleaned

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Central Tendency
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def get_mean(self):
        return sum(self.data) / len(self.data)

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        return sorted_data[mid]

    def get_mode(self):
        freq = {}
        for x in self.data:
            freq[x] = freq.get(x, 0) + 1

        max_freq = max(freq.values())

        if max_freq == 1:
            return "No mode (all values are unique)"

        return [k for k, v in freq.items() if v == max_freq]

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Dispersion
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def get_variance(self, is_sample=True):
        n = len(self.data)
        mean = self.get_mean()

        if is_sample and n < 2:
            raise ValueError("Sample variance requires at least 2 data points.")

        var_sum = sum((x - mean) ** 2 for x in self.data)
        return var_sum / (n - 1 if is_sample else n)

    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # Outlier Detection
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()

        if std == 0:
            return []

        return [x for x in self.data if abs((x - mean) / std) > threshold]
