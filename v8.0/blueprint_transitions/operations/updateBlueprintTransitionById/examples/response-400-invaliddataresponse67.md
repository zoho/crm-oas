Invalid data in the **api_name** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 7,
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].field.api_name"
      },
      "status": "error"
    }
  ]
}
```
