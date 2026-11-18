Error response with **INVALID_DATA**: invalid data type in **api_name**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```
