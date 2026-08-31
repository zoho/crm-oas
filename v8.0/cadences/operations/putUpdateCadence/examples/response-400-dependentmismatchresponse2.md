Inconsistent dependent field values error

```json
{
  "cadences": [
    {
      "code": "DEPENDENT_MISMATCH",
      "details": {
        "dependee": {
          "api_name": "reference_id",
          "json_path": "$.cadences[0].follow_ups[1].parent_follow_up.reference_id"
        },
        "api_name": "triggers",
        "json_path": "$.cadences[0].follow_ups[1].triggers[0]",
        "supported_values": []
      },
      "message": "dependent mismatch",
      "status": "error"
    }
  ]
}
```
