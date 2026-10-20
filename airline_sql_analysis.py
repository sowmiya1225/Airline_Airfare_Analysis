import pandas as pd
import sqlite3

# ============================================================
# AIRLINE & AIRFARE ANALYTICS - SQLITE
# ============================================================

# ------------------------------------------------------------
# 1. LOAD CLEANED CSV
# ------------------------------------------------------------

df = pd.read_csv("cleaned_airline_airfare.csv")

print("=" * 70)
print("AIRLINE & AIRFARE ANALYTICS - SQLITE")
print("=" * 70)

print("\nDataset Shape:")
print(df.shape)

# ------------------------------------------------------------
# 2. CREATE SQLITE DATABASE
# ------------------------------------------------------------

conn = sqlite3.connect("airline_airfare.db")

df.to_sql(
    "airline_data",
    conn,
    if_exists="replace",
    index=False
)

print("\nSQLite Database Created Successfully!")
print("Database : airline_airfare.db")
print("Table    : airline_data")

# ============================================================
# 3. TOTAL FLIGHTS
# ============================================================

print("\n1. TOTAL FLIGHTS")

query = """
SELECT COUNT(*) AS total_flights
FROM airline_data;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 4. TOTAL AIRLINES
# ============================================================

print("\n2. TOTAL AIRLINES")

query = """
SELECT COUNT(DISTINCT Airline) AS total_airlines
FROM airline_data;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 5. LIST ALL AIRLINES
# ============================================================

print("\n3. ALL AIRLINES")

query = """
SELECT DISTINCT Airline
FROM airline_data
ORDER BY Airline;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 6. FLIGHTS BY AIRLINE
# ============================================================

print("\n4. FLIGHTS BY AIRLINE")

query = """
SELECT
    Airline,
    COUNT(*) AS flight_count
FROM airline_data
GROUP BY Airline
ORDER BY flight_count DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 7. AVERAGE TICKET PRICE
# ============================================================

print("\n5. AVERAGE TICKET PRICE")

query = """
SELECT
    ROUND(AVG(Price), 2) AS average_ticket_price
FROM airline_data;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 8. MINIMUM AND MAXIMUM PRICE
# ============================================================

print("\n6. MINIMUM AND MAXIMUM PRICE")

query = """
SELECT
    MIN(Price) AS minimum_price,
    MAX(Price) AS maximum_price
FROM airline_data;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 9. AVERAGE PRICE BY AIRLINE
# ============================================================

print("\n7. AVERAGE PRICE BY AIRLINE")

query = """
SELECT
    Airline,
    COUNT(*) AS flight_count,
    ROUND(AVG(Price), 2) AS average_price
FROM airline_data
GROUP BY Airline
ORDER BY average_price DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 10. AVERAGE PRICE BY CLASS
# ============================================================

print("\n8. AVERAGE PRICE BY CLASS")

query = """
SELECT
    Class,
    COUNT(*) AS flight_count,
    ROUND(AVG(Price), 2) AS average_price
FROM airline_data
GROUP BY Class
ORDER BY average_price DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 11. AVERAGE PRICE BY STOPS
# ============================================================

print("\n9. AVERAGE PRICE BY STOPS")

query = """
SELECT
    Stops,
    COUNT(*) AS flight_count,
    ROUND(AVG(Price), 2) AS average_price
FROM airline_data
GROUP BY Stops
ORDER BY average_price DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 12. FLIGHTS BY SOURCE
# ============================================================

print("\n10. FLIGHTS BY SOURCE")

query = """
SELECT
    Source,
    COUNT(*) AS flight_count
FROM airline_data
GROUP BY Source
ORDER BY flight_count DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 13. FLIGHTS BY DESTINATION
# ============================================================

print("\n11. FLIGHTS BY DESTINATION")

query = """
SELECT
    Destination,
    COUNT(*) AS flight_count
FROM airline_data
GROUP BY Destination
ORDER BY flight_count DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 14. SOURCE TO DESTINATION ROUTES
# ============================================================

print("\n12. MOST COMMON ROUTES")

query = """
SELECT
    Source,
    Destination,
    COUNT(*) AS flight_count
