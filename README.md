Observed weather data scrapper
==============================

This scrapper is designed to use with an _unnamed_ lithuanian weather website.

## Running

1. Copy the `.env.dist` to `.env` and provide the configuration values.

2. Start the container
    ```shell
    docker-compose up -d
    ```
3. To pull the data to the database, run:
    ```shell
    ./run.sh
    ```