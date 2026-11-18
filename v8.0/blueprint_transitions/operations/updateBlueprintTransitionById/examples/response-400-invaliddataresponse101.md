Error response with code INVALID_DATA: Invalid data (Field: api_name)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 8,
        "json_path": "$.transitions[*].during_inputs[*].related_list.layout.api_name"
      },
      "status": "error"
    }
  ]
}
```
