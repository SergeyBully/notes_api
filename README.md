# notes_api
API for creating simple notes

Server - localhost
#### Version: 1.0.0

## /notes
### GET
**Description:**
Returns all notes

**Parameters**

No parameters

**Responses**
```commandline
[
    {
        "content": "This is my first note!",
        "id": 1,
        "title": "first note",
        "type_id": 2,
        "update_date": 1730747109
    },
    {
        "content": "This is my second note!",
        "id": 2,
        "title": "second note",
        "type_id": 4,
        "update_date": 1730747383
    }
]
```

| Code | Description |
| ---- |-------------|
| 200 | All notes   |

## /note/{note_id}
### GET
**Description:**
Returns specific notes

**Parameters**

No parameters

**Responses**
```commandline
{
    "content": "This is my second note!",
    "id": 2,
    "title": "second note",
    "type_id": 4,
    "update_date": 1730747200
}
```

| Code | Description   |
| ---- |---------------|
| 200 | Specific note |

## /notes
### POST
**Description:**
Create new note

**Parameters**

```commandline
{
    "title": "third note",
    "content": "This is my third note!",
    "type_name": "genral"
}
```
| Name | Located in | Description                       | Required | Schema |
| ---- | ---------- |-----------------------------------| -------- | ---- |
| title | path |                                   | Yes | string |
| content | path |                                   | Yes | string |
| type_name | path | type should be presented in types | Yes | string |
> [!NOTE]
> If you get an error "Such type name does not exist!" use POST /types to add your new type

**Responses**
```commandline
{
    "content": "This is my third note!",
    "id": 4,
    "title": "third note",
    "type_id": 2,
    "update_date": 1730753075
}
```

| Code | Description |
|------|-------------|
| 201  | Response    |

## /notes/{note_id}
### PUT
**Description:**
Update existing note

**Parameters**

```commandline
{
    "title": "Updated note",
    "content": "This is my updated note!",
    "type_name": "genral"
}
```
| Name | Located in | Description                       | Required | Schema |
| ---- | ---------- |-----------------------------------|----------| ---- |
| title | path |                                   | No       | string |
| content | path |                                   | No       | string |
| type_name | path | type should be presented in types | No       | string |
> [!NOTE]
> If you get an error "Such type name does not exist!" use POST /types to add your new type 

**Responses**
```commandline
{
    "content": "This is my updated note!",
    "id": 2,
    "title": "Updated note",
    "type_id": 2,
    "update_date": 1730753646
}
```

| Code | Description |
|------|-------------|
| 201  | Response    |

## /notes/{note_id}
### DELETE
**Description:**
Delete specific note

**Parameters**

No parameters

**Responses**
```commandline
{
    "message": "Note deleted successfully"
}
```

| Code | Description |
| ---- |-------------|
| 200 | Response    |

## /types
### GET
**Description:**
Returns all notes

**Parameters**

No parameters

**Responses**
```commandline
[
    {
        "id": 1,
        "type_name": "general"
    },
    {
        "id": 2,
        "type_name": "shopping list"
    }
]
```

| Code | Description |
| ---- |-------------|
| 200 | All types   |

## /types
### POST
**Description:**
Create new type

**Parameters**

```commandline
{
    "type_name": "new type"
}
```
| Name | Located in | Description                       | Required | Schema |
| ---- | ---------- |-----------------------------------| -------- | ---- |
| type_name | path |                                   | Yes | string |
> [!NOTE]
> type_name should be unique

**Responses**
```commandline
{
    "type_name": "new type"
}
```

| Code | Description |
|------|-------------|
| 200  | Response    |

## /types/{type_id}
### POST
**Description:**
Update existing type

**Parameters**

```commandline
{
    "type_name": "new type updated"
}
```
| Name | Located in | Description                       | Required | Schema |
| ---- | ---------- |-----------------------------------| -------- | ---- |
| type_name | path |                                   | Yes | string |
> [!NOTE]
> type_name should be unique

**Responses**
```commandline
{
    "type_name": "new type updated"
}
```

| Code | Description |
|------|-------------|
| 200  | Response    |

## /delete/{type_id}
### DELETE
**Description:**
Delete specific type

**Parameters**

No parameters

**Responses**
```commandline
{
    "message": "Type deleted successfully"
}
```

| Code | Description |
| ---- |-------------|
| 200 | Response    |


## /update_history/{note_id}
### GET
**Description:**
Returns histroty of updates for specific note_id

**Parameters**

No parameters

**Responses**
```commandline
[
    {
        "content": "This is my second note!323",
        "note_id": 2,
        "title": "second note",
        "type_id": 2,
        "update_date": 1730747137,
        "update_id": 1
    },
    {
        "content": "This is my second note! updated",
        "note_id": 2,
        "title": "second note",
        "type_id": 4,
        "update_date": 1730747200,
        "update_id": 2
    }
]
```

| Code | Description                   |
| ---- |-------------------------------|
| 200 | All updates for specific note |

# Database
[How to create database in AWS RDS](https://aws.amazon.com/getting-started/hands-on/create-microsoft-sql-db/)

To connect to your database create ```.env``` file in main directory with the following:
```commandline
SQL_SERVER=<Endpoint>
SQL_DATABASE=<Database name>
SQL_USERNAME=<Username>
SQL_PASSWORD=<Password>
```
### Database schema
![DB.png](..%2FDB.png)