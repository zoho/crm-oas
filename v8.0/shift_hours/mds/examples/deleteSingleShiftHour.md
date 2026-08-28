# Examples: deleteSingleShiftHour

**DELETE /settings/business_hours/shift_hours/{shift}**

## Parameter examples

### `shift` (path) — Default

Example shift hour ID

```json
"5725767000000296005"
```

## Response examples

### Status `200` — `application/json` — Default

Delete shift hour response example

```json
{
  "shift_hours": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "12345"
      },
      "message": "Success",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — Default

An example of an error response.

```json
{
  "code": "INVALID_DATA",
  "message": "Invalid ID",
  "status": "error",
  "details": {}
}
```

### Status `403` — `application/json` — Default

An example of error response where the user does not have enough permission to perform this request.

```json
{
  "code": "NO_PERMISSION",
  "message": "Permission denied",
  "status": "error",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Users"
    ]
  }
}
```
