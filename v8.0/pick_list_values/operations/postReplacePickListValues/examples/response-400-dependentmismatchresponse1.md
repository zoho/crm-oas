Error response with code DEPENDENT_MISMATCH: old_value and new_value should not be the same (Field: new_value)

```json
{
  "replace_pick_list_values": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "old_value",
          "json_path": "$.replace_pick_list_values[0].old_value"
        },
        "api_name": "new_value",
        "json_path": "$.replace_pick_list_values[0].new_value"
      },
      "message": "old_value and new_value should not be the same",
      "status": "error"
    }
  ]
}
```
