Error response when the **criteria** field has an invalid data type

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "criteria",
        "expected_data_type": "jsonobject",
        "json_path": "$.transitions[*].during_inputs[*].validation_filter.criteria"
      },
      "status": "error"
    }
  ]
}
```
