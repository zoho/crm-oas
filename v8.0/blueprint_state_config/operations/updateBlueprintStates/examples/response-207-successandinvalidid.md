Mixed Response With One Success and One Invalid ID Error

```json
{
  "states": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.states[0].id"
      },
      "message": "the value given is invalid",
      "status": "error"
    },
    {
      "code": "SUCCESS",
      "details": {
        "id": "1234567890"
      },
      "message": "State updated successfully",
      "status": "success"
    }
  ]
}
```
