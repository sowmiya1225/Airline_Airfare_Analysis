import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. LOAD CSV DATASET
# ============================================================

df = pd.read_csv("airline_airfare_dataset.csv")

print("=" * 60)
print("AIRLINE & AIRFARE ANALYTICS")
print("=" * 60)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

# ============================================================
# 2. MISSING VALUES
# ============================================================

print("\nMissing Values:")
print(df.isnull().sum())

# ============================================================
# 3. DUPLICATE VALUES
# ============================================================

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# ============================================================
# 4. REMOVE DUPLICATES
# ============================================================

df = df.drop_duplicates()

print("\nAfter Removing Duplicates:")
print("Rows:", len(df))
print("Duplicates:", df.duplicated().sum())

# ============================================================
# 5. HANDLE MISSING VALUES
# ============================================================

df["Price"] = df["Price"].fillna(
    df["Price"].median()
)

df["Rating"] = df["Rating"].fillna(
    df["Rating"].median()
)

df["BaggageAllowanceKg"] = df["BaggageAllowanceKg"].fillna(
    df["BaggageAllowanceKg"].median()
)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ============================================================
# 6. CONVERT DATE
# ============================================================

df["FlightDate"] = pd.to_datetime(df["FlightDate"])

print("\nData Types:")
print(df.dtypes)

# ============================================================
# 7. BASIC STATISTICS
# ============================================================

print("\nBasic Statistics:")
print(df.describe())

# ============================================================
# 8. AIRLINE ANALYSIS
# ============================================================

print("\nFlights by Airline:")
print(df["Airline"].value_counts())

print("\nAverage Price by Airline:")

