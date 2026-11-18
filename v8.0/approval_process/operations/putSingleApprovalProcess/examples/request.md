### `application/json` — SamplePutRequest

Update a single Approval Process with rules and approver stages

```json
{
  "approval_process": [
    {
      "name": "Lead Module Approval Process",
      "id": "1034369000575839525",
      "description": "Lead Approval Process flow",
      "module": {
        "api_name": "Leads",
        "id": "111112000000000030"
      },
      "execute_on": "create | edit | create_or_edit",
      "active": true,
      "generated_type": "custom | internal",
      "sequence_number": 1,
      "rules": [
        {
          "name": "Rule 1",
          "id": "1034369000575839526",
          "criteria": {
            "comparator": "equal",
            "field": {
              "api_name": "Lead_Status",
              "id": "111112000000000030"
            },
            "value": "Contacted"
          },
          "sequence_number": 1,
          "overall_approval_type": "everyone_sequential | everyone_parallel | anyone",
          "overall_stages_record_modification": {
            "during_approval_waiting": {
              "update_allowed_for": "specific_fields | all_fields | no_fields",
              "fields": [
                {
                  "api_name": "Lead_Status",
                  "id": "111112000000000030"
                },
                {
                  "api_name": "Lead_Source",
                  "id": "111112000000000031"
                }
              ]
            },
            "after_record_rejection": {
              "update_allowed_for": "all_fields | specific_fields | no_fields",
              "fields": [
                {
                  "api_name": "Lead_Status",
                  "id": "111112000000000030"
                },
                {
                  "api_name": "Lead_Source",
                  "id": "111112000000000031"
                }
              ]
            }
          },
          "actions_per_approval": [
            {
              "approval_order": 1,
              "actions": [
                {
                  "name": "approval process",
                  "id": "947413000021529606",
                  "type": "field_updates"
                }
              ]
            }
          ],
          "approver_stages": [
            {
              "name": "Stage 1",
              "id": "1034369000575839527",
              "sequence_number": 1,
              "approver": {
                "type": "users | levels | roles | groups | static | reporting_manager | profiles | team_user",
                "resource": {
                  "id": "111111000000000039",
                  "name": "Jayaram kt"
                },
                "level": 2,
                "level_up_to": 3,
                "field": {
                  "id": "12345678",
                  "api_name": "Owner"
                },
                "based_on_field": {
                  "api_name": "Lead_Owner",
                  "id": "111112000000000030"
                },
                "everyone_approval_required": false
              },
              "record_modification": {
                "during_approval_waiting": {
                  "update_allowed_for": "specific_fields | all_fields | no_fields",
                  "fields": [
                    {
                      "api_name": "Lead_Status",
                      "id": "111112000000000030"
                    }
                  ]
                },
                "after_record_rejection": {
                  "update_allowed_for": "all_fields | specific_fields | no_fields",
                  "fields": [
                    {
                      "api_name": "Lead_Status",
                      "id": "111112000000000030"
                    }
                  ]
                }
              },
              "actions": {
                "on_approval_trigger": [
                  {
                    "type": "tasks",
                    "name": "Approval Assign Task",
                    "id": "111112000000000030"
                  }
                ],
                "on_approve": [
                  {
                    "type": "field_updates",
                    "name": "Update Approval Status FU",
                    "id": "111112000000000030"
                  }
                ]
              },
              "actions_per_approval": [
                {
                  "approval_order": 1,
                  "actions": [
                    {
                      "name": "approval process",
                      "id": "947413000021529606",
                      "type": "field_updates"
                    }
                  ]
                }
              ]
            }
          ],
          "process_admin_configuration": {
            "process_admin": [
              {
                "type": "users",
                "resources": [
                  {
                    "id": "111111000000000039",
                    "name": "Jayaram kt"
                  }
                ]
              }
            ],
            "record_modification": {
              "update_allowed_for": "all_fields | no_fields | approver_stages_record_modification_fields"
            },
            "notify_original_approvers_via": {
              "email": true,
              "feed": false
            }
          },
          "actions_upon_final_approval": {
            "send_default_emails_enabled": true,
            "actions": [
              {
                "type": "tasks | email_notifications | functions | field_updates | create_record | webhooks | cliq_notifications",
                "name": "Approval Completed Task",
                "details": {
                  "layout": {
                    "id": "4582374000006644115",
                    "name": "Standard"
                  },
                  "module": {
                    "id": "4582374000006644116",
                    "api_name": "custom21"
                  },
                  "field_mappings": [
                    {
                      "field": {
                        "id": "4582374000006644154",
                        "api_name": "Name"
                      },
                      "type": "static | merge_field",
                      "value": "test"
                    }
                  ]
                },
                "id": "111112000000000030"
              }
            ]
          },
          "actions_upon_rejection": {
            "rejection_type": "all_previous_stages | current_stage | current_approver_decide",
            "notify_original_approvers_via": {
              "email": true,
              "feed": false
            },
            "actions": [
              {
                "type": "tasks | email_notifications | functions | field_updates | create_record | webhooks | cliq_notifications",
                "name": "Approval Completed Task",
                "details": {
                  "layout": {
                    "id": "4582374000006644115",
                    "name": "Standard"
                  },
                  "module": {
                    "id": "4582374000006644116",
                    "api_name": "custom21"
                  },
                  "field_mappings": [
                    {
                      "field": {
                        "id": "4582374000006644154",
                        "api_name": "Name"
                      },
                      "type": "static | merge_field",
                      "value": "test"
                    }
                  ]
                },
                "id": "111112000000000030"
              }
            ]
          }
        }
      ]
    }
  ]
}
```
