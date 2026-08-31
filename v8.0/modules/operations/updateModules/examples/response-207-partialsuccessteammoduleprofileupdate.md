Partial success - profile update not allowed for team module

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
      "code": "NOT_ALLOWED",
      "details": {
        "api_name": "profiles",
        "json_path": "$.modules[1].profiles"
      },
      "message": "profile update for team module is not allowed",
      "status": "error"
    }
  ]
}
```
