Invalid data in the **api_name** field (**INVALID_DATA**)

```json
{
  "transitions": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "api_name",
        "maximum_length": 100,
        "json_path": "$.transitions[*].module.api_name"
      },
      "status": "error"
    }
  ]
}
```
