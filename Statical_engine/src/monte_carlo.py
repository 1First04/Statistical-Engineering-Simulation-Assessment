class MonteCarloServerSimulation:
    """
    Simulates a startup server crash probability using Monte Carlo method
    True probability = 0.045 (4.5%)
    """

    def __init__(self, crash_prob=0.045, seed=42):
        self.crash_prob = crash_prob
        random.seed(seed)

    def simulate_crashes(self, days: int):
        """
        Simulate crashes over a number of days
        Returns: total_crashes, simulated_probability
        """
        crashes = 0

        for _ in range(days):
            if random.random() < self.crash_prob:
                crashes += 1

        simulated_prob = crashes / days
        return crashes, simulated_prob

    def run_experiments(self, day_sets):
        """
        Run multiple simulations for different day sizes
        """
        results = {}
   for days in day_sets:
            crashes, prob = self.simulate_crashes(days)
            results[days] = {
                "crashes": crashes,
                "simulated_probability": prob
            }

        return results

    def law_of_large_numbers_demo(self, max_days=10000):
        """
        Demonstrates LLN: running probability converges to true probability
        """
        crashes = 0
        running_probs = []

        for day in range(1, max_days + 1):
            if random.random() < self.crash_prob:
                crashes += 1

            running_probs.append(crashes / day)

        return running_probs
