# Examples: createHolidays

**POST /settings/holidays**

## Request examples

### `application/json` — Default

Default success response after creating holidays

```json
{
  "holidays": [
    {
      "name": "New Year",
      "date": "2025-01-01",
      "type": "business_holiday"
    }
  ]
}
```

## Response examples

### Status `201` — `application/json` — Default

Default 400 error response for holiday creation

```json
{
  "holidays": []
}
```

### Status `207` — `application/json` — Default

An example multi-status response.

```json
{
  "holidays": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "12345"
      },
      "message": "Holiday created successfully",
      "status": "success"
    }
  ]
}
```

### Status `400` — `application/json` — MissingDate

Missing required date field

```json
{
  "holidays": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "date",
        "json_path": "$.holidays[0].date"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MissingType

Missing required type field

```json
{
  "holidays": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "type",
        "json_path": "$.holidays[0].type"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — MissingName

Missing required name field

```json
{
  "holidays": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "details": {
        "api_name": "name",
        "json_path": "$.holidays[0].name"
      },
      "message": "required field not found",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — LimitExceeded

Holiday limit exceeded for the specified type

```json
{
  "holidays": [
    {
      "code": "LIMIT_EXCEEDED",
      "details": {
        "limit": 52,
        "limit_due_to": [
          {
            "api_name": "type",
            "json_path": "$.holidays[0].type"
          }
        ]
      },
      "message": "Holidays limit exceeds",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DuplicateData

Duplicate holiday name and date combination

```json
{
  "holidays": [
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.holidays[0].name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — DependentFieldMissing

Missing dependent field for shift holiday

```json
{
  "holidays": [
    {
      "code": "DEPENDENT_FIELD_MISSING",
      "details": {
        "dependee": {
          "api_name": "type",
          "json_path": "$.holidays[0].type"
        },
        "api_name": "shift_hour",
        "json_path": "$.holidays[0].shift_hour"
      },
      "message": "Shift id is required for shift holidays",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataMaxLength

Holiday name exceeds maximum length

```json
{
  "holidays": [
    {
      "code": "INVALID_DATA",
      "details": {
        "maximum_length": 80,
        "api_name": "name",
        "json_path": "$.holidays[0].name"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataDateRange

Holiday date outside allowed range

```json
{
  "holidays": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "date",
        "json_path": "$.holidays[0].date"
      },
      "message": "Date Should be between current and next financial year",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataShiftId

Invalid shift hour ID value

```json
{
  "holidays": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.holidays[0].shift_hour.id"
      },
      "message": "Invalid shift id",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataSpecialChars

Holiday name contains invalid special characters

```json
{
  "holidays": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.holidays[0].name"
      },
      "message": "Holiday Name should not contain special characters:#, %, ^, &, *",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataType

Invalid holiday type value

```json
{
  "holidays": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "type",
        "json_path": "$.holidays[0].type",
        "supported_values": [
          "business_holiday",
          "shift_holiday"
        ]
      },
      "message": "Invalid type",
      "status": "error"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataDateFormat

Holiday date in invalid format

```json
{
  "holidays": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "date",
        "api_name": "date",
        "json_path": "$.holidays[0].date"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```

### Status `403` — `application/json` — NoPermission

No permission to access holiday data

```json
{
  "code": "NO_PERMISSION",
  "details": {},
  "message": "Permission to read holiday data is required",
  "status": "error"
}
```
