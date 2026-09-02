Ambiguity when `id` and `api_name` refer to different fields

```json
{
  "record_locking_configurations": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "json_path": "$.record_locking_configurations[0].excluded_fields[0].api_name",
            "api_name": "api_name"
          },
          {
            "json_path": "$.record_locking_configurations[0].excluded_fields[0].id",
            "api_name": "id"
          }
        ]
      },
      "message": "Field Id and apiname are ambiguous",
      "status": "error"
    }
  ]
}
```
