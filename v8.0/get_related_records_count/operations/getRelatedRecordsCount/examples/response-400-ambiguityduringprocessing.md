ID and API name mismatch

```json
{
  "get_related_records_count": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.get_related_records_count[0].related_list.id"
          },
          {
            "api_name": "api_name",
            "json_path": "$.get_related_records_count[0].related_list.api_name"
          }
        ]
      },
      "message": "Ambiguity while processing the request",
      "status": "error"
    }
  ]
}
```
