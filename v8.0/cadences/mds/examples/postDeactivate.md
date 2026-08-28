# Examples: postDeactivate

**POST /settings/automation/cadences/{id}/actions/deactivate**

## Response examples

### Status `200` — `application/json` — Success200

Successful Cadence deactivation response

```json
{
  "cadences": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111112000000092007"
      },
      "message": "Cadences deactivated successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Invalid Cadence ID error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the given id seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — AlreadyDeactivatedResponse1

Cadence already deactivated error

```json
{
  "code": "ALREADY_DEACTIVATED",
  "details": {},
  "message": "The cadences is already deactivated",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission to deactivate Cadence error

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Cadences"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```
