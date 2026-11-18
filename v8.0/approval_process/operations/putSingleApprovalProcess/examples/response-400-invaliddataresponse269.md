Invalid data type for the field-mapping id of a rejection action

```json
{
  "approval_process": [
    {
      "code": "INVALID_DATA",
      "message": "Invalid data type",
      "details": {
        "api_name": "id",
        "expected_data_type": "bigint",
        "json_path": "$.approval_process[*].rules[*].actions_upon_rejection.actions[*].details.field_mappings[*].field.id"
      },
      "status": "error"
    }
  ]
}
```
