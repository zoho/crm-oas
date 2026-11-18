Error response **INVALID_DATA**: invalid data type in **field**

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "field",
        "expected_data_type": "jsonobject",
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].field"
      },
      "status": "error"
    }
  ]
}
```
