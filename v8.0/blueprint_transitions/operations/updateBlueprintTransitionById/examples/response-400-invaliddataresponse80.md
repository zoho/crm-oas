Invalid data type in the **value** field of the transition criteria

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "value",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria.value"
      },
      "status": "error"
    }
  ]
}
```
