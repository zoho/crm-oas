# Examples: updateBusinessHours

**PUT /settings/business_hours**

## Request examples

### `application/json` — UpdateCustomHours

Update to Custom Business Hours

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

### `application/json` — DeleteCustomTiming

Delete Custom Timing for a Specific Day

```json
{
  "business_hours": {
    "week_starts_on": "Monday",
    "type": "custom",
    "business_days": [
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday"
    ],
    "same_as_everyday": false,
    "custom_timing": [
      {
        "days": "Monday",
        "business_timing": [
          "10:00",
          "17:00"
        ]
      },
      {
        "days": "Tuesday",
        "business_timing": [
          "10:30",
          "17:00"
        ]
      },
      {
        "days": "Wednesday",
        "business_timing": [
          "11:00",
          "17:00"
        ]
      },
      {
        "days": "Thursday",
        "business_timing": [
          "09:00",
          "18:30"
        ]
      },
      {
        "days": "Friday",
        "business_timing": [
          "11:30",
          "18:30"
        ],
        "_delete": true
      }
    ]
  }
}
```

## Response examples

### Status `200` — `application/json` — Success

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

### Status `400` — `application/json` — UpdateRestrictions

Update Restrictions Error

```json
{
  "business_hours": {
    "code": "NOT_ALLOWED",
    "details": {},
    "message": "Cannot update business hours",
    "status": "error"
  }
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
