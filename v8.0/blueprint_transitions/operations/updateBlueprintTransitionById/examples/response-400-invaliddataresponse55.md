Invalid value for the api_name field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 200,
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.criteria.field.api_name"
      },
      "status": "error"
    }
  ]
}
```
