import numpy as np

np.random.seed(42)

runs = np.random.randint(0, 5000, 100)          # total runs
balls = np.random.randint(1, 4000, 100)         # balls faced
wickets = np.random.randint(0, 200, 100)        # wickets taken
matches = np.random.randint(1, 300, 100)        # matches played

strike_rate = (runs / balls) * 100

cricket_data = np.column_stack((runs, balls, wickets, matches, strike_rate))

print("Dataset Shape:", cricket_data.shape)
print("\nFirst 5 Records:\n", cricket_data[:5])

print("\nAverage Runs:", np.mean(runs))

print("Highest Runs:", np.max(runs))

print("Lowest Runs:", np.min(runs))

print("Runs Standard Deviation:", np.std(runs))

print("Runs Variance:", np.var(runs))

print("90th Percentile Runs:", np.percentile(runs, 90))

print("Total Runs:", np.sum(runs))

high_sr = strike_rate > 120
print("Players with Strike Rate >120:", np.sum(high_sr))

high_wickets = wickets > 50
print("Players with >50 Wickets:", np.sum(high_wickets))

runs_per_match = runs / matches
print("Average Runs per Match:", np.mean(runs_per_match))

sorted_runs = np.sort(runs)
print("Top 5 Highest Scores:", sorted_runs[-5:])

correlation = np.corrcoef(runs, matches)
print("Correlation Matrix (Runs vs Matches):\n", correlation)

print("Median Strike Rate:", np.median(strike_rate))

experienced = matches > 200
print("Players with >200 Matches:", np.sum(experienced))