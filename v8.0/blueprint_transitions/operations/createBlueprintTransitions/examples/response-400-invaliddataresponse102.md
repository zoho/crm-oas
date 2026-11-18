Error response with code **INVALID_DATA** for an invalid data type in **title**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "title",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].title"
      },
      "status": "error"
    }
  ]
}
```
