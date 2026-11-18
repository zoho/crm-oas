Error response **INVALID_DATA**: invalid data in field **api_name**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 200,
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria.field.api_name"
      },
      "status": "error"
    }
  ]
}
```
