# Examples: getAssignmentRuleById

**GET /settings/automation/assignment_rules/{id}**

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
  "assignment_rules": [
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
        "id": "5264350000141111111",
        "name": "Ravivarma",
        "type": "user",
        "resource": {
          "id": "5264350000141111111",
          "name": "Ravivarma"
        }
      },
      "rule_entries": [
        {
          "id": "526435000014296015",
          "sequence_number": 0,
          "criteria": {
            "group_operator": "AND",
            "group": [
              {
                "comparator": "equal",
                "field": {
                  "api_name": "Annual_Revenue",
                  "id": "526435000000000581"
                },
                "type": "value",
                "value": "1000"
              },
              {
                "comparator": "contains",
                "field": {
                  "api_name": "Email",
                  "id": "526435000000000563"
                },
                "type": "field",
                "value": {
                  "api_name": "Lookup_3.Full_Name",
                  "id": "526435000000000597"
                }
              }
            ]
          },
          "assign_to": {
            "type": "users",
            "resources": [
              {
                "name": "Ted Mosby",
                "id": "526435000000670072"
              },
              {
                "name": "Nivedha",
                "id": "526435000000227013"
              }
            ]
          },
          "user_availability_based_on": [
            "online_status",
            "shift_timing"
          ],
          "followup_actions": [
            {
              "type": "tasks",
              "resources": [
                {
                  "name": "Test task",
                  "id": "526435000014344004"
                }
              ]
            }
          ]
        },
        {
          "id": "526435000014296016",
          "sequence_number": 1,
          "criteria": null,
          "assign_to": {
            "type": "profile",
            "resource": {
              "name": "Participants",
              "id": "526435000000670072"
            }
          },
          "user_availability_based_on": null,
          "followup_actions": null
        },
        {
          "id": "526435000014296015",
          "sequence_number": 2,
          "criteria": {
            "comparator": "equal",
            "field": {
              "api_name": "City",
              "id": "526435000000000581"
            },
            "type": "value",
            "value": "Chennai"
          },
          "assign_to": {
            "type": "group",
            "resource": {
              "name": "Chennai Branch Managers",
              "id": "526435000000670072"
            }
          },
          "user_availability_based_on": [
            "shift_timing"
          ],
          "followup_actions": [
            {
              "type": "tasks",
              "resources": [
                {
                  "name": "Test task",
                  "id": "526435000014344004"
                }
              ]
            }
          ]
        },
        {
          "id": "526435000014296016",
          "sequence_number": 3,
          "criteria": null,
          "assign_to": {
            "type": "role",
            "resource": {
              "name": "CEO",
              "id": "526435000000670072"
            }
          },
          "user_availability_based_on": null,
          "followup_actions": null
        },
        {
          "id": "526435000014296016",
          "sequence_number": 4,
          "criteria": null,
          "assign_to": {
            "type": "zia_suggested_users"
          },
          "user_availability_based_on": null,
          "followup_actions": null
        }
      ]
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionToManageARErrorResponseExample

NO_PERMISSION error for Assignment Rule access

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_AR_{moduleName}"
    ]
  },
  "message": "User does not have sufficient permission to manage assignment rules of given module",
  "status": "error"
}
```
