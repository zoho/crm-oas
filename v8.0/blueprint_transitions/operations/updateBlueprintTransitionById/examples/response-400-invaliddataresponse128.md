Invalid data in the **api_name** field (error code **INVALID_DATA**)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 8,
        "json_path": "$.transitions[*].actions[*].details.module.api_name"
      },
      "status": "error"
    }
  ]
}
```
