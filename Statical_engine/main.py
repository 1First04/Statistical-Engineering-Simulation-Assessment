
"""
Main Entry Point
Statistical Engineering & Simulation Project

Runs:
- Part 1: Statistical Analysis
- Part 2: Monte Carlo Simulation (Server Failure)
"""

from stat_engine import StatEngine
from simulation import MonteCarloServerSimulation
import json


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Part 1: Statistical Analysis
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def run_statistical_analysis():
    print("=== Part 1: Statistical Engine ===")

    try:
        # Load dataset (JSON)
        with open("data/sample_salaries.json", "r") as f:
            data = json.load(f)

        engine = StatEngine(data)

        print(f"Dataset Size: {len(engine.data)}")
        print("Mean:", engine.get_mean())
        print("Median:", engine.get_median())
        print("Mode:", engine.get_mode())
        print("Sample Variance:", engine.get_variance(is_sample=True))
        print("Population Variance:", engine.get_variance(is_sample=False))
        print("Standard Deviation:", engine.get_standard_deviation())
        print("Outliers:", engine.get_outliers())

    except FileNotFoundError:
        print("❌ Error: Dataset file not found.")
    except ValueError as e:
        print(f"❌ Error: {e}")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Part 2: Monte Carlo Simulation
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def run_simulation():
    print("\n=== Part 2: Monte Carlo Simulation ===")

    sim = MonteCarloServerSimulation(crash_prob=0.045)

    # Different dataset sizes
    day_sets = [10, 100, 1000, 10000]

    print("\n--- Simulation Results ---")
    for days in day_sets:
        crashes, prob = sim.simulate_crashes(days)
        print(f"Days: {days} | Crashes: {crashes} | Simulated Prob: {prob:.4f}")

    # LLN Demonstration
    print("\n--- Law of Large Numbers ---")
    running_probs = sim.law_of_large_numbers_demo(1000)
    print(f"Final Converged Probability: {running_probs[-1]:.4f}")

    print("\nInterpretation:")
    print("As the number of days increases, the simulated probability converges to the true probability (0.045).")
    print("Small datasets produce unstable results, making them unreliable for decision-making.")


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Main Execution
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def main():
    print("🚀 Statistical Engineering & Simulation Project\n")

    run_statistical_analysis()
    run_simulation()

    print("\n✅ Execution Completed Successfully")


if __name__ == "__main__":
    main()
