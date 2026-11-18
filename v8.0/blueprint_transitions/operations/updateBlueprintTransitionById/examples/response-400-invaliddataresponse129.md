Invalid data type for the **tags** field (error code **INVALID_DATA**)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "tags",
        "expected_data_type": "jsonarray",
        "json_path": "$.transitions[*].actions[*].details.tags"
      },
      "status": "error"
    }
  ]
}
```
