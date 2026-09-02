Error response with code EXPECTED_FIELD_MISSING: specify atleast one field

```json
{
  "replace_pick_list_values": [
    {
      "code": "EXPECTED_FIELD_MISSING",
      "details": {
        "expected_fields": [
          {
            "api_name": "id",
            "json_path": "$.replace_pick_list_values[0].old_value.id"
          },
          {
            "api_name": "display_value",
            "json_path": "$.replace_pick_list_values[0].old_value.display_value"
          }
        ]
      },
      "message": "specify atleast one field",
      "status": "error"
    }
  ]
}
```
