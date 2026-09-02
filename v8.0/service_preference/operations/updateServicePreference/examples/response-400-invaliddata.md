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
