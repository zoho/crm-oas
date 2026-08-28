# Examples: getAssignmentRules

**GET /settings/automation/assignment_rules**

## Response examples

### Status `200` — `application/json` — Success200

Successful Assignment Rule operation

```json
{
  "assignment_rules": [
    {
      "api_name": "OrderAssignment",
      "module": {
        "api_name": "Orders",
        "id": "5264350000312423443",
        "name": "Orders"
      },
      "name": "Order owner assignment rule",
      "id": "5264350000141324328",
      "description": "Assignment rule to assign owners for order records",
      "created_by": {
        "id": "5264350000141324329",
        "name": "Nivedha"
      },
      "created_time": "2025-01-23T00:00:00+05:30",
      "modified_by": {
        "id": "5264350000141111111",
        "name": "Ravivarma"
      },
      "modified_time": "2025-01-01T16:43:11+05:30",
      "default_assignee": {
        "id": "5264350000141111111",
        "name": "Ravivarma",
        "type": "user",
        "resource": {
          "id": "5264350000141111111",
          "name": "Ravivarma"
        }
      }
    },
    {
      "api_name": "OrderAssignment",
      "module": {
        "api_name": "Orders",
        "id": "5264350000312423443",
        "name": "Orders"
      },
      "name": "Order owner assignment rule",
      "id": "5264350000141324329",
      "description": "Assignment rule to assign owners for order records",
      "created_by": {
        "id": "5264350000141324329",
        "name": "Nivedha"
      },
      "created_time": "2025-01-23T00:00:00+05:30",
      "modified_by": {
        "id": "5264350000141111111",
        "name": "Ravivarma"
      },
      "modified_time": "2025-01-01T16:43:11+05:30",
      "default_assignee": {
        "id": "526435000014111111",
        "name": "Ravivarma",
        "type": "user",
        "resource": {
          "id": "5264350000141111111",
          "name": "Ravivarma"
        }
      }
    }
  ]
}
```
