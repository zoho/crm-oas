Partial batch - one success, one invalid profile error

```json
{
  "modules": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "111111000000263276"
      },
      "message": "module updated successfully",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.modules[1].profiles[0].id"
      },
      "message": "Invalid profile id passed",
      "status": "error"
    }
  ]
}
```
