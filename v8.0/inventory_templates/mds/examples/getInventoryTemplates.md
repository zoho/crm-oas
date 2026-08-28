# Examples: getInventoryTemplates

**GET /settings/inventory_templates**

## Response examples

### Status `400` — `application/json` — InvalidData

Invalid module name in request

```json
{
  "code": "INVALID_DATA",
  "message": "The module name provided is invalid.",
  "status": "error",
  "details": {
    "param_name": "module"
  }
}
```

### Status `400` — `application/json` — PatternNotMatched

Invalid sort_order parameter value

```json
{
  "code": "PATTERN_NOT_MATCHED",
  "details": {
    "param_name": "sort_order"
  },
  "message": "Please check whether the input values are correct",
  "status": "error"
}
```
