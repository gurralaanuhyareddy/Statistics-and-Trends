"""
This is the template file for the statistics and trends assignment.
You will be expected to complete all the sections and
make this a fully working, documented file.
You should NOT change any function, file or variable names,
 if they are given to you here.
Make use of the functions presented in the lectures
and ensure your code is PEP-8 compliant, including docstrings.
"""
from corner import corner
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss
import seaborn as sns


def plot_relational_plot(df):
    fig, ax = plt.subplots()
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        data=df,
        x="Session_Duration (hours)",  # <-- Correct column name
        y="Calories_Burned",
        hue="Workout_Type",
        alpha=0.7
    )
    plt.title("Session Duration vs Calories Burned")
    plt.xlabel("Session Duration (hours)")
    plt.ylabel("Calories Burned")
    plt.legend(title="Workout Type", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig("relational_plot.png")
    return


def plot_categorical_plot(df):
    """
    Create and save a categorical plot comparing calories burned across workout types.
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(
        data=df,
        x="Workout_Type",
        y="Calories_Burned",
        palette="Set2"
    )
    plt.title("Calories Burned by Workout Type")
    plt.xlabel("Workout Type")
    plt.ylabel("Calories Burned")
    plt.tight_layout()
    plt.savefig("categorical_plot.png")
    plt.close()
    return


def plot_statistical_plot(df):
    """
    Create and save a histogram with KDE for calories burned distribution.
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(df["Calories_Burned"], kde=True, color="skyblue")
    plt.title("Distribution of Calories Burned")
    plt.xlabel("Calories Burned")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("statistical_plot.png")
    plt.close()
    return


def statistical_analysis(df, col: str):
    """
    Compute and return mean, std dev, skewness, and excess kurtosis for a given column.
    """
    mean = df[col].mean()
    stddev = df[col].std()
    skew = ss.skew(df[col])
    excess_kurtosis = ss.kurtosis(df[col])
    return mean, stddev, skew, excess_kurtosis
    


def preprocessing(df):
    """
    Preprocess the dataset by checking basic statistics, missing values,
    and correlation among numeric columns.
    """
    print("First five rows of data:")
    print(df.head())

    print("\nSummary statistics:")
    print(df.describe())

    print("\nMissing values per column:")
    print(df.isnull().sum().sum())

    # Correlation heatmap (optional visualization)
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.select_dtypes(include=[np.number]).corr(), cmap="coolwarm", center=0)
    plt.title("Correlation Heatmap (Numeric Columns)")
    plt.tight_layout()
    plt.savefig("correlation_heatmap.png")
    plt.close()
    return df

def writing(moments, col):
    """
    Print the computed statistical moments and interpret skewness/kurtosis.
    """
    mean, stddev, skew, excess_kurtosis = moments
    print(f"\nFor the attribute '{col}':")
    print(f"Mean = {mean:.2f}")
    print(f"Standard Deviation = {stddev:.2f}")
    print(f"Skewness = {skew:.2f}")
    print(f"Excess Kurtosis = {excess_kurtosis:.2f}")

    # Interpretation
    if skew > 0.5:
        skew_text = "right-skewed"
    elif skew < -0.5:
        skew_text = "left-skewed"
    else:
        skew_text = "approximately symmetric"

    if excess_kurtosis > 1:
        kurt_text = "leptokurtic (heavy tails)"
    elif excess_kurtosis < -1:
        kurt_text = "platykurtic (light tails)"
    else:
        kurt_text = "mesokurtic (normal tails)"

    print(f"The data is {skew_text} and {kurt_text}.")
    return
 
def main():
    df = pd.read_csv("Final_data.csv")
    df = preprocessing(df)
    col = "Calories_Burned"
    plot_relational_plot(df)
    plot_statistical_plot(df)
    plot_categorical_plot(df)
    moments = statistical_analysis(df, col)
    writing(moments, col)
    return


if __name__ == "__main__":
    main()
    

