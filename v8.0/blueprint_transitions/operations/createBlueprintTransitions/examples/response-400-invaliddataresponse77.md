Error response with code **INVALID_DATA**: invalid data (field **id**)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria.field.id"
      },
      "status": "error"
    }
  ]
}
```
