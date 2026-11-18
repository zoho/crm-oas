Error response when the **field** value has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.criteria.field"
      },
      "status": "error"
    }
  ]
}
```
