# Examples: getUserGroupSources

**GET /settings/user_groups/{group}/sources**

## Response examples

### Status `200` — `application/json` — Success

Successful response with member sources

```json
{
  "sources": [
    {
      "source": {
        "name": "Patricia Boyle",
        "id": "3652397000000186017"
      },
      "type": "users"
    },
    {
      "source": {
        "name": "Sales Manager",
        "id": "3652397000000026008"
      },
      "type": "roles",
      "subordinates": false
    },
    {
      "source": {
        "name": "APAC Region",
        "id": "3652397000000095001"
      },
      "type": "roles",
      "sub_territories": true
    }
  ],
  "info": {
    "per_page": 200,
    "count": 2,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — InvalidData

Invalid group ID in request URL

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "The provided group ID is invalid.",
  "status": "error"
}
```

### Status `400` — `application/json` — PatternNotMatched

Query parameter value does not match required pattern

```json
{
  "code": "PATTERN_NOT_MATCHED",
  "details": {
    "regex": "users|roles|groups|territories",
    "param_name": "type"
  },
  "message": "invalid data",
  "status": "error"
}
```
