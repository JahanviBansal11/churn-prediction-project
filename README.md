# Customer Churn Prediction

This project focuses on predicting whether a customer is likely to churn (leave a service) using behavioral and transactional data. The goal is to help businesses identify at-risk customers early so they can take steps to retain them.

---

## Overview

 Project uses a synthetic dataset that simulates real customer behavior, including:

- Time since joining (`tenure`)
- Recent transactions
- Average spend
- Login activity
- Support interactions
- Payment delays

Each customer is labeled as either "churned" (1) or "retained" (0) based on their activity patterns.

---

## Feature Engineering

To improve model accuracy, I created new features that give more insight into customer behavior:

- `engagement_score`: Combines login activity and transaction frequency  
- `payment_risk`: Highlights customers with frequent late payments  
- `support_burden`: Flags customers with lots of support issues  
- `high_value_customer`: Identifies customers who spend more than ₹1500  
- `is_loyal`: Tags customers with over 3 years of tenure  

These features help the model understand patterns that lead to churn more effectively.

---

## Tools Used

- Python (Pandas, NumPy)
- Scikit-learn (Random Forest, GridSearchCV)
- Jupyter Notebook

---

## Results

- The final model achieved high accuracy after tuning and feature engineering  
- Key drivers of churn include inactivity, late payments, and support issues

---

## Next Steps

- Try advanced models like XGBoost  
- Use SHAP to explain predictions  
- Segment users for targeted retention strategies

---

Built by **Jahanvi Bansal** to explore how data-driven insights can help in product and customer decision-making.
