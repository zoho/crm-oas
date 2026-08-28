# Examples: getDeletedRecords

**GET /{module}/deleted**

## Parameter examples

### `module` (path) — Example

```json
"Leads"
```

### `If-Modified-Since` (header) — Example

```json
"2019-07-25T15:26:49+05:30"
```

## Response examples

### Status `200` — `application/json` — DeletedRecords

List of deleted records with metadata

```json
{
  "data": [
    {
      "deleted_by": {
        "name": "Patricia Boyle",
        "id": "410888000000086001"
      },
      "id": "410888000000099071",
      "display_name": "Patricia",
      "type": "recycle",
      "created_by": {
        "name": "Patricia Boyle",
        "id": "410888000000086001"
      },
      "deleted_time": "2015-06-19T11:19:38+05:30"
    },
    {
      "deleted_by": {
        "name": "Patricia Boyle",
        "id": "410888000000086001"
      },
      "id": "410888000000094004",
      "display_name": "Patricia",
      "type": "recycle",
      "created_by": {
        "name": "Patricia Boyle",
        "id": "410888000000086001"
      },
      "deleted_time": "2015-04-07T17:43:33+05:30"
    },
    {
      "deleted_by": null,
      "id": "410888000000680013",
      "display_name": null,
      "type": "permanent",
      "created_by": null,
      "deleted_time": "2016-10-26T11:44:15+05:30"
    },
    {
      "deleted_by": null,
      "id": "410888000000680009",
      "display_name": null,
      "type": "permanent",
      "created_by": null,
      "deleted_time": "2016-10-26T11:44:15+05:30"
    }
  ],
  "info": {
    "per_page": 200,
    "count": 4,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — InvalidModule

Invalid module API name in the request

```json
{
  "data": [
    {
      "code": "INVALID_MODULE",
      "message": "the module name given seems to be invalid",
      "status": "error",
      "details": {
        "resource_path_index": 0
      }
    }
  ]
}
```

### Status `400` — `application/json` — PatternNotMatched

Value does not match the expected pattern

```json
{
  "data": [
    {
      "code": "PATTERN_NOT_MATCHED",
      "details": {
        "param_name": "type"
      },
      "message": "Please check whether the input values are correct",
      "status": "error"
    }
  ]
}
```

### Status `401` — `application/json` — ScopeMismatch

OAuth access token missing the required scope

```json
{
  "code": "OAUTH_SCOPE_MISMATCH",
  "message": "Unauthorized",
  "status": "error",
  "details": {}
}
```

### Status `403` — `application/json` — NoPermission

User profile lacks the required module permission

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "status": "error",
  "details": {
    "permissions": [
      "Crm_Implied_View_Leads"
    ]
  }
}
```

### Status `500` — `application/json` — InternalError

Unexpected internal server error during processing

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "status": "error",
  "details": {}
}
```
