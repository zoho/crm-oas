Invalid data error when a Members entry is an inactive user

```json
{
  "data": [
    {
      "code": "INVALID_DATA",
      "details": {
        "user_status": "inactive",
        "api_name": "id",
        "json_path": "$.data[0].Members[0].Members.id"
      },
      "message": "Members is not Active",
      "status": "error"
    }
  ]
}
```
