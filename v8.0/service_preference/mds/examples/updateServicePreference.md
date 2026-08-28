# Examples: updateServicePreference

**PUT /settings/service_preferences**

## Request examples

### `application/json` — ExpectedRequest

An example request to update service preferences.

```json
{
  "service_preferences": {
    "job_sheet_enabled": true
  }
}
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

An example successful response for updating service preferences.

```json
{
  "service_preferences": {
    "code": "SUCCESS",
    "details": {},
    "message": "Services preferences updated successfully",
    "status": "success"
  }
}
```

### Status `400` — `application/json` — MandatoryNotFound

An example error response when the service_preferences key is missing.

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "service_preferences",
    "json_path": "$.service_preferences"
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidData

An example error response when job_sheet_enabled has an invalid data type.

```json
{
  "service_preferences": {
    "code": "INVALID_DATA",
    "details": {
      "expected_data_type": "boolean",
      "api_name": "job_sheet_enabled",
      "json_path": "$.service_preferences.job_sheet_enabled"
    },
    "message": "invalid data",
    "status": "error"
  }
}
```
