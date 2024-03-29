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

### Collection creation
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
my_table = client.collections.get(collection_name)

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

### Available filters

- EqFilter
- EqualFilter (Alias of EqFilter)
- NotEqualFilter
- GreaterThanFilter
- GreaterOrEqualFilter
- LessThanFilter
- LessOrEqualFilter
- LikeFilter
- Or
- Not
- And

#### Combining filters using Logical operations

```python
from nocobase import filters

# Basic filters...
nick_filter = filters.EqFilter("nickname", "elchicodepython")
country_filter = filters.EqFilter("country", "es")
girlfriend_code = filters.EqFilter("gfcode", "404")
current_mood_code = filters.EqFilter("moodcode", "418")

# Combining filters using logical filters
or_filter = filters.Or(nick_filter, country_filter)
and_filter = filters.And(girlfriend_code, current_mood_code)

# Negating filters with a Not filter
not_me = filters.Not(filters.EqFilter("nickname", "elchicodepython"))

# You can also combine combinations
or_combined_filter = filters.Or(or_filter, and_filter)
and_combined_filter = filters.And(or_filter, and_filter)

```

### Using custom filters

nocobase is evolving and new operators are coming with each release.

Most of the basic operations are inside this package but you could need some new
feature that could not be added yet.
For those filters you can build your own.

Example for basic filters:

```python
from nocobase.filters.factory import basic_filter_class_factory

BasicFilter = basic_filter_class_factory('=')
table_rows = client.list(collection_name, BasicFilter('age', '16'))

```

You can find the updated list of all the available nocobase operators [here](https://docs.nocobase.com/developer-resources/rest-apis/#comparison-operators).

In some cases you might want to write your own filter string as described in the previous link.
For that cases you can use the less-semmantic RawFilter.

```python
from nocobase.filters.raw_filter import RawFilter

table_rows = client.list(collection_name, RawFilter('(birthday,eq,exactDate,2023-06-01)'))
```

In some cases we might want to have a file with some custom raw filters already defined by us.
We can easily create custom raw filter classes using `raw_template_filter_class_factory`.

```python
from nocobase.filters.factory import raw_template_filter_class_factory

BirthdayDateFilter = raw_template_filter_class_factory('(birthday,eq,exactDate,{})')
ExactDateEqFilter = raw_template_filter_class_factory('({},eq,exactDate,{})')
ExactDateOpFilter = raw_template_filter_class_factory('({},{op},exactDate,{})')

table_rows = client.list(collection_name, BirthdayDateFilter('2023-06-01'))
table_rows = client.list(collection_name, ExactDateEqFilter('column', '2023-06-01'))
table_rows = client.list(collection_name, ExactDateOpFilter('column', '2023-06-01', op='eq'))
```


Credits to @MitPitt for asking this feature.

## Author notes

I created this package to bootstrap some personal collections and I hope it
will help other developers from the python community. It's not completed but
it has what I needed: A full CRUD with some filters.

Feel free to add new capabilities by creating a new MR.

## Contributors

![Contributors image](https://contrib.rocks/image?repo=ueki-kazuki/python-nocobase)


- Kazuki UEKI @ueki-kazuki

