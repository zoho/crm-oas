Error response with **INVALID_DATA**: invalid data type in **message**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "message",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].message"
      },
      "status": "error"
    }
  ]
}
```
