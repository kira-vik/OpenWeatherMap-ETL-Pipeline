<h1 align="center">OpenWeatherMap ETL Pipeline: From REST API to PostgreSQL</h1>
<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#database-setup">Database Setup</a></li>
      </ul>
    </li>
    <li><a href="#project-architecture">Project Architecture</a></li>
    <li><a href="#future-work">Future Work</a></li>
    <li><a href="#author">Author</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About the Project

![OpenWeatherMap ETL Pipeline.png](https://github.com/kira-vik/OpenWeatherMap-ETL-Pipeline/blob/main/OpenWeatherMap%20ETL%20Pipeline.png)

The **OpenWeatherMap ETL Pipeline** is a Python-based data engineering project that automates the collection, transformation, and storage of real-time weather data into a PostgreSQL database.

Using the **OpenWeatherMap REST API**, the pipeline periodically fetches current weather data for multiple cities, cleans and structures the data, and loads it into a relational database designed for efficient querying and analysis.

This project is designed to demonstrate:

- **ETL pipeline development** (Extract, Transform, Load)
- **API integration** and **data ingestion**
- **Database schema design** and **SQLAlchemy Core usage**
- **Job scheduling and automation**

It’s a step beyond the [Weather App](https://github.com/kira-vik/weather-app-api-project), emphasizing backend data flow and engineering principles used in real-world data infrastructure.

### Features

- Fetches live weather data for multiple cities using OpenWeatherMap’s API
- Uses a **two-table schema** (cities and weather_data) with relational mapping - _Check <a href="#database-setup">Database Setup</a>_
- Prevents duplicate city entries with `ON CONFLICT` handling
- Loads new records with timestamps without overwriting old data
- Uses **SQLAlchemy** for clean and efficient PostgreSQL interaction
- Built-in logging and error handling

### Built With

- **Python 3.14**
- **PostgreSQL**
- Key libraries: **SQLAlchemy**, **Requests**, and more - _check_ `requirements.txt`

<p align="right">
  [<a href="#readme-top">back to top</a>]
</p>

## Getting Started

### Prerequisites

Before running the project, make sure you have the following installed:

- [Python 3.12+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [VS Code](https://code.visualstudio.com/) or your preferred editor
- An [OpenWeatherMap API Key](https://openweathermap.org/api)

### Installation

Clone the repository by running the following command in your project directory:

```bash
git clone {project-link}
```

You can open the cloned repository in VS Code using the command in your project directory:

```bash
code . {project-path}
```

Set up a virtual environment to keep necessary dependencies isolated to this particular project:

```bash
python -m venv {virtual_env_name}
```

Activate the virtual environment: - On Windows:

```bash
{virtual_env_name}\Scripts\activate
```

- On macOS/Linux:

```bash
source {virtual_env_name}/bin/activate
```

- On Windows (in a bash terminal):

```bash
source {virtual_env_name}/Scripts/activate
```

Download the required libraries using the command in your project terminal:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```bash
OPENWEATHERMAP_API_KEY=your_api_key_here
DB_USER=db_user
DB_PASSWORD=db_user_password
DB_HOST=db_host
DB_PORT=db_port
DB_NAME=db_name
```

<p align="right">
  [<a href="#readme-top">back to top</a>]
</p>

### Database Setup

Open a PostgreSQL shell or use your SQL client of choice to create the database and tables:

```sql
CREATE DATABASE weatherdb;
```

Then create the schema:

```sql
CREATE TABLE cities (
    city_id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    country_code VARCHAR(10) NOT NULL,
    longitude DOUBLE PRECISION,
    latitude DOUBLE PRECISION,
    UNIQUE (city, country_code)
);

CREATE TABLE weather_data (
    weather_id SERIAL PRIMARY KEY,
    city_id INT NOT NULL,
    temperature DOUBLE PRECISION NOT NULL,
    humidity INT,
    pressure INT,
    wind_speed DOUBLE PRECISION,
    cloudiness INT,
    weather_description VARCHAR(255),
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT fk_city FOREIGN KEY (city_id)
        REFERENCES cities(city_id)
        ON DELETE CASCADE
);
```

<p align="right">
  [<a href="#readme-top">back to top</a>]
</p>

## Project Architecture

```bash
weather_etl/
│
├── app.py                      # Entry point for the ETL pipeline
├── config/
│   ├── __init__.py             # Package initializer
│   └── db_config.py            # SQLAlchemy DB engine setup
│
├── services/
│   ├── __init__.py             # Package initializer
│   ├── weather_service.py      # Handles weather data extraction and transformation
│   └── db_service.py           # Handles PostgreSQL insertions and queries
│
├── utils/
│   ├── __init__.py             # Package initializer
│   └── logger.py               # Configures and manages logging
│
├── .env                        # Environment variable definitions
├── .gitignore                  # Untracked files to ignore in Git
├── .gitattributes              # Git config for file handling
├── LICENSE.txt                 # Project license information
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview and usage instructions
```

## Future Work

While the ETL currently runs manually or via simple scheduling, future updates will include:

- Automated scheduling using APScheduler or Airflow
- Data visualization dashboard for weather trends
- Analytical extensions, such as weather forecasting
- Containerization using Docker for portability

 > _A PROBLEM FOR FUTURE ME_

 <p align="right">
  [<a href="#readme-top">back to top</a>]
</p>

  <!--AUTHOR-->
## Author

  Victor Weke - @[kira-vik](https://github.com/kira-vik)

  Project Link: [OpenWeatherMap ETL Pipeline](https://github.com/kira-vik/weather-app-api-project)
  
  <!--LICENSE-->
## License
  
  Copyright © 2025, Victor Weke.
  
  Distributed under the [MIT](https://choosealicense.com/licenses/mit/) license. See LICENSE.txt for more information.

<p align="right">
  [<a href="#readme-top">back to top</a>]
</p>
