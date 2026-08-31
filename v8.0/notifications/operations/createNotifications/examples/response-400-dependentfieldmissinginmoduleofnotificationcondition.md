Dependent field field_selection missing from the notification condition

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "message": "DEPENDENT_FIELD_MISSING",
  "details": {
    "api_name": "field_selection",
    "json_path": "$.watch[0].notification_condition[0].field_selection",
    "dependee": {
      "api_name": "type",
      "json_path": "$.watch[0].notification_condition[0].type"
    }
  },
  "status": "error"
}
```