avg_airline_price = (
    df.groupby("Airline")["Price"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

print(avg_airline_price)

# ============================================================
# 9. CLASS ANALYSIS
# ============================================================

print("\nFlights by Class:")
print(df["Class"].value_counts())

print("\nAverage Price by Class:")

avg_class_price = (
    df.groupby("Class")["Price"]
    .mean()
    .round(2)
)

print(avg_class_price)

# ============================================================
# 10. STOPS ANALYSIS
# ============================================================

print("\nFlights by Stops:")
print(df["Stops"].value_counts())

print("\nAverage Price by Stops:")

avg_stop_price = (
    df.groupby("Stops")["Price"]
    .mean()
    .round(2)
)

print(avg_stop_price)

# ============================================================
# 11. SOURCE CITY ANALYSIS
# ============================================================

print("\nFlights by Source:")
print(df["Source"].value_counts())

# ============================================================
# 12. DESTINATION ANALYSIS
# ============================================================

print("\nFlights by Destination:")
print(df["Destination"].value_counts())

# ============================================================
# 13. MONTHLY FLIGHT ANALYSIS
# ============================================================

print("\nFlights by Month:")

monthly_flights = (
    df.groupby(df["FlightDate"].dt.month)["FlightID"]
    .count()
)

print(monthly_flights)

# ============================================================
# 14. OVERALL AVERAGE PRICE
# ============================================================

average_price = df["Price"].mean()

print("\nOverall Average Ticket Price:")
print(round(average_price, 2))

# ============================================================
# 15. AVERAGE FLIGHT DURATION
# ============================================================

average_duration = df["DurationHours"].mean()

print("\nAverage Flight Duration:")
print(round(average_duration, 2), "hours")

# ============================================================
# 16. AVERAGE RATING
# ============================================================

average_rating = df["Rating"].mean()

print("\nAverage Rating:")
print(round(average_rating, 2))

# ============================================================
# 17. TOP 10 EXPENSIVE FLIGHTS
# ============================================================

print("\nTop 10 Most Expensive Flights:")

top_expensive = df.sort_values(
    by="Price",
    ascending=False
).head(10)

print(
    top_expensive[
        [
            "FlightID",
            "Airline",
            "Source",
            "Destination",
            "Class",
            "Stops",
            "Price"
        ]
    ]
)

# ============================================================
# 18. TOP 10 CHEAPEST FLIGHTS
# ============================================================

print("\nTop 10 Cheapest Flights:")

cheapest = df.sort_values(
    by="Price",
    ascending=True
).head(10)

print(
    cheapest[
        [
            "FlightID",
            "Airline",
            "Source",
            "Destination",
            "Class",
            "Stops",
            "Price"
        ]
    ]
)

# ============================================================
# 19. AIRLINE + CLASS PRICE ANALYSIS
# ============================================================

print("\nAverage Price by Airline and Class:")

airline_class_price = (
    df.groupby(
        ["Airline", "Class"]
    )["Price"]
    .mean()
    .round(2)
)

print(airline_class_price)

# ============================================================
# 20. DISTANCE CATEGORY
# ============================================================

df["DistanceCategory"] = pd.cut(
    df["DistanceKm"],
    bins=[0, 800, 1500, 2500, 4000],
    labels=[
        "Short",
        "Medium",
        "Long",
        "Very Long"
    ]
)

print("\nAverage Price by Distance:")

print(
    df.groupby(
        "DistanceCategory",
        observed=True
    )["Price"]
    .mean()
    .round(2)
)

# ============================================================
# 21. BOOKING PERIOD ANALYSIS
# ============================================================

df["BookingCategory"] = pd.cut(
    df["DaysBeforeBooking"],
    bins=[0, 7, 15, 30, 60],
    labels=[
        "0-7 Days",
        "8-15 Days",
        "16-30 Days",
        "31-60 Days"
    ]
)

print("\nAverage Price by Booking Period:")

print(
    df.groupby(
        "BookingCategory",
        observed=True
    )["Price"]
    .mean()
    .round(2)
)

# ============================================================
# 22. CHART - FLIGHTS BY AIRLINE
# ============================================================

airline_count = df["Airline"].value_counts()

plt.figure(figsize=(9, 5))

bars = plt.bar(
    airline_count.index,
    airline_count.values
)

plt.title(
    "Number of Flights by Airline",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Airline")
plt.ylabel("Number of Flights")

plt.xticks(rotation=30)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 5,
        str(int(height)),
        ha="center"
    )

plt.tight_layout()
plt.show()

# ============================================================
# 23. CHART - AVERAGE PRICE BY AIRLINE
# ============================================================

plt.figure(figsize=(9, 5))

bars = plt.bar(
    avg_airline_price.index,
    avg_airline_price.values
)

plt.title(
    "Average Ticket Price by Airline",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Airline")
plt.ylabel("Average Ticket Price")

plt.xticks(rotation=30)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 100,
        f"₹{height:,.0f}",
        ha="center"
    )

plt.tight_layout()
plt.show()

# ============================================================
# 24. CHART - PRICE BY CLASS
# ============================================================

plt.figure(figsize=(7, 5))

bars = plt.bar(
    avg_class_price.index,
    avg_class_price.values
)

plt.title(
    "Average Ticket Price by Class",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Class")
plt.ylabel("Average Ticket Price")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 100,
        f"₹{height:,.0f}",
        ha="center"
    )

plt.tight_layout()
plt.show()

# ============================================================
# 25. CHART - FLIGHTS BY STOPS
# ============================================================

stop_count = df["Stops"].value_counts()

plt.figure(figsize=(7, 5))

bars = plt.bar(
    stop_count.index,
    stop_count.values
)

plt.title(
    "Number of Flights by Stops",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Stops")
plt.ylabel("Number of Flights")

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 5,
        str(int(height)),
        ha="center"
    )

plt.tight_layout()
plt.show()

# ============================================================
# 26. CHART - MONTHLY FLIGHT TREND
# ============================================================

plt.figure(figsize=(9, 5))

plt.plot(
    monthly_flights.index,
    monthly_flights.values,
    marker="o"
)

plt.title(
    "Monthly Flight Trend",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Month")
plt.ylabel("Number of Flights")

plt.xticks(range(1, 13))

plt.grid(
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()
plt.show()

# ============================================================
# 27. FINAL SUMMARY
# ============================================================

print("\n")
print("=" * 60)
print("FINAL ANALYSIS SUMMARY")
print("=" * 60)

print("Total Flights:", len(df))

print(
    "Number of Airlines:",
    df["Airline"].nunique()
)

print(
    "Average Ticket Price:",
    round(df["Price"].mean(), 2)
)

print(
    "Average Flight Duration:",
    round(df["DurationHours"].mean(), 2),
    "hours"
)

print(
    "Average Rating:",
    round(df["Rating"].mean(), 2)
)

print(
    "Most Common Airline:",
    df["Airline"].mode()[0]
)

print(
    "Most Common Source:",
    df["Source"].mode()[0]
)

print(
    "Most Common Destination:",
    df["Destination"].mode()[0]
)

# ============================================================
# 28. SAVE CLEANED CSV
# ============================================================

df.to_csv(
    "cleaned_airline_airfare.csv",
    index=False
)

print("\nCleaned dataset saved:")
print("cleaned_airline_airfare.csv")

print("\nAnalysis completed successfully! ✈️📊")