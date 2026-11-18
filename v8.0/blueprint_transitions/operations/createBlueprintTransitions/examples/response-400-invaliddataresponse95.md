Error response with code **INVALID_DATA**: invalid data in field **api_name**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 5,
        "json_path": "$.transitions[*].during_inputs[*].related_list.module.api_name"
      },
      "status": "error"
    }
  ]
}
```
