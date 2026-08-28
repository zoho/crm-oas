# Examples: updateCallPreferences

**PUT /settings/call_preferences**

## Request examples

### `application/json` — RequestBody

Enable both From Number and To Number on Call records

```json
{
  "call_preferences": {
    "show_from_number": true,
    "show_to_number": true
  }
}
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

Call Preferences updated successfully

```json
{
  "call_preferences": {
    "code": "SUCCESS",
    "details": {},
    "message": "calls preferences updated successfully",
    "status": "success"
  }
}
```

### Status `400` — `application/json` — InvalidData

Preference value is not a Boolean

```json
{
  "call_preferences": {
    "code": "INVALID_DATA",
    "status": "error",
    "message": "Invalid data",
    "details": {
      "expected_data_type": "boolean",
      "api_name": "show_from_number",
      "json_path": "$.preferences.show_from_number"
    }
  }
}
```
