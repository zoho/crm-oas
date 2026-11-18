**INVALID_DATA** error response: invalid data type in the **criteria** field

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "criteria",
        "expected_data_type": "jsonobject",
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria"
      },
      "status": "error"
    }
  ]
}
```
