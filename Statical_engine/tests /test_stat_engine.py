def run_tests():
    data = [1, 2, 2, 3, 4]
    engine = StatEngine(data)

    assert engine.get_mean() == 2.4
    assert engine.get_median() == 2
    assert engine.get_mode() == [2]

    print("All basic tests passed!")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Example excution          @
#@@@@@@@@@@@@@@@@@@@@@@@@@@@

if __name__ == "__main__":
    dataset = [10, 12, 15, 18, 1000, "20", None, "bad"]

    engine = StatEngine(dataset)

    print("=== Statistical Analysis ===")
    print("Data:", engine.data)
    print("Mean:", engine.get_mean())
    print("Median:", engine.get_median())
    print("Mode:", engine.get_mode())
    print("Variance:", engine.get_variance())
    print("Std Dev:", engine.get_standard_deviation())
    print("Outliers:", engine.get_outliers())

    print("\n=== LLN Simulation ===")
    sim = SimulationEngine()
    means = sim.law_of_large_numbers(sim.generate_uniform_data, n_trials=1000)
    print("Final Running Mean (should stabilize):", means[-1])

    print("\n=== Running Tests ===")
    run_tests()
