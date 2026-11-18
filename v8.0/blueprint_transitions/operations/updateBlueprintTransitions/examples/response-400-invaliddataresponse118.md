Error response with code INVALID_DATA: Invalid data type (Field: name)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "name",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].kiosk.name"
      },
      "status": "error"
    }
  ]
}
```
