INVALID_DATA: field-mapping type is not a supported value in a final-approval action

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data",
      "details": {
        "api_name": "type",
        "supported_values": [
          "static",
          "merge_field"
        ],
        "json_path": "$.approval_process[*].rules[*].actions_upon_final_approval.actions[*].details.field_mappings[*].type"
      },
      "status": "error"
    }
  ]
}
```
