# **Winter GMU45 Dashboard Project**

![Dashboard Screenshot](link-to-your-screenshot.png)

## **Introduction**

After recovering from a running injury, I set an ambitious goal: to complete the **Winter Green Man Ultra** in March 2025. Combining my passion for running and data science, I've embarked on a project to build a personalized training dashboard using data from my Garmin watch.

This project aims to:

- **Optimize Training:** Provide a customized overview of my running data to enhance my training regimen.
- **Demonstrate Data Skills:** Apply and showcase my data analysis and visualization expertise through a real-world application.
- **Create a Versatile Tool:** Develop a dashboard that could potentially benefit other Garmin users seeking personalized data insights.

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

- **Automated Data Retrieval:** Batch scraping of Garmin activity data using an extended functionality of the `garminexport` package.
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
- **Data Retrieval:** `garminexport` package
- **Cloud Services (Planned):** AWS Lambda
- **File Formats:** .FIT, .TCX, .GPX, .CSV

## **Installation**

To set up the project locally:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/winter-gmu45-dashboard.git
