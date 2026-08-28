# Examples: getVariableGroupById

**GET /settings/variable_groups/{id}**

## Response examples

### Status `200` — `application/json` — Success200

Successful get variable group by ID response

```json
{
  "variable_groups": [
    {
      "display_label": "General",
      "api_name": "General",
      "name": "General",
      "description": null,
      "id": "111111000000117077",
      "source": "crm"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Error response for invalid variable group ID

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "Invalid ID",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response for insufficient permissions

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Variables_Access"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
