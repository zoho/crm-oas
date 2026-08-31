Partial success and failure response

```json
{
  "custom_views": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "2411194000003890058"
      },
      "message": "custom view updated",
      "status": "success"
    },
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "id",
        "json_path": "$.custom_views[1].id"
      },
      "message": "invalid data",
      "status": "error"
    }
  ]
}
```
