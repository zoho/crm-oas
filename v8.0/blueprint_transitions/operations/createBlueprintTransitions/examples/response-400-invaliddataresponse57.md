Error response with code **INVALID_DATA**: Invalid data (Field: **id**)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "id",
        "maximum_length": 25,
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.criteria.field.id"
      },
      "status": "error"
    }
  ]
}
```
