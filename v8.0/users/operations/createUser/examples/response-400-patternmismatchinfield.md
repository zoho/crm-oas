Shows the error returned when the value provided for a field does not match the expected format or pattern, such as for the time format, distance preference, or status fields.

```json
{
  "users": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "time_format",
        "json_path": "$.users[0].time_format"
      },
      "message": "Pattern not matched",
      "status": "error"
    }
  ],
  "summary": "Field value does not match the expected pattern"
}
```
