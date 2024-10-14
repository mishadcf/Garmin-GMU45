# **Winter GMU45 Dashboard Project**

![Dashboard Screenshot](link-to-your-screenshot.png)

## **Introduction**

After recovering from a running injury, I set a new goal: to complete the **Winter Green Man Ultra** in March 2025. Combining my passion for running and data science, I've embarked on a project to build a personalized training dashboard using data from my Garmin watch.

This project aims to:

- **Optimize Training:** Provide a customized overview of my running data to enhance my training regimen.
- **Demonstrate Data Skills:** Apply and showcase my data analysis and visualization expertise through a real-world application.
- **Create a Versatile Tool:** Develop a dashboard that could potentially benefit other Garmin users seeking personalized data insights.
- **More to come...**


## **Table of Contents**

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Progress](#project-progress)
  - [Completed Milestones](#completed-milestones)
  - [Data Insights](#data-insights)
  - [Next Steps](#next-steps)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## **Features**

- **Automated Data Retrieval:** Batch scraping of Garmin activity data using an extended functionality of the `garminexpress` package.
- **Data Processing and Storage:** Parsing and storing data from various file formats (.FIT, .TCX, .GPX, .CSV).
- **Interactive Dashboard:** Built with Dash and Plotly, featuring:
  - **Weekly Mileage Tracker:** Visualizes weekly running mileage against a 10% incremental target leading up to race day.
  - **Countdown Timer:** Displays the time remaining until the Winter Green Man Ultra 2025.
  - **Route Mapping:** Visualizes running routes using GeoPandas and GPX data.
- **Scalable Architecture:** Plans to implement AWS Lambda functions for automated data updates.

## **Technologies Used**

- **Programming Languages:** Python
- **Data Processing:** Pandas, GeoPandas
- **Data Visualization:** Plotly, Dash
- **Web Framework:** Dash (by Plotly)
- **Data Retrieval:** `garminexpress` package
- **Cloud Services (Planned):** AWS Lambda
- **File Formats:** .FIT, .TCX, .GPX, .CSV

## **Installation**

To set up the project locally:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/winter-gmu45-dashboard.git


## **Project Progress**

### **Progress So Far**

#### **Project Planning**

- **Brainstormed End-Product:**
  - Envisioned a deployed web app featuring a dashboard with my data, updating daily or semi-daily with the latest Garmin data.

#### **Data Extraction**

- **Utilized `garminexport` Package:**
  - Found and extended the existing GitHub package `garminexport` to allow batch scraping.
- **Data Retrieval:**
  - Successfully pulled all of my activity data from Garmin, obtaining `.csv`, `.tcx`, `.gpx`, and `.zip` files.

#### **Data Exploration**

- **File Content Analysis:**
  - Explored the data within the files to determine relevance for the dashboard.
- **Route Plotting:**
  - Experimented with plotting GPX files using GeoPandas for route visualization.

#### **Dashboard Development**

- **Template Creation:**
  - Developed a template Dash application to work towards the end product.
- **Weekly Mileage Tracker:**
  - Generated the first useful graph—a weekly mileage tracker versus a 10% increase limit until the race date—using Pandas and Plotly Go.
- **Dashboard Integration:**
  - Placed the graph on the dashboard along with a countdown timer until the race.

---

### **Data Content Findings**

- **`.FIT` Files:**
  - Provide the most detailed and comprehensive data, including advanced fitness metrics.
  - Useful for adding heart rate, cadence, power, and other advanced metrics to the dashboard.
- **`.TCX` Files:**
  - Similar data to `.FIT` files but in a more readable XML format.
  - Less efficient for large datasets but easier to inspect manually.
- **`.GPX` Files:**
  - Focus on GPS location and route data.
  - Useful for visualizing routes but lack detailed fitness metrics.
- **`.CSV` Files:**
  - Good for summary statistics.
  - Lack detailed data such as heart rate or cadence.

---

### **Next Steps**

#### **Automation**

- **AWS Lambda Functions:**
  - Learn how to use AWS Lambda functions to automate data retrieval through the Garmin API.

#### **Dashboard Enhancement**

- **Visual Improvements:**
  - Make the dashboard more visually appealing and improve the user interface.
- **Additional Features:**
  - Add more features to the dashboard, such as:
    - Heart rate zone analysis.
    - Elevation gain over time.
    - Interactive route maps.

#### **Scalability**

- **Customization for Other Users:**
  - Once the dashboard is polished, useful, and has robust data retrieval, consider making it customizable for other Garmin users.

#### **Advanced Analytics**

- **Predictive Analytics:**
  - Incorporate predictive analytics to forecast performance.
- **Metric Correlation Analysis:**
  - Analyze correlations between different training metrics.
