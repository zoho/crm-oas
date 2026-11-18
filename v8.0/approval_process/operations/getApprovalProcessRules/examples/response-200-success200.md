Successful retrieval of rules for a valid Approval Process

```json
{
  "rules": [
    {
      "sequence_number": 1,
      "name": "Rule1",
      "overall_approval_type": "everyone_parallel",
      "criteria": {
        "group_operator": "and",
        "group": [
          {
            "comparator": "equal",
            "field": "CFSingleUser.name",
            "value": [
              "947413000015708143",
              "947413000015708236"
            ]
          },
          {
            "comparator": "equal",
            "field": "CFPickList",
            "value": [
              "Option 1",
              "Option 2"
            ]
          }
        ]
      },
      "process_admin_configuration": {
        "notify_original_approvers_via": {
          "feed": false,
          "email": true
        },
        "process_admin": [
          {
            "resources": [
              {
                "name": "jayaram kt",
                "id": "947413000000328001"
              },
              {
                "name": "Osaka Sales Administration User1",
                "id": "947413000007750712"
              },
              {
                "name": "Jayaram UserNew11",
                "id": "947413000007750738"
              }
            ],
            "type": "users"
          }
        ],
        "record_modification": {
          "update_allowed_for": "approver_stages_record_modification_fields"
        }
      },
      "actions_upon_final_approval": {
        "actions": [
          {
            "name": "Email Notif 1",
            "id": "947413000003601372",
            "type": "email_notifications"
          },
          {
            "related_details": null,
            "name": "AP Bug Task 1",
            "id": "947413000000554001",
            "type": "tasks"
          },
          {
            "name": "Leads webhookOnApproval",
            "id": "947413000005795105",
            "type": "webhooks"
          },
          {
            "name": "WF custom func",
            "id": "947413000020031022",
            "type": "functions"
          }
        ]
      },
      "actions_upon_rejection": {
        "notify_original_approvers_via": {
          "feed": true,
          "email": true
        },
        "actions": [
          {
            "name": "webhook from workflow",
            "id": "947413000020031005",
            "type": "webhooks"
          },
          {
            "name": "updateSomeNumbers",
            "id": "947413000007892101",
            "type": "functions"
          },
          {
            "name": "approval process",
            "id": "947413000020109122",
            "type": "email_notifications"
          },
          {
            "name": "approval process",
            "id": "947413000020109123",
            "type": "email_notifications"
          },
          {
            "related_details": null,
            "name": "approval process",
            "id": "947413000020109144",
            "type": "field_updates"
          }
        ]
      },
      "id": "947413000014810021",
      "overall_stages_record_modification": {
        "during_approval_waiting": {
          "update_allowed_for": "no_fields"
        },
        "after_record_rejection": {
          "update_allowed_for": "all_fields"
        }
      },
      "approver_stages": [
        {
          "sequence_number": 1,
          "name": "Stage 1",
          "approver": {
            "resource": {
              "name": "Jayaram associate",
              "id": "947413000000500001"
            },
            "type": "users"
          },
          "actions": {
            "on_approve": [
              {
                "related_details": null,
                "name": "approval process",
                "id": "947413000020109142",
                "type": "field_updates"
              }
            ],
            "on_approval_trigger": [
              {
                "related_details": null,
                "name": "Email AP Latest Localzoho",
                "id": "947413000001305793",
                "type": "tasks"
              }
            ]
          },
          "id": "947413000020109168"
        },
        {
          "sequence_number": 2,
          "name": "Stage 2",
          "approver": {
            "resource": {
              "name": "CEO",
              "id": "947413000000015966"
            },
            "everyone_approval_required": true,
            "type": "roles"
          },
          "actions": {
            "on_approve": [
              {
                "related_details": null,
                "name": "approval process",
                "id": "947413000020109130",
                "type": "field_updates"
              }
            ],
            "on_approval_trigger": [
              {
                "related_details": null,
                "name": "Email AP Latest Localzoho",
                "id": "947413000001305793",
                "type": "tasks"
              }
            ]
          },
          "id": "947413000020109156"
        },
        {
          "sequence_number": 3,
          "name": "Stage 3",
          "approver": {
            "resource": {
              "name": "TestGroup1",
              "id": "947413000004659004"
            },
            "everyone_approval_required": false,
            "type": "groups"
          },
          "actions": {
            "on_approve": [
              {
                "related_details": null,
                "name": "approval process",
                "id": "947413000020109130",
                "type": "field_updates"
              }
            ],
            "on_approval_trigger": [
              {
                "related_details": null,
                "name": "Email AP Latest Localzoho",
                "id": "947413000001305793",
                "type": "tasks"
              }
            ]
          },
          "id": "947413000020109154"
        },
        {
          "approver": {
            "type": "levels",
            "level": 2,
            "based_on_field": {
              "id": "111111000000004784",
              "api_name": "Owner"
            },
            "everyone_approval_required": false
          },
          "sequence_number": 4,
          "name": "Stage 4",
          "actions": {
            "on_approval_trigger": [
              {
                "related_details": null,
                "name": "approval process",
                "type": "tasks",
                "id": "111111000000078477"
              }
            ],
            "on_approve": [
              {
                "related_details": null,
                "name": "approval process",
                "type": "field_updates",
                "id": "111111000000078238"
              }
            ]
          },
          "id": "947413000020109160"
        },
        {
          "sequence_number": 5,
          "name": "Stage 5",
          "approver": {
            "based_on_field": {
              "api_name": "Owner",
              "id": "947413000000000553"
            },
            "everyone_approval_required": false,
            "type": "levels",
            "level_up_to": "2"
          },
          "actions": {
            "actions_per_approval": [
              {
                "approval_order": 1,
                "actions": [
                  {
                    "related_details": null,
                    "name": "approval process",
                    "id": "947413000020109132",
                    "type": "field_updates"
                  }
                ]
              }
            ],
            "on_approval_trigger": [
              {
                "related_details": null,
                "name": "approval process",
                "id": "947413000001305793",
                "type": "tasks"
              }
            ]
          },
          "id": "947413000020109158"
        },
        {
          "sequence_number": 6,
          "name": "Stage 6",
          "approver": {
            "field": {
              "api_name": "Owner",
              "data_type": "ownerlookup",
              "id": "947413000000000553"
            },
            "type": "static"
          },
          "actions": {
            "on_approve": [
              {
                "related_details": null,
                "name": "approval process",
                "id": "947413000020109140",
                "type": "field_updates"
              }
            ],
            "on_approval_trigger": [
              {
                "related_details": null,
                "name": "approval process",
                "id": "947413000001305793",
                "type": "tasks"
              }
            ]
          },
          "id": "947413000020109166"
        },
        {
          "sequence_number": 7,
          "name": "Stage 7",
          "approver": {
            "based_on_field": {
              "api_name": "Owner",
              "id": "947413000000000553"
            },
            "type": "reporting_manager"
          },
          "actions": {
            "on_approve": [
              {
                "related_details": null,
                "name": "approval process",
                "id": "947413000020109140",
                "type": "field_updates"
              }
            ],
            "on_approval_trigger": [
              {
                "related_details": null,
                "name": "approval process",
                "id": "947413000001305793",
                "type": "tasks"
              }
            ]
          },
          "id": "947413000020109164"
        },
        {
          "approver": {
            "type": "static",
            "field": {
              "id": "111111000000004826",
              "data_type": "userlookup",
              "api_name": "Created_By"
            }
          },
          "sequence_number": 8,
          "name": "Stage 8",
          "actions": {
            "on_approval_trigger": [
              {
                "related_details": null,
                "name": "approval process",
                "type": "tasks",
                "id": "111111000000078481"
              }
            ],
            "on_approve": [
              {
                "related_details": null,
                "name": "approval process",
                "type": "field_updates",
                "id": "111111000000078246"
              }
            ]
          },
          "id": "947413000020109170"
        },
        {
          "sequence_number": 9,
          "name": "Stage 9",
          "approver": {
            "resource": {
              "name": "Team User 1",
              "id": "111111000000056059"
            },
            "everyone_approval_required": "false",
            "type": "team_user"
          },
          "actions": {
            "on_approval_trigger": [
              {
                "related_details": null,
                "name": "approval process",
                "type": "tasks",
                "id": "111111000000078481"
              }
            ],
            "on_approve": [
              {
                "related_details": null,
                "name": "approval process",
                "type": "field_updates",
                "id": "111111000000078246"
              }
            ]
          },
          "id": "947413000020109125"
        },
        {
          "sequence_number": 10,
          "name": "Stage10",
          "approver": {
            "resource": {
              "name": "Requester",
              "id": "111111000000056059"
            },
            "everyone_approval_required": "false",
            "type": "profiles"
          },
          "actions": {
            "on_approval_trigger": [
              {
                "related_details": null,
                "name": "approval process",
                "type": "tasks",
                "id": "111111000000078481"
              }
            ],
            "on_approve": [
              {
                "related_details": null,
                "name": "approval process",
                "type": "field_updates",
                "id": "111111000000078246"
              }
            ]
          },
          "id": "947413000020109134"
        }
      ],
      "actions_per_approval": [
        {
          "approval_order": 1,
          "actions": [
            {
              "related_details": null,
              "name": "FU11",
              "id": "111111000000078491",
              "type": "field_updates"
            }
          ]
        },
        {
          "approval_order": 2,
          "actions": [
            {
              "related_details": null,
              "name": "FU12",
              "id": "111111000000078495",
              "type": "field_updates"
            }
          ]
        },
        {
          "approval_order": 3,
          "actions": [
            {
              "related_details": null,
              "name": "FU1",
              "id": "111111000000078224",
              "type": "field_updates"
            }
          ]
        },
        {
          "approval_order": 4,
          "actions": [
            {
              "related_details": null,
              "name": "FU2",
              "id": "111111000000078230",
              "type": "field_updates"
            }
          ]
        },
        {
          "approval_order": 5,
          "actions": [
            {
              "related_details": null,
              "name": "FU3",
              "id": "111111000000078234",
              "type": "field_updates"
            }
          ]
        },
        {
          "approval_order": 6,
          "actions": [
            {
              "related_details": null,
              "name": "FU4",
              "id": "111111000000078238",
              "type": "field_updates"
            }
          ]
        },
        {
          "approval_order": 7,
          "actions": [
            {
              "related_details": null,
              "name": "FU5",
              "id": "111111000000078242",
              "type": "field_updates"
            }
          ]
        },
        {
          "approval_order": 8,
          "actions": [
            {
              "related_details": null,
              "name": "FU6",
              "id": "111111000000078246",
              "type": "field_updates"
            }
          ]
        },
        {
          "approval_order": 9,
          "actions": [
            {
              "related_details": null,
              "name": "FU7",
              "id": "111111000000078250",
              "type": "field_updates"
            }
          ]
        },
        {
          "approval_order": 10,
          "actions": [
            {
              "related_details": null,
              "name": "FU8",
              "id": "111111000000078254",
              "type": "field_updates"
            }
          ]
        }
      ]
    }
  ]
}
```
