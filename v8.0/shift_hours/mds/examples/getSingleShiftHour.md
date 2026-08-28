# Examples: getSingleShiftHour

**GET /settings/business_hours/shift_hours/{shift}**

## Parameter examples

### `shift` (path) — Default

Example shift hour ID

```json
"5725767000000296005"
```

## Response examples

### Status `200` — `application/json` — Default

An example of successful shift hour response.

```json
{
  "shift_hours": [
    {
      "timezone": "Asia/Kolkata",
      "name": "General Shift",
      "same_as_everyday": true,
      "users_count": 0,
      "shift_days": [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
      ],
      "daily_timing": [
        "09:00",
        "18:00"
      ],
      "custom_timing": [],
      "break_hours": [],
      "holidays": [],
      "users": [],
      "id": "1234567890"
    }
  ],
  "shift_count": {
    "total_shift_with_user": 0
  }
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
