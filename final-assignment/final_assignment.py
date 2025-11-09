import os
import pandas as pd
import matplotlib.pyplot as plt

# folder setup - this was recommended because it is portable for any machine

BASE_DIR = os.getcwd()                  # current project folder
DATA_RAW = os.path.join("data", "raw")  # relative paths
DATA_OUT = os.path.join("data", "processed")
OUTPUTS = "outputs"

os.makedirs(DATA_RAW, exist_ok=True) # here we create the folder, and if it exists nothing happens
os.makedirs(DATA_OUT, exist_ok=True)
os.makedirs(OUTPUTS, exist_ok=True)

csv_path = os.path.join(DATA_RAW, "epl-games_p.csv") 

# Reading a csv file
df = pd.read_csv("C:\\Users\\PC\\Desktop\\MSc in Finance CEU\\1. Fall Term\\Coding for Economists\\python_coding\\data\\raw\\epl-games_p.csv") # when reproducing the code, please insert here the correct path

# Statistics table summary of the current DataFrame

print(df.describe(include="number"))

# Fixing types of data with a for loop
convert_cols_to_int = ["points_home", "points_away", "goals_home", "goals_away"]

for c in convert_cols_to_int:    
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)

# Parse dates (pandas will produce NaT for bad values)
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Keep season as string
if "season" in df.columns:
    df["season"] = df["season"].astype(str)

print("\n types \n", df.dtypes)

# Transformations: total_goals, goal_diff_home, result, dictionary mapping to points
if {"goals_home", "goals_away"}.issubset(df.columns):
    df["total_goals"] = df["goals_home"] + df["goals_away"]
    df["goal_diff_home"] = df["goals_home"] - df["goals_away"]
    # result from home perspective: H=home win, D=draw, A=away win
    df["result"] = df["goal_diff_home"].apply(lambda x: "H" if x > 0 else ("D" if x == 0 else "A"))

    # dictionary mapping 
    points_by_result = {"H": 3, "D": 1, "A": 0}
    df["points_home_from_result"] = df["result"].map(points_by_result)

df[["goals_home","goals_away","total_goals","goal_diff_home","result","points_home_from_result"]].head()

cols = [
    "team_home", "team_away", "points_home_from_result"
]

# Here are the first few rows for illustration
print(df[cols].head(10).to_string(index=False))


# Filter observations
if "date" in df.columns:
    df = df[df["date"].notna()]  # drop rows with missing/invalid dates

if {"goals_home", "goals_away"}.issubset(df.columns):
    df = df[df["goals_home"].notna() & df["goals_away"].notna()]  # keep rows where both goal columns are present

#print("Rows after filtering:", len(df))    # this is for checking if the filtering works
#print(df.head(3).to_string(index=False))

# Filter variables - I will keep all the columns as I need them for further analysis, but here this is done for illustrative purposes
keep_cols = [c for c in [
    "season", "date", "team_home", "team_away",
    "goals_home", "goals_away", "total_goals", "goal_diff_home",
    "result", "points_home", "points_away", "points_home_from_result", "games"
] if c in df.columns]

df_small = df[keep_cols].copy() # Without .copy(), the new DataFrame would still be linked to the original df
df_small.head()

# Saving modified data
clean_path = os.path.join(DATA_OUT, "epl-games_p_clean.csv")
df_small.to_csv(clean_path, index=False)

# Summary table with statistics of the data - also done at the beginning of the code with the "describe" command, only now we are also saving the file in the "outputs" folder
summary_numeric = df_small.describe(include="number").T
summary_file = os.path.join(OUTPUTS, "summary_numeric.csv")
summary_numeric.to_csv(summary_file)

# Create and save a simple plot: average total goals by season
if {"season","total_goals"}.issubset(df_small.columns):
    avg_goals_by_season = (
        df_small
        .groupby("season", as_index=False)["total_goals"]
        .mean()
        .sort_values("season")
    )

    plt.figure()
    plt.plot(avg_goals_by_season["season"], avg_goals_by_season["total_goals"])
    plt.title("Average Total Goals per Match by Season")
    plt.xlabel("Season")
    plt.ylabel("Average Total Goals")
    plt.xticks(rotation=45, ha="right") # here we rotate the years for 45 degrees so they dont overlap
    plt.tight_layout()

    fig_path = os.path.join(OUTPUTS, "avg_total_goals_by_season.png")
    plt.savefig(fig_path, dpi=150)
    plt.show()  
    print("Saved plot to:", fig_path)
else:
    print("Columns 'season' and/or 'total_goals' not found — skipping plot.")

