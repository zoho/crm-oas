Example of an error when a field receives a value of the wrong data type.

```json
{
  "appointment_preferences": {
    "status": "error",
    "code": "INVALID_DATA",
    "details": {
      "expected_data_type": "boolean",
      "api_name": "show_job_sheet",
      "json_path": "$.appointment_preferences.show_job_sheet"
    },
    "message": "invalid data"
  }
}
```
