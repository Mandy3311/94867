import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from scipy.optimize import linprog
from gurobipy import Model, GRB, quicksum

# Load the dataset
df = pd.read_csv('/Users/enzezhao/Desktop/DABP_OptiGuide_Group_Project_Final/notebook/data/before_dummy.csv')



external_cost  = {'cost_per_call': 2}

profit_per_subscription = {'profit_per_subscription': 10}

constraints = {'max_calls': 1000, 'max_duration': 10000}


# Create a new model
m = Model("marketing_campaign_optimization")

# OPTIGUIDE DATA CODE GOES HERE

# Create variables
x = m.addVars(df.index, vtype=GRB.BINARY, name="x")

# Set objective
m.setObjective(
    quicksum(profit_per_subscription['profit_per_subscription'] * df['P_i'][i] * x[i] for i in df.index) - 
    quicksum(external_cost['cost_per_call'] * x[i] for i in df.index), GRB.MAXIMIZE)

# Add education level constraints
m.addConstr(quicksum(x[i] for i in df.index) <= constraints['max_calls'], name="max_calls")
m.addConstr(quicksum(df.loc[i, 'duration'] * x[i] for i in df.index) <= constraints['max_duration'], name="max_duration")

# Optimize model
m.optimize()


# OPTIGUIDE CONSTRAINT CODE GOES HERE

# Solve
m.update()

if m.status == GRB.OPTIMAL:
    print(f'Optimal value(maximized net profit): {m.objVal}')
else:
    print("Optimization was not successful.")