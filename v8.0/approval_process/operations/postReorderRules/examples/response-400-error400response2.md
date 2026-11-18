Duplicate sequence number across two rules

```json
{
  "reorder": {
    "code": "ALREADY_EXISTS",
    "details": {
      "api_name": "sequence_number",
      "json_path": "$.reorder.rules[0].sequence_number",
      "exists_in": {
        "api_name": "sequence_number",
        "json_path": "$.reorder.rules[1].sequence_number"
      }
    },
    "message": "duplicate sequence number",
    "status": "error"
  }
}
```
