Missing expected field error

```json
{
  "cadences": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "reference_id",
            "json_path": "$.cadences[0].follow_ups[1].parent_follow_up.reference_id"
          },
          {
            "api_name": "id",
            "json_path": "$.cadences[0].follow_ups[1].parent_follow_up.id"
          }
        ]
      },
      "message": "Specify atleast one field",
      "status": "error"
    }
  ]
}
```
