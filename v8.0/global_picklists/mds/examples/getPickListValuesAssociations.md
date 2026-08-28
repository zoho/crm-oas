# Examples: getPickListValuesAssociations

**GET /settings/global_picklists/{id}/actions/pick_list_values_associations**

## Parameter examples

### `id` (path) — Example

```json
"111111000000055938"
```

## Response examples

### Status `200` — `application/json` — SuccessResponse

Example response with picklist value associations

```json
{
  "pick_list_values_associations": [
    {
      "resources": [
        {
          "name": "dddddd",
          "details": [
            {
              "name": "Big Deal Rule",
              "id": "111113000000045665",
              "type": "Workflow"
            }
          ],
          "id": "111113000000071003"
        },
        {
          "name": "Testt",
          "details": [],
          "id": "111113000000064001"
        }
      ],
      "type": "field_update"
    },
    {
      "resources": [
        {
          "name": "Another",
          "details": [
            {
              "name": "Qualify Leads through Call - V1",
              "id": "111113000000047921",
              "type": "Orchestration",
              "transition": {
                "name": "Create Lead",
                "id": "111113000000048457"
              }
            }
          ],
          "id": "111113000000072027"
        }
      ],
      "type": "task"
    },
    {
      "resources": [
        {
          "name": "sss",
          "details": {
            "module": {
              "plural_label": "Leads",
              "api_name": "Leads",
              "id": "111113000000000050"
            }
          },
          "id": "111113000000077032"
        }
      ],
      "type": "blueprint"
    },
    {
      "resources": [
        {
          "name": "Qualify Leads through Call - V1",
          "details": {
            "actions": [
              {
                "module": {
                  "api_name": "Leads",
                  "id": "111113000000000042"
                },
                "id": "111113000000082133",
                "type": "CreateRecord",
                "transition": {
                  "name": "Create Lead",
                  "id": "111113000000048457"
                }
              }
            ]
          },
          "id": "111113000000047921"
        }
      ],
      "type": "orchestration"
    },
    {
      "resources": [
        {
          "name": "Big Deal Rule",
          "details": {
            "actions": [
              {
                "module": {
                  "api_name": "Deals",
                  "id": "111113000000000048"
                },
                "id": "111113000000072001",
                "type": "CreateRecord"
              }
            ]
          },
          "id": "111113000000045665"
        }
      ],
      "type": "workflow"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidId

Invalid ID in path

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — DeletionInProgress

Deletion already in progress

```json
{
  "code": "NOT_ALLOWED",
  "details": {
    "resource_path_index": 2
  },
  "message": "global picklist deletion in progress.",
  "status": "error"
}
```

### Status `400` — `application/json` — MissingParameter

Required parameter missing

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param": "picklist_value_id"
  },
  "message": "One of the expected parameter is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidParameterValue

Invalid parameter value

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "picklist_value_id"
  },
  "message": "the id given seems to be invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — ErrorExample

```json
{
  "code": "NO_PERMISSION",
  "message": "permission denied",
  "details": {
    "permissions": [
      "Crm_Implied_Customize_Zoho_CRM"
    ]
  },
  "status": "error"
}
```

### Status `500` — `application/json` — ErrorExample

```json
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error",
  "details": {},
  "status": "error"
}
```
