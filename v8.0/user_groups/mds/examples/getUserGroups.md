# Examples: getUserGroups

**GET /settings/user_groups**

## Response examples

### Status `200` — `application/json` — Success

Successful response with user groups

```json
{
  "user_groups": [
    {
      "created_time": "2022-11-21T12:33:12+05:30",
      "sources_count": {
        "territories": 1,
        "roles": 2,
        "users": 2,
        "groups": 1
      },
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
    },
    {
      "created_time": "2023-12-01T10:00:00Z",
      "sources_count": {
        "roles": 2
      },
      "modified_time": null,
      "name": "group test",
      "modified_by": null,
      "description": null,
      "id": "3652397000009952001",
      "created_by": {
        "name": "Patricia Boyle",
        "id": "3652397000000186017"
      }
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

### Status `400` — `application/json` — NoPermission

Invalid filters parameter

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "filters"
  },
  "message": "The given filters is not a valid json",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermission

User does not have permission to access groups

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": "Crm_Implied_Manage_Groups"
  },
  "message": "You do not have permission to access user groups",
  "status": "error"
}
```
