Holiday name contains invalid special characters in bulk update

```json
{
  "holidays": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "name",
        "json_path": "$.holidays[0].name"
      },
      "message": "Holiday Name should not contain special characters:#, %, ^, &, *",
      "status": "error"
    }
  ]
}
```
