Missing ID or API name

```json
{
  "get_related_records_count": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "api_name",
            "json_path": "$.get_related_records_count[0].related_list.api_name"
          },
          {
            "api_name": "id",
            "json_path": "$.get_related_records_count[0].related_list.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
