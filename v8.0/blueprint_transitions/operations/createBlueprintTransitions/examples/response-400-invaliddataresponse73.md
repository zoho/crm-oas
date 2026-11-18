Error response **INVALID_DATA**: invalid data in field **field**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "field",
        "maximum_length": 1,
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria.field"
      },
      "status": "error"
    }
  ]
}
```
