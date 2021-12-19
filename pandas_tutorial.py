import pandas as pd


namesdf = pd.read_csv('NC.txt')
# # read each column
# print(df[["Name", "Type 1"]])

# read each row
# print(df.iloc[0:4])

# read a specific location
# print(df.iloc[2, 1])

# iterate over rows
# for index, row in df.iterrows():
#     print(index, row["Name"])

# read each row
# print(df.loc[df["Type 1"] == "Grass"])

# print(df.sort_values(["Type 1", "HP"], ascending=[1, 0]))

# find the sum of values in each row
# df["Total"] = df.iloc[:, 4:10].sum(axis=1)
# print(df.head(4))

# print only the fire columns
# print(df.loc[df["Type 1"] == "Fire"

# print(df[["Name", "Total"]].sort_values(["Total"], ascending=False))

# print(df.groupby(["Type 1"]).mean())


# tylerdf = namesdf.loc[(namesdf['Name'] == "Tyler")
#                       & (namesdf['Year'] >= 2015) & (namesdf['Gender'] == "M")]


# tylerdf = tylerdf.reset_index()

# tylerdf.to_csv('NC_Tyler.csv')
