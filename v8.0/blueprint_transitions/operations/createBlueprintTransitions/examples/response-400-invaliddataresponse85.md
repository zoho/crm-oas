Error response with code **INVALID_DATA**: the **related_list** field exceeds the maximum length of 1

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "related_list",
        "maximum_length": 1,
        "json_path": "$.transitions[*].during_inputs[*].related_list"
      },
      "status": "error"
    }
  ]
}
```
