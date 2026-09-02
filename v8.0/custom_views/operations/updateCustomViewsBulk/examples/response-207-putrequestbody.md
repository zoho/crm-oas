Bulk update partial success response

```json
{
  "custom_views": [
    {
      "code": "SUCCESS",
      "details": {
        "id": "2411194000004076067"
      },
      "message": "custom view updated",
      "status": "success"
    },
    {
      "code": "DUPLICATE_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.custom_views[0].name"
      },
      "message": "duplicate data",
      "status": "error"
    }
  ]
}
```
