import pandas as pd
import numpy as np

np.random.seed(0)

n = 5000

# Base features
df = pd.DataFrame({
    'customer_id': np.arange(1, n+1),
    'tenure': np.random.randint(1, 60, size=n),
    'num_transactions_last_month': np.random.poisson(5, size=n),
    'avg_transaction_value': np.random.normal(1200, 300, size=n).round(2),
    'last_login_days_ago': np.random.randint(1, 30, size=n),
    'late_payments': np.random.binomial(5, 0.2, size=n),
    'support_tickets_opened': np.random.poisson(1, size=n),
    'region': np.random.choice(['North', 'South', 'East', 'West'], size=n),
    'plan_type': np.random.choice(['Basic', 'Premium', 'VIP'], size=n)
})

# Simulate base churn probability from behavioral factors
base_churn_prob = (
    0.2 * (df['last_login_days_ago'] > 20).astype(int) +
    0.2 * (df['late_payments'] > 2).astype(int) +
    0.2 * (df['support_tickets_opened'] > 1).astype(int) +
    0.1 * (df['num_transactions_last_month'] < 3).astype(int) +
    0.1 * (df['tenure'] < 10).astype(int)
)

# Add influence from plan and region
region_effect = df['region'].map({'North': 0.05, 'South': 0.1, 'East': -0.05, 'West': 0.0})
plan_effect = df['plan_type'].map({'Basic': 0.1, 'Premium': 0.05, 'VIP': -0.1})

# Combine all effects
total_churn_prob = base_churn_prob + region_effect + plan_effect + np.random.normal(0, 0.05, size=n)

# Clip between 0 and 1
total_churn_prob = np.clip(total_churn_prob, 0, 1)

# Final churn column using binomial sampling
df['churn'] = (np.random.rand(n) < total_churn_prob).astype(int)

# Save to CSV
df.to_csv('realistic_customer_churn.csv', index=False)
print("✅ Realistic churn dataset generated!")

