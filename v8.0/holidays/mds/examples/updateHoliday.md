# Examples: updateHoliday

**PUT /settings/holidays/{holidayId}**

## Parameter examples

### `holidayId` (path) — Default

Example holiday ID

```json
"5725767000000525001"
```

## Request examples

### `application/json` — Default

Default success response after updating a holiday

```json
{}
```

## Response examples

### Status `200` — `application/json` — Default

Default 400 error response for holiday update

```json
{
  "holidays": []
}
```

### Status `400` — `application/json` — DuplicateData

Duplicate holiday name

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
