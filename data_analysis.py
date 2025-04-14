import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset using a raw string literal for the file path (adjust the path as needed)
df = pd.read_csv(r'C:\Users\Begum\Desktop\Dataset-Hotel Booking Cancellation Prediction.csv')

# Display basic dataset information
print("Dataset Shape:", df.shape)
print("\nDataset Head:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nDescriptive Statistics:")
print(df.describe())

# Calculate Cancellation Percentage (assuming 'is_canceled' column where 1 = cancelled, 0 = not cancelled)
total_bookings = df.shape[0]
cancelled_count = df['is_canceled'].sum()
cancellation_percentage = (cancelled_count / total_bookings) * 100
print(f"\nCancellation Percentage: {cancellation_percentage:.2f}%")

# Calculate Repeated Guest Percentage (assuming 'repeated_guest' column where 1 = repeat guest)
repeated_guest_count = df['repeated_guest'].sum()
repeated_guest_percentage = (repeated_guest_count / total_bookings) * 100
print(f"Repeated Guest Percentage: {repeated_guest_percentage:.2f}%")

# Online vs. Offline Bookings
# (assuming 'market_segment_type' column contains the word 'Online' for online bookings)
online_filter = df['market_segment_type'].str.contains('Online', case=False, na=False)
online_count = df[online_filter].shape[0]
offline_count = total_bookings - online_count
online_percentage = (online_count / total_bookings) * 100
offline_percentage = (offline_count / total_bookings) * 100
print(f"\nOnline Bookings: {online_count} ({online_percentage:.2f}%), Offline Bookings: {offline_count} ({offline_percentage:.2f}%)")

# Plot: Booking Channel Distribution (Online vs. Offline)
plt.figure(figsize=(6, 4))
plt.bar(['Online', 'Offline'], [online_count, offline_count], color=['blue', 'orange'])
plt.title('Booking Channel Distribution')
plt.ylabel('Number of Bookings')
plt.show()

# Plot: Cancellation Distribution
plt.figure(figsize=(6, 4))
cancel_counts = df['is_canceled'].value_counts()
plt.bar(['Not Cancelled', 'Cancelled'], cancel_counts, color=['green', 'red'])
plt.title('Cancellation Distribution')
plt.ylabel('Number of Bookings')
plt.show()

# Plot: Lead Time Distribution for Cancelled Bookings (assuming 'lead_time' column exists)
plt.figure(figsize=(6, 4))
plt.hist(df[df['is_canceled'] == 1]['lead_time'], bins=20, edgecolor='black')
plt.title('Lead Time for Cancelled Bookings')
plt.xlabel('Lead Time (days)')
plt.ylabel('Frequency')
plt.show()

# Plot: Bookings per Arrival Month (assuming 'arrival_month' column exists; months should be sortable)
plt.figure(figsize=(6, 4))
month_counts = df['arrival_month'].value_counts().sort_index()
plt.bar(month_counts.index, month_counts.values, color='purple')
plt.title('Bookings per Arrival Month')
plt.xlabel('Month')
plt.ylabel('Number of Bookings')
plt.show()

# Plot: Bookings per Market Segment
plt.figure(figsize=(8, 4))
market_counts = df['market_segment_type'].value_counts()
plt.bar(market_counts.index, market_counts.values, color='teal')
plt.title('Bookings per Market Segment')
plt.xlabel('Market Segment')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.show()
