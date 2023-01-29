import time
from clickhouse_driver import Client

# Connect to the ClickHouse server
client = Client('hostname', user='username', password='password')

while True:
    # Execute a query to retrieve index usage statistics
    result = client.execute('SELECT index, bytes_read, query_time_ms FROM system.indices')

    # Print the results
    for row in result:
        print(f"Index: {row[0]}, Bytes Read: {row[1]}, Query Time (ms): {row[2]}")

    # Sleep for 2 seconds
    time.sleep(2)