FROM airline_data
GROUP BY Source, Destination
ORDER BY flight_count DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 15. AVERAGE PRICE BY ROUTE
# ============================================================

print("\n13. AVERAGE PRICE BY ROUTE")

query = """
SELECT
    Source,
    Destination,
    COUNT(*) AS flight_count,
    ROUND(AVG(Price), 2) AS average_price
FROM airline_data
GROUP BY Source, Destination
ORDER BY average_price DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 16. AVERAGE DURATION BY AIRLINE
# ============================================================

print("\n14. AVERAGE FLIGHT DURATION BY AIRLINE")

query = """
SELECT
    Airline,
    ROUND(AVG(DurationHours), 2) AS average_duration
FROM airline_data
GROUP BY Airline
ORDER BY average_duration DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 17. AVERAGE RATING BY AIRLINE
# ============================================================

print("\n15. AVERAGE RATING BY AIRLINE")

query = """
SELECT
    Airline,
    ROUND(AVG(Rating), 2) AS average_rating
FROM airline_data
GROUP BY Airline
ORDER BY average_rating DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 18. AIRLINE + CLASS ANALYSIS
# ============================================================

print("\n16. AIRLINE AND CLASS ANALYSIS")

query = """
SELECT
    Airline,
    Class,
    COUNT(*) AS flight_count,
    ROUND(AVG(Price), 2) AS average_price
FROM airline_data
GROUP BY Airline, Class
ORDER BY Airline, average_price DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 19. AIRLINE + STOPS ANALYSIS
# ============================================================

print("\n17. AIRLINE AND STOPS ANALYSIS")

query = """
SELECT
    Airline,
    Stops,
    COUNT(*) AS flight_count,
    ROUND(AVG(Price), 2) AS average_price
FROM airline_data
GROUP BY Airline, Stops
ORDER BY Airline, average_price DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 20. TOP 10 EXPENSIVE FLIGHTS
# ============================================================

print("\n18. TOP 10 MOST EXPENSIVE FLIGHTS")

query = """
SELECT
    FlightID,
    Airline,
    Source,
    Destination,
    Class,
    Stops,
    Price
FROM airline_data
ORDER BY Price DESC
LIMIT 10;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 21. TOP 10 CHEAPEST FLIGHTS
# ============================================================

print("\n19. TOP 10 CHEAPEST FLIGHTS")

query = """
SELECT
    FlightID,
    Airline,
    Source,
    Destination,
    Class,
    Stops,
    Price
FROM airline_data
ORDER BY Price ASC
LIMIT 10;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 22. ABOVE AVERAGE PRICE
# ============================================================

print("\n20. FLIGHTS ABOVE AVERAGE PRICE")

query = """
SELECT
    FlightID,
    Airline,
    Source,
    Destination,
    Class,
    Price
FROM airline_data
WHERE Price > (
    SELECT AVG(Price)
    FROM airline_data
)
ORDER BY Price DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 23. BELOW AVERAGE PRICE
# ============================================================

print("\n21. FLIGHTS BELOW AVERAGE PRICE")

query = """
SELECT
    FlightID,
    Airline,
    Source,
    Destination,
    Class,
    Price
FROM airline_data
WHERE Price < (
    SELECT AVG(Price)
    FROM airline_data
)
ORDER BY Price ASC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 24. BUSINESS CLASS EXPENSIVE FLIGHTS
# ============================================================

print("\n22. TOP 10 BUSINESS CLASS EXPENSIVE FLIGHTS")

query = """
SELECT
    FlightID,
    Airline,
    Source,
    Destination,
    Price
FROM airline_data
WHERE Class = 'Business'
ORDER BY Price DESC
LIMIT 10;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 25. NON-STOP FLIGHTS
# ============================================================

print("\n23. NON-STOP FLIGHTS BY AIRLINE")

query = """
SELECT
    Airline,
    COUNT(*) AS non_stop_flights
FROM airline_data
WHERE Stops = 'Non-stop'
GROUP BY Airline
ORDER BY non_stop_flights DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 26. AVERAGE BAGGAGE ALLOWANCE
# ============================================================

print("\n24. AVERAGE BAGGAGE ALLOWANCE")

query = """
SELECT
    Airline,
    ROUND(AVG(BaggageAllowanceKg), 2) AS average_baggage_kg
