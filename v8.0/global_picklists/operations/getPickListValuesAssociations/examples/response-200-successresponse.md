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
