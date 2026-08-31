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
