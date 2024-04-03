# NocoBase Python Client

NocoBase is a great Airtable alternative. This client allows python developers
to use NocoBase API in a simple way.

This library is inspired by [ElChicoDe/python-nocodb](https://github.com/ElChicoDePython/python-nocodb).
I appreciate their works.

- [Contributors guidelines](contributors.md)

## Installation

```bash
pip install python-nocobase
```

## Usage

### Client configuration
```python
from nocobase.nocobase import APIToken, JWTAuthToken
from nocobase.infra.requests_client import NocoBaseRequestsClient


# Usage with JWT Token
client = NocoBaseRequestsClient(
        # Your API Token retrieved from NocoBase conf
        JWTAuthToken("your.jwt.token"),
        # Your nocobase root path
        "http://localhost:13000"
)
```

### Collection creation (not implemented yet)
```python
# Example with default database
collection_body = {"title": "My new collection"}

# Example with Postgresql
collection_body = {
    "title": "Mycollection",
    "bases": [
        {
            "type": "pg",
            "config": {
                "client": "pg",
                "connection": {
                    "host": "localhost",
                    "port": "5432",
                    "user": "postgres",
                    "password": "postgres",
                    "database": "postgres"
                },
                "searchPath": [
                    "public"
                ]
            },
            "inflection_column": "camelize",
            "inflection_table": "camelize"
        }
    ],
    "external": True
}

collection = client.collections().create(body=collection_body)
```

### Collection rows operations
```python
collection_name = "my_table"
my_table = client.collection(collection_name)

# Retrieve a page of rows from a table
table_rows = my_table.list()

# Retrieve the first 1000 rows
table_rows = my_table.list(page=1, page_size=1000)

# Skip 100 rows
table_rows = my_table.list(page=2, page_size=100)
```

⚠️ Seems that we can't retrieve more than 1000 rows at the same time but we can paginate
 to retrieve all the rows from a table

Pagination example

```python

for record in my_table.list():
    print(record)
```

More row operations

```python
# Filter the query
table_rows = my_table.list(filter={"name", "%sam%"})
table_rows = my_table.list(filter={"name", "%sam%", "age", 26})
table_rows = my_table.list(filter={"id", 100})

# Find one row
table_row = my_table.list(filter={"id", 100}, sort=["-created_at"])

# Retrieve a single row
row_id = 10
row = my_table.get(id=row_id)

# Create a new row
row_info = {
    "name": "my thoughts",
    "content": "i'm going to buy john a beer 🍻 because I 💚 this module",
    "mood": ":)"
}
my_table.create(row_info)

# Update a row
row_id = 2
row_info = {
    "content": "i'm going to buy john a new car 🚙 because I 💚 this module",
}
my_table.update(id=row_id, body=row_info)

# Delete a row (only if you've already bought me a beer)
my_table.delete(id=row_id)
```

## Author notes

I created this package to bootstrap some personal collections and I hope it
will help other developers from the python community. It's not completed but
it has what I needed: A full CRUD with some filters.

Feel free to add new capabilities by creating a new MR.

## Contributors

![Contributors image](https://contrib.rocks/image?repo=ueki-kazuki/python-nocobase)


- Kazuki UEKI @ueki-kazuki
- and ALL python-nocodb committers
