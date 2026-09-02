Holiday date outside allowed range in bulk update

```json
{
  "holidays": [
    {
      "code": "INVALID_DATA",
      "details": {
        "api_name": "date",
        "json_path": "$.holidays[0].date"
      },
      "message": "Date Should be between current and next financial year",
      "status": "error"
    }
  ]
}
```
