Missing sequence_number field triggers MANDATORY_NOT_FOUND with json_path reference


```json
{
  "blueprints": [
    {
      "code": "MANDATORY_NOT_FOUND",
      "message": "Required field is missing",
      "details": {
        "api_name": "sequence_number",
        "json_path": "$.blueprints[*].sequence_number"
      },
      "status": "error"
    }
  ]
}
```
