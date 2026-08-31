Error response with code AMBIGUITY_DURING_PROCESSING: ambiguity while processing the new_value

```json
{
  "replace_pick_list_values": [
    {
      "code": "AMBIGUITY_DURING_PROCESSING",
      "details": {
        "ambiguity_due_to": [
          {
            "api_name": "id",
            "json_path": "$.replace_pick_list_values[0].new_value.id"
          },
          {
            "api_name": "display_value",
            "json_path": "$.replace_pick_list_values[0].new_value.display_value"
          }
        ]
      },
      "message": "ambiguity while processing the new_value",
      "status": "error"
    }
  ]
}
```
