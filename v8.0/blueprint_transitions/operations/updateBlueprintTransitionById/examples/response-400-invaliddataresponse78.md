Invalid data type in the **comparator** field of the transition criteria

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "comparator",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria.comparator"
      },
      "status": "error"
    }
  ]
}
```
