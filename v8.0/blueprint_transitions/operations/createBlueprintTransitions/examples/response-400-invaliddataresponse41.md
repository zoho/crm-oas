Error response with **INVALID_DATA**: invalid data in **api_name**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 12,
        "json_path": "$.transitions[*].during_inputs[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```
