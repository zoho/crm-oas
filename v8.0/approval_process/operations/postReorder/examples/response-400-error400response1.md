Duplicate sequence number error

```json
{
  "reorder": {
    "code": "ALREADY_EXISTS",
    "details": {
      "api_name": "sequence_number",
      "json_path": "$.reorder.approval_process[0].sequence_number",
      "exists_in": {
        "api_name": "sequence_number",
        "json_path": "$.reorder.approval_process[1].sequence_number"
      }
    },
    "message": "duplicate sequence number",
    "status": "error"
  }
}
```
