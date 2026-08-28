# Examples: updateHolidays

**PUT /settings/holidays**

## Request examples

### `application/json` — Default

Default request body for bulk holiday update

```json
{
  "holidays": [
    {
      "id": "4150868000011382033",
      "name": "New Year Updated"
    }
  ]
}
```

## Response examples

### Status `200` — `application/json` — Default

Default success response after updating holidays

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

### Status `400` — `application/json` — DuplicateData

Duplicate holiday name in bulk update

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

Missing dependent field for shift holiday in bulk update

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

Holiday name exceeds maximum length in bulk update

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

Holiday date outside allowed range in bulk update

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

Invalid shift hour ID in bulk update

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

Holiday name contains invalid special characters in bulk update

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

Invalid holiday type value in bulk update

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

Holiday date in invalid format in bulk update

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

### Status `400` — `application/json` — InvalidHolidayId

Invalid holiday ID in bulk update

```json
{
  "holidays": [
    {
      "code": "INVALID_DATA",
      "details": {
        "expected_data_type": "long",
        "api_name": "id",
        "json_path": "$.holidays[0].id"
      },
      "message": "Invalid holiday id",
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
