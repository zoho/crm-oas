# Examples: getAssociatedGroupsForUser

**GET /users/{user}/actions/associated_groups**

## Response examples

### Status `200` — `application/json` — Success

Successful response with associated user groups

```json
{
  "user_groups": [
    {
      "created_time": "2022-11-21T12:33:12+05:30",
      "modified_time": "2022-11-21T13:21:46+05:30",
      "name": "group 1",
      "modified_by": {
        "name": "Patricia Boyle",
        "id": "3652397000000186017"
      },
      "description": "groups API",
      "id": "3652397000009949005",
      "created_by": {
        "name": "Patricia Boyle",
        "id": "3652397000000186017"
      }
    }
  ],
  "info": {
    "per_page": 200,
    "count": 1,
    "page": 1,
    "more_records": false
  }
}
```

### Status `400` — `application/json` — InvalidData

Invalid user ID in request URL

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

### Status `404` — `application/json` — InvalidData

Invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "The provided group ID is invalid.",
  "status": "error"
}
```
