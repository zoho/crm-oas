INVALID_DATA error for an invalid data type on the sequence_number field

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "sequence_number",
        "expected_data_type": "integer",
        "json_path": "$.approval_process[*].sequence_number"
      },
      "status": "error"
    }
  ]
}
```
