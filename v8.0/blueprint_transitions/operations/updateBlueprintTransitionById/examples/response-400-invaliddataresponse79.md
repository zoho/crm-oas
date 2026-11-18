Invalid data in the **comparator** field of the transition criteria

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "comparator",
        "maximum_length": 12,
        "json_path": "$.transitions[*].during_inputs[*].configured_fields[*].criteria.comparator"
      },
      "status": "error"
    }
  ]
}
```
