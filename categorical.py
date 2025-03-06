inmport pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def categorical_analysis(df, categorical_columns, target_column=None):
    """
    Perform categorical analysis including value counts and visualizations.
    
    Parameters:
    df (pd.DataFrame): The dataset.
    categorical_columns (list): List of categorical column names.
    target_column (str, optional): Target column for relationship analysis.
    """
    for col in categorical_columns:
        print(f"\nAnalysis for: {col}")
        print(df[col].value_counts())
        print("-" * 40)
        
        plt.figure(figsize=(8, 4))
        sns.countplot(data=df, x=col, order=df[col].value_counts().index, palette="viridis")
        plt.xticks(rotation=45)
        plt.title(f"Distribution of {col}")
        plt.show()
        
        if target_column:
            plt.figure(figsize=(8, 4))
            sns.countplot(data=df, x=col, hue=target_column, order=df[col].value_counts().index, palette="coolwarm")
            plt.xticks(rotation=45)
            plt.title(f"{col} vs {target_column}")
            plt.show()

# Example Usage:
# df = pd.read_csv("your_data.csv")
# categorical_columns = ["Category1", "Category2"]
# categorical_analysis(df, categorical_columns, target_column="Target")
