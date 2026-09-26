# Interactive Tour Enquiry Dashboard

## Objective

Build an interactive dashboard to analyze tour enquiries and customer requests.

The dashboard provides insights into enquiry volume, popular tour destinations, peak enquiry times, enquiry types, and geographic distribution.

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy

## Dataset

A synthetic tour enquiry dataset was created for this project to demonstrate the dashboard functionality.

The dataset contains 50 tour enquiries with information including:

- Enquiry ID
- Destination
- Enquiry Type
- Enquiry Hour
- Group Size
- Budget
- Latitude
- Longitude

## Dashboard Features

### 1. Total Enquiries
Displays the total number of enquiries based on the selected filters.

### 2. Popular Destination
Identifies the destination receiving the highest number of enquiries.

### 3. Average Group Size
Shows the average number of travelers per enquiry.

### 4. Popular Tour Destinations
A bar chart showing the number of enquiries for each destination.

### 5. Peak Enquiry Times
A line chart showing the distribution of enquiries by hour.

### 6. Geographic Distribution
An interactive map showing the geographic locations of tour enquiries.

### 7. Enquiry Types
A chart showing different types of tour requests such as family tours, adventure trips, honeymoon trips, solo travel, and group tours.

### 8. Interactive Filtering
Users can select one or more destinations from the sidebar to filter the dashboard results.

## Project Files

```text
Task3_Dashboard/
├── README.md
├── tour_enquiry_dashboard.py
└── tour_enquiries.csv