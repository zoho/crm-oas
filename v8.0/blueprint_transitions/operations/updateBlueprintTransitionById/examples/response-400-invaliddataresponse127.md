Invalid data type for the **api_name** field (error code **INVALID_DATA**)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "api_name",
        "expected_data_type": "text",
        "json_path": "$.transitions[*].actions[*].details.module.api_name"
      },
      "status": "error"
    }
  ]
}
```
