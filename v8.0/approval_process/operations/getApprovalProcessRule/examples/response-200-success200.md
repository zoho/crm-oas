Approval process rule retrieved successfully

```json
{
  "rules": [
    {
      "sequence_number": 1,
      "overall_approval_type": "everyone_sequential",
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
      "name": "Rule1",
      "id": "947413000014810021",
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
      "approver_stages": [
        {
          "sequence_number": 1,
          "name": "Stage 1",
          "approver": {
            "resource": {
              "name": "TestGroup1",
              "id": "947413000004659004"
            },
            "everyone_approval_required": false,
            "type": "groups"
          },
          "record_modification": {
            "during_approval_waiting": {
              "update_allowed_for": "all_fields"
            },
            "after_record_rejection": {
              "update_allowed_for": "no_fields"
            }
          },
          "actions": {
            "on_approve": [
              {
                "name": "approval process",
                "id": "947413000020109142",
                "type": "field_updates",
                "related_details": null
              }
            ],
            "on_approval_trigger": [
              {
                "name": "Email AP Latest Localzoho",
                "id": "947413000001305793",
                "type": "tasks",
                "related_details": null
              }
            ]
          },
          "id": "947413000020109046"
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
                "name": "approval process",
                "id": "947413000020109130",
                "type": "field_updates",
                "related_details": null
              }
            ],
            "on_approval_trigger": [
              {
                "name": "Email AP Latest Localzoho",
                "id": "947413000001305793",
                "type": "tasks",
                "related_details": null
              }
            ]
          },
          "record_modification": {
            "during_approval_waiting": {
              "update_allowed_for": "no_fields"
            },
            "after_record_rejection": {
              "update_allowed_for": "all_fields"
            }
          },
          "id": "947413000020109048"
        }
      ],
      "actions_upon_final_approval": {
        "actions": [
          {
            "name": "Email Notif 1",
            "id": "947413000003601372",
            "type": "email_notifications"
          },
          {
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
            "name": "approval process",
            "id": "947413000020109144",
            "type": "field_updates"
          }
        ]
      }
    }
  ]
}
```
