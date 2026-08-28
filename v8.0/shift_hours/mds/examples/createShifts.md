# Examples: createShifts

**POST /settings/business_hours/shift_hours**

## Request examples

### `application/json` — Default

An example of create shift hour request.

```json
{
  "shift_hours": [
    {
      "name": "New Shift",
      "timezone": "Asia/Kolkata",
      "same_as_everyday": true,
      "daily_timing": [
        "09:00",
        "18:00"
      ],
      "shift_days": [
        "Monday",
        "Tuesday"
      ],
      "users": [],
      "break_hours": [],
      "holidays": []
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Default

An example success response.

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

### Status `207` — `application/json` — Default

An example multi-status response.

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

An example error response.

```json
{
  "shift_hours": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.shift_hours[0].name"
      },
      "message": "Shift Name already exists",
      "status": "error"
    }
  ]
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
