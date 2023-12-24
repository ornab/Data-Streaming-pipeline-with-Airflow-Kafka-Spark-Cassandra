## Project Overview

Welcome to our data pipeline project! Here, we handle data from an API endpoint using essential tools like Apache Airflow, Kafka, Apache Spark, and Cassandra, all managed within Docker containers.

### Data Journey:

1. **Data Collection:** We start by fetching data from ```randomuser.me``` API endpoint to generate random user data for our pipeline..
2. **Workflow Management:** Apache Airflow organizes data flow and storing fetched data in a PostgreSQL database.
3. **Streaming via Kafka & Zookeeper:** Data seamlessly streams from PostgreSQL to the processing engine using Kafka, enabling efficient real-time processing.
4. **Control Center and Schema Registry:** Helps in monitoring and schema management of our Kafka streams.
5. **Processing with Spark:** Apache Spark processes and derives insights from the data.
6. **Storage in Cassandra:**  Finally, Cassandra provides a reliable home for our valuable processed data.

### Tools

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker

### Proejct Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/ornab/Data-Streaming-pipeline-with-Airflow-Kafka-Spark-Cassandra.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Data-Streaming-pipeline-with-Airflow-Kafka-Spark-Cassandra
    ```

3. Run Docker Compose to spin up the services:
    ```bash
    docker-compose up -d
    ```
