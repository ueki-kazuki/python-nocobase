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
from nocobase.nocobase import JWTAuthToken
from nocobase.infra.requests_client import NocoBaseRequestsClient

# Usage with JWT Token
client = NocoBaseRequestsClient(
        # Your JWT Token retrieved from NocoBase
        JWTAuthToken("your.jwt.token"),
        # Your NocoBase root path
        "http://localhost:13000"
)
```

### Collections management
```python
# List all collections
collections = client.collections().list()
for collection in collections:
    print(f"Collection: {collection.name}")

# Get a specific collection by name
try:
    my_collection = client.collection("my_table_name")
    print(f"Found collection: {my_collection.name}")
except NocoBaseCollectionNotFoundError:
    print("Collection not found")

# Get collection by name using collections manager
collections_manager = client.collections()
my_collection = collections_manager.get("my_table_name")
```

### Collection creation (not implemented yet)
Collection creation, update, and deletion methods are defined but not yet implemented. The following methods are available in the Collections class but need implementation:

```python
collections = client.collections()
# These methods exist but are not implemented yet:
# collections.create()
# collections.update() 
# collections.destroy()
# collections.move()
# collections.set_fields()
```

### Collection rows operations
```python
collection_name = "my_table"
my_table = client.collection(collection_name)

# Retrieve all rows from a table (with automatic pagination)
for row in my_table.list():
    print(row)

# Retrieve a specific page of rows
table_rows = list(my_table.list(page=1, page_size=100))

# Retrieve rows with pagination parameters
table_rows = list(my_table.list(page=2, page_size=100))  # Skip first 100 rows
```

⚠️ The list() method returns a generator that automatically handles pagination. You can iterate through all rows or convert to a list for a specific page.

### Advanced querying
```python
# Filter the query (filter parameter expects a dictionary)
filtered_rows = list(my_table.list(filter={"name": "sam"}))
filtered_rows = list(my_table.list(filter={"name": "sam", "age": 26}))
filtered_rows = list(my_table.list(filter={"id": 100}))

# Sort results (use - prefix for descending order)
sorted_rows = list(my_table.list(sort=["-created_at", "name"]))

# Select specific fields only
selected_fields = list(my_table.list(fields=["id", "name", "email"]))

# Include related data
with_relations = list(my_table.list(appends=["user", "category"]))

# Exclude specific fields
without_fields = list(my_table.list(excepts=["password", "internal_notes"]))

# Combine multiple parameters
complex_query = list(my_table.list(
    filter={"status": "active"},
    sort=["-created_at"],
    fields=["id", "name", "status"],
    page_size=50
))
```

### Single row operations
```python
# Retrieve a single row by ID
row_id = 10
row = my_table.get(id=row_id)

# Get a row with specific fields
row = my_table.get(id=row_id, fields=["id", "name", "email"])

# Get a row with filter (instead of ID)
row = my_table.get(filter={"email": "user@example.com"})

# Get a row with sorting and relations
row = my_table.get(
    id=row_id,
    appends=["user_profile"],
    sort=["-updated_at"]
)
```

### Creating and updating rows
```python
# Create a new row
row_info = {
    "name": "my thoughts",
    "content": "i'm going to buy john a beer 🍻 because I 💚 this module",
    "mood": ":)"
}
created_row = my_table.create(row_info)

# Create with field whitelist (only these fields will be saved)
created_row = my_table.create(row_info, whitelist=["name", "content"])

# Create with field blacklist (these fields will be ignored)
created_row = my_table.create(row_info, blacklist=["internal_field"])

# Update a row by ID
row_id = 2
row_info = {
    "content": "i'm going to buy john a new car 🚙 because I 💚 this module",
}
updated_row = my_table.update(id=row_id, body=row_info)

# Update with filter (instead of ID)
updated_row = my_table.update(
    filter={"email": "user@example.com"},
    body={"status": "verified"}
)

# Update with whitelist/blacklist
updated_row = my_table.update(
    id=row_id,
    body=row_info,
    whitelist=["content", "mood"]
)
```

### Error handling
```python
from nocobase.exceptions import NocoBaseAPIError, NocoBaseCollectionNotFoundError

try:
    # Try to get a collection that doesn't exist
    my_table = client.collection("nonexistent_table")
except NocoBaseCollectionNotFoundError as e:
    print(f"Collection not found: {e}")

try:
    # Try an API operation that might fail
    row = my_table.get(id=999999)
except NocoBaseAPIError as e:
    print(f"API Error: {e}")
    print(f"Status Code: {e.status_code}")
    print(f"Response: {e.response_json}")
```

## Current Implementation Status

### ✅ Implemented Features
- **Authentication**: JWT token-based authentication
- **Collections Management**: List and retrieve collections
- **Row Operations**: Full CRUD operations (Create, Read, Update)
- **Advanced Querying**: Filtering, sorting, field selection, pagination
- **Error Handling**: Custom exceptions for API errors and collection not found
- **Automatic Pagination**: Generator-based iteration through large datasets

### ⚠️ Partially Implemented
- **Collection Management**: Collection creation, update, and deletion methods exist but are not implemented
- **Row Deletion**: The `destroy` method is defined in the abstract class but not implemented in the Collection class

### 🚧 Not Yet Implemented
- **Collection Creation**: Creating new collections with custom schemas
- **Collection Updates**: Modifying existing collection structures  
- **Collection Deletion**: Removing collections
- **Field Management**: Managing collection fields and relationships
- **Database Views**: Querying and managing database views
- **Collection Categories**: Managing collection categories

## API Reference

### NocoBaseRequestsClient
Main client class for interacting with NocoBase API.

```python
client = NocoBaseRequestsClient(auth_token, base_uri)
```

**Methods:**
- `collections()` → Returns Collections manager
- `collection(name: str)` → Returns specific Collection instance
- `list_collections()` → Returns raw collection data

### Collection
Represents a single NocoBase collection with full CRUD operations.

**Query Methods:**
- `list(**params)` → Generator yielding all rows with automatic pagination
- `get(id=None, filter=None, **params)` → Single row retrieval

**Mutation Methods:**
- `create(body, whitelist=[], blacklist=[])` → Create new row
- `update(body, id=None, filter=None, whitelist=[], blacklist=[])` → Update existing row

**Parameters:**
- `page`, `page_size`: Pagination control
- `filter`: Dictionary for filtering results
- `sort`: List of field names (prefix with `-` for descending)
- `fields`: List of fields to include in response
- `appends`: List of related fields to include
- `excepts`: List of fields to exclude from response
- `whitelist`: Only save these fields (create/update)
- `blacklist`: Ignore these fields (create/update)

## Author notes

I created this package to bootstrap some personal collections and I hope it
will help other developers from the python community. It provides a solid
foundation for NocoBase API integration with full CRUD operations and advanced
querying capabilities.

The library is actively maintained and contributions are welcome. Feel free to
add new capabilities by creating a new MR.

## Contributors

![Contributors image](https://contrib.rocks/image?repo=ueki-kazuki/python-nocobase)

- Kazuki UEKI @ueki-kazuki
- and ALL python-nocodb committers
