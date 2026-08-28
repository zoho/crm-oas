# Examples: createBusinessHours

**POST /settings/business_hours**

## Request examples

### `application/json` — CustomHours

Custom Business Hours

```json
{
  "business_hours": {
    "week_starts_on": "Monday",
    "type": "custom",
    "business_days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday"
    ],
    "same_as_everyday": false,
    "daily_timing": [
      "09:00",
      "18:00"
    ],
    "custom_timing": [
      {
        "days": "Monday",
        "business_timing": [
          "09:00",
          "18:00"
        ]
      }
    ]
  }
}
```

## Response examples

### Status `201` — `application/json` — Success

Success Response

```json
{
  "business_hours": {
    "status": "success",
    "code": "SUCCESS",
    "message": "Business Hours saved successfully",
    "details": {
      "id": "1234567890"
    }
  }
}
```

### Status `400` — `application/json` — MultipleBusinessHours

Multiple Business Hours Error

```json
{
  "code": "NOT_ALLOWED",
  "details": {},
  "message": "Organization can have only one Business Hour",
  "status": "error"
}
```

### Status `403` — `application/json` — Forbidden

Forbidden Error

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Users"
    ]
  },
  "message": "Forbidden due to insufficient permissions",
  "status": "error"
}
```