FROM airline_data
GROUP BY Airline
ORDER BY average_baggage_kg DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 27. BOOKING PERIOD ANALYSIS
# ============================================================

print("\n25. BOOKING PERIOD ANALYSIS")

query = """
SELECT
    CASE
        WHEN DaysBeforeBooking <= 7 THEN '0-7 Days'
        WHEN DaysBeforeBooking <= 15 THEN '8-15 Days'
        WHEN DaysBeforeBooking <= 30 THEN '16-30 Days'
        ELSE '31-60 Days'
    END AS booking_period,

    COUNT(*) AS flight_count,

    ROUND(AVG(Price), 2) AS average_price

FROM airline_data

GROUP BY booking_period

ORDER BY average_price DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 28. DISTANCE CATEGORY ANALYSIS
# ============================================================

print("\n26. DISTANCE CATEGORY ANALYSIS")

query = """
SELECT

    CASE
        WHEN DistanceKm <= 800 THEN 'Short'
        WHEN DistanceKm <= 1500 THEN 'Medium'
        WHEN DistanceKm <= 2500 THEN 'Long'
        ELSE 'Very Long'
    END AS distance_category,

    COUNT(*) AS flight_count,

    ROUND(AVG(Price), 2) AS average_price

FROM airline_data

GROUP BY distance_category

ORDER BY average_price DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 29. MONTHLY FLIGHT ANALYSIS
# ============================================================

print("\n27. MONTHLY FLIGHT ANALYSIS")

query = """
SELECT
    Month,
    COUNT(*) AS flight_count,
    ROUND(AVG(Price), 2) AS average_price
FROM airline_data
GROUP BY Month
ORDER BY Month;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 30. SEASONAL ANALYSIS
# ============================================================

print("\n28. SEASONAL ANALYSIS")

query = """
SELECT
    Season,
    COUNT(*) AS flight_count,
    ROUND(AVG(Price), 2) AS average_price
FROM airline_data
GROUP BY Season
ORDER BY average_price DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 31. HIGH VALUE FLIGHTS
# ============================================================

print("\n29. HIGH VALUE FLIGHTS")

query = """
SELECT
    FlightID,
    Airline,
    Source,
    Destination,
    Class,
    Price
FROM airline_data
WHERE Price >= 20000
ORDER BY Price DESC;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 32. MISSING VALUES CHECK
# ============================================================

print("\n30. MISSING VALUES")

query = """
SELECT
    SUM(CASE WHEN Price IS NULL THEN 1 ELSE 0 END)
        AS missing_price,

    SUM(CASE WHEN Rating IS NULL THEN 1 ELSE 0 END)
        AS missing_rating,

    SUM(CASE WHEN BaggageAllowanceKg IS NULL THEN 1 ELSE 0 END)
        AS missing_baggage

FROM airline_data;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 33. DUPLICATE FLIGHT IDs
# ============================================================

print("\n31. DUPLICATE FLIGHT IDs")

query = """
SELECT
    FlightID,
    COUNT(*) AS duplicate_count
FROM airline_data
GROUP BY FlightID
HAVING COUNT(*) > 1;
"""

print(pd.read_sql_query(query, conn))

# ============================================================
# 34. FINAL BUSINESS ANALYSIS
# ============================================================

print("\n32. FINAL BUSINESS ANALYSIS")

query = """
SELECT
    Airline,

    COUNT(*) AS total_flights,

    ROUND(AVG(Price), 2)
        AS average_price,

    ROUND(AVG(DurationHours), 2)
        AS average_duration,

    ROUND(AVG(Rating), 2)
        AS average_rating,

    ROUND(AVG(BaggageAllowanceKg), 2)
        AS average_baggage

FROM airline_data

GROUP BY Airline

ORDER BY average_price DESC;
"""

final_result = pd.read_sql_query(query, conn)

print(final_result)

# ============================================================
# 35. CLOSE DATABASE
# ============================================================

conn.close()

print("\n" + "=" * 70)
print("SQL ANALYSIS COMPLETED SUCCESSFULLY! ✈️📊")
print("=" * 70)

print("\nDatabase Created:")
print("airline_airfare.db")

print("\nTable Created:")
print("airline_data")