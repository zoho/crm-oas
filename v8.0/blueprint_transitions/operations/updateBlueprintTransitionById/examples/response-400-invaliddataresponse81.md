Invalid data in the **value** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "value",
        "maximum_length": 4,
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria.value"
      },
      "status": "error"
    }
  ]
}
```
