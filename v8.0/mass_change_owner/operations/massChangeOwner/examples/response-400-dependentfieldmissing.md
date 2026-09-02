Example of missing dependent comparator or value in criteria.

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "details": {
    "dependee": {
      "api_name": "field",
      "json_path": "$.criteria.field"
    },
    "api_name": "field|comparator|value",
    "json_path": "$.<field|comparator|value>"
  },
  "message": "Dependent Field missing",
  "status": "error"
}
```
