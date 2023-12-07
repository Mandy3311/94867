# Maximizing Bank Profit Success: An Optimized Marketing Strategy

## Credits

This project uses the OptiGuide from [OptiGuide](https://github.com/microsoft/OptiGuide) created by Microsoft. We are grateful to the developers for making the code available for use.

## Code Architecture and design

The main files for this projects are all in the notebook directory.

### notebook/DABP_Sensitivity_Analysis.ipynb
In this file, we make data visualization and sensitivity analysis on the original dataset(downloaded from UCI Machine Learning Repository https://archive.ics.uci.edu/dataset/222/bank+marketing)

### notebook/DABP_Optimization_Model.ipynb
We explore some possible models and constraints that could be applied to our objective function.

### notebook/optiguide.ipynb
This is the file to integrate our model with the Optiguide and then tune the model using the answer from the agents in OptiGuide system.

### notebook/optim1.py, notebook/optim2.py, notebook/optim3.py
The scripts of the models that could possibly suitable to optimize our markting strategies. They will support the interaction with OptiGuide System.

### notebook/data/
Inlude the original dataset and new datasets generated after the data cleaning and feature engineering.

## Walk through the codebase

### Step 1: Run the notebook/DABP_Sensitivity_Analysis.ipynb
This will give an overview of the dataset we'll be using through this project and why we should pay attention to part of the features.

### Step 2: Run the notebook/DABP_Optimization_Model.ipynb
Get ideas about the optimization models we're going to use and learn about the pros & cons of each model. Get the datasets with proper feature engineering.

### Step 3: Change the file path in the model scripts - notebook/optim1.py, notebook/optim2.py, notebook/optim3.py
optim1.py and optim2.py should use notebook/data/before_dummy.csv
optim3.py should use notebook/data/df_train.csv

### Step 4: Preparation before running the notebook/optiguide.ipynb

#### Optional: We would recommand to create a virtual environment to avoid some version conflicts.
```latex
python3 -m venv optiguidevenv
source optiguidevenv/bin/activate
```

#### Install the require packages.
```latex
%pip install optiguide
%pip install pandas
%pip install scikit-learn
%pip install matplotlib
%pip install --upgrade openai
```

#### 
Go to the notebook/optiguide.ipynb and add your ChatGPT API key in the last line in the first code block
For example:
```latex
openai.api_key = 'your-api-key'
```

Finally restart the kernel to make sure all the libraries work.

### Step 5: Run the notebook/optiguide.ipynb
We have already create some conversations with agent1 and agent3(since the model behind agent2 is proved to be not suitable for optimize our marketing strategy). You could create more conversations with three agents supported by different models at the end of the file.

## Appendix
Just for reference, a macbook with 2.3 GHz Quad-Core Intel Core i5 Processor, Intel Iris Plus Graphics 655 1536 MB Graphics, and 8 GB 2133 MHz LPDDR3 Memory could successfully run the project using this guidance.