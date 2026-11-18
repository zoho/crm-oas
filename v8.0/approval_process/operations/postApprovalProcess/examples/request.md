### `application/json` — SamplePostRequest

Sample request to create an Approval Process

```json
{
  "approval_process": [
    {
      "name": "Lead Module Approval Process",
      "description": "Lead Approval Process flow",
      "module": {
        "api_name": "Leads",
        "id": "111112000000000030"
      },
      "execute_on": "create_or_edit",
      "active": true,
      "generated_type": "custom",
      "rules": [
        {
          "name": "Rule 1",
          "criteria": {
            "comparator": "equal",
            "field": {
              "api_name": "Lead_Status",
              "id": "111112000000000030"
            },
            "value": "Contacted"
          },
          "overall_approval_type": "everyone_sequential",
          "overall_stages_record_modification": {
            "during_approval_waiting": {
              "update_allowed_for": "specific_fields",
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
              "update_allowed_for": "specific_fields",
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
              "sequence_number": 1,
              "approver": {
                "type": "levels",
                "level_up_to": 3,
                "based_on_field": {
                  "api_name": "Lead_Owner",
                  "id": "111112000000000030"
                },
                "everyone_approval_required": false
              },
              "record_modification": {
                "during_approval_waiting": {
                  "update_allowed_for": "specific_fields",
                  "fields": [
                    {
                      "api_name": "Lead_Status",
                      "id": "111112000000000030"
                    }
                  ]
                },
                "after_record_rejection": {
                  "update_allowed_for": "specific_fields",
                  "fields": [
                    {
                      "api_name": "Lead_Status",
                      "id": "111112000000000030"
                    }
                  ]
                }
              },
              "actions": {
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
              "update_allowed_for": "approver_stages_record_modification_fields"
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
                "type": "tasks",
                "name": "Approval Completed Task",
                "id": "111112000000000030"
              },
              {
                "type": "cliq_notifications",
                "name": "Notify Leads - Owner, Creator",
                "details": {
                  "message": "Record has been approved",
                  "notify_to": {
                    "module": {
                      "id": "111111000000002656"
                    },
                    "notify_fields": {
                      "fields": [
                        {
                          "id": "111111000000004864"
                        },
                        {
                          "id": "111111000000004906"
                        }
                      ],
                      "static_fields": [
                        {
                          "name": "owner_manager"
                        }
                      ]
                    },
                    "type": "fields"
                  }
                }
              },
              {
                "type": "cliq_notifications",
                "name": "Notify Zoho Cliq - Sobin",
                "details": {
                  "message": "Test notification to user",
                  "notify_to": {
                    "id": "684880122",
                    "name": "Sobin",
                    "type": "user"
                  }
                }
              },
              {
                "type": "cliq_notifications",
                "name": "Notify Zoho Cliq - #External Integration Spikes",
                "details": {
                  "message": "Test notification to channel",
                  "notify_to": {
                    "id": "P1775998001426569813",
                    "name": "#External Integration",
                    "type": "channel"
                  }
                }
              }
            ]
          },
          "actions_upon_rejection": {
            "rejection_type": "all_previous_stages",
            "notify_original_approvers_via": {
              "email": true,
              "feed": false
            },
            "actions": [
              {
                "type": "tasks",
                "name": "Approval Completed Task",
                "id": "111112000000000030"
              },
              {
                "type": "cliq_notifications",
                "name": "Notify Leads - Owner, Creator",
                "details": {
                  "message": "Record has been rejected",
                  "notify_to": {
                    "module": {
                      "id": "111111000000002656"
                    },
                    "notify_fields": {
                      "fields": [
                        {
                          "id": "111111000000004864"
                        },
                        {
                          "id": "111111000000004906"
                        }
                      ],
                      "static_fields": [
                        {
                          "name": "owner_manager"
                        }
                      ]
                    },
                    "type": "fields"
                  }
                }
              },
              {
                "type": "cliq_notifications",
                "name": "Notify Zoho Cliq - Sobin",
                "details": {
                  "message": "Test notification to user",
                  "notify_to": {
                    "id": "684880122",
                    "name": "Sobin",
                    "type": "user"
                  }
                }
              },
              {
                "type": "cliq_notifications",
                "name": "Notify Zoho Cliq - #External Integration Spikes",
                "details": {
                  "message": "Test notification to channel",
                  "notify_to": {
                    "id": "P1775998001426569813",
                    "name": "#External Integration",
                    "type": "channel"
                  }
                }
              }
            ]
          }
        }
      ]
    }
  ]
}
```
