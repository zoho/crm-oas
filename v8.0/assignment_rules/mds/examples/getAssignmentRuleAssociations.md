# Examples: getAssignmentRuleAssociations

**GET /settings/automation/assignment_rules/{id}/actions/associations**

## Parameter examples

### `id` (path) — Typical

sample value 1

```json
"123456789"
```

### `id` (path) — LargeId

Maximum long value example

```json
"9223372036854775807"
```

## Response examples

### Status `200` — `application/json` — Success200

Successful Assignment Rule operation

```json
{
  "associations": [
    {
      "type": "workflow_rules",
      "resources": [
        {
          "id": "234356789",
          "name": "Lead create workflow flow",
          "_details": {}
        }
      ]
    }
  ]
}
```
