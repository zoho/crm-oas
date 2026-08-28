# Examples: getWorkflowConfigurations

**GET /workflow_configurations**

## Response examples

### Status `200` — `application/json` — Success200

Workflow configurations for the Leads module

```json
{
  "workflow_configurations": {
    "related_triggers_details": [
      {
        "api_name": "Notes",
        "module": {
          "singular_label": "Note",
          "plural_label": "Notes",
          "api_name": "Notes",
          "name": "Notes",
          "id": "3361265000000000147"
        },
        "name": "Notes",
        "triggers": [
          {
            "api_name": "create",
            "deprecated": false,
            "name": "Create",
            "scheduled_actions_supported": true,
            "actions": [
              "add_tags",
              "remove_tags",
              "email_notifications",
              "create_record",
              "add_meeting",
              "schedule_call",
              "webhooks",
              "functions",
              "flow"
            ]
          },
          {
            "api_name": "create_or_edit",
            "deprecated": false,
            "name": "CreateorEdit",
            "scheduled_actions_supported": true,
            "actions": [
              "add_tags",
              "remove_tags",
              "email_notifications",
              "create_record",
              "add_meeting",
              "schedule_call",
              "webhooks",
              "functions",
              "flow"
            ]
          },
          {
            "api_name": "edit",
            "deprecated": false,
            "name": "Edit",
            "scheduled_actions_supported": true,
            "actions": [
              "add_tags",
              "remove_tags",
              "email_notifications",
              "create_record",
              "add_meeting",
              "schedule_call",
              "webhooks",
              "functions",
              "flow"
            ]
          },
          {
            "api_name": "delete",
            "deprecated": false,
            "name": "Delete",
            "scheduled_actions_supported": false,
            "actions": [
              "email_notifications",
              "webhooks",
              "functions"
            ]
          }
        ]
      }
    ],
    "triggers": [
      {
        "api_name": "create",
        "deprecated": false,
        "name": "Create",
        "scheduled_actions_supported": true,
        "actions": [
          "field_updates",
          "assign_owner",
          "add_tags",
          "remove_tags",
          "email_notifications",
          "create_record",
          "add_meeting",
          "schedule_call",
          "convert",
          "webhooks",
          "functions",
          "flow"
        ]
      },
      {
        "api_name": "create_or_edit",
        "deprecated": false,
        "name": "CreateorEdit",
        "scheduled_actions_supported": true,
        "actions": [
          "field_updates",
          "assign_owner",
          "add_tags",
          "remove_tags",
          "email_notifications",
          "create_record",
          "add_meeting",
          "schedule_call",
          "convert",
          "webhooks",
          "functions",
          "flow"
        ]
      },
      {
        "api_name": "edit",
        "deprecated": false,
        "name": "Edit",
        "scheduled_actions_supported": true,
        "actions": [
          "field_updates",
          "assign_owner",
          "add_tags",
          "remove_tags",
          "email_notifications",
          "create_record",
          "add_meeting",
          "schedule_call",
          "convert",
          "webhooks",
          "functions",
          "flow"
        ]
      },
      {
        "api_name": "field_update",
        "deprecated": false,
        "name": "FieldUpdate",
        "scheduled_actions_supported": true,
        "actions": [
          "field_updates",
          "assign_owner",
          "add_tags",
          "remove_tags",
          "email_notifications",
          "create_record",
          "add_meeting",
          "schedule_call",
          "convert",
          "webhooks",
          "functions",
          "flow"
        ]
      },
      {
        "api_name": "section_update",
        "deprecated": false,
        "name": "SectionUpdate",
        "scheduled_actions_supported": true,
        "actions": [
          "field_updates",
          "assign_owner",
          "add_tags",
          "remove_tags",
          "email_notifications",
          "create_record",
          "add_meeting",
          "schedule_call",
          "convert",
          "webhooks",
          "functions",
          "flow"
        ]
      },
      {
        "api_name": "delete",
        "deprecated": false,
        "name": "Delete",
        "scheduled_actions_supported": false,
        "actions": [
          "email_notifications",
          "webhooks",
          "functions"
        ]
      },
      {
        "api_name": "date_or_datetime",
        "deprecated": false,
        "name": "DateBased",
        "scheduled_actions_supported": true,
        "actions": [
          "field_updates",
          "assign_owner",
          "add_tags",
          "remove_tags",
          "email_notifications",
          "create_record",
          "add_meeting",
          "schedule_call",
          "webhooks",
          "functions",
          "flow"
        ]
      },
      {
        "api_name": "score_increase",
        "deprecated": false,
        "name": "ScoreIncrease",
        "scheduled_actions_supported": false,
        "actions": [
          "field_updates",
          "assign_owner",
          "add_tags",
          "remove_tags",
          "email_notifications",
          "webhooks",
          "functions",
          "flow"
        ]
      },
      {
        "api_name": "score_decrease",
        "deprecated": false,
        "name": "ScoreDecrease",
        "scheduled_actions_supported": false,
        "actions": [
          "field_updates",
          "assign_owner",
          "add_tags",
          "remove_tags",
          "email_notifications",
          "webhooks",
          "functions",
          "flow"
        ]
      },
      {
        "api_name": "score_update",
        "deprecated": false,
        "name": "ScoreUpdate",
        "scheduled_actions_supported": false,
        "actions": [
          "field_updates",
          "assign_owner",
          "add_tags",
          "remove_tags",
          "email_notifications",
          "webhooks",
          "functions",
          "flow"
        ]
      }
    ],
    "actions": [
      {
        "is_clickable": true,
        "associate_action": false,
        "limit_per_action": 10,
        "api_name": "remove_tags",
        "supported_in_scheduled_action": true,
        "name": "RemoveTags",
        "limit": 1
      },
      {
        "is_clickable": true,
        "associate_action": false,
        "limit_per_action": null,
        "api_name": "convert",
        "supported_in_scheduled_action": false,
        "name": "Convert",
        "limit": 1
      },
      {
        "is_clickable": true,
        "associate_action": true,
        "limit_per_action": null,
        "api_name": "functions",
        "supported_in_scheduled_action": true,
        "name": "Deluge",
        "limit": 1
      },
      {
        "is_clickable": true,
        "associate_action": false,
        "limit_per_action": null,
        "api_name": "assign_owner",
        "supported_in_scheduled_action": true,
        "name": "AssignOwner",
        "limit": 3
      },
      {
        "is_clickable": true,
        "associate_action": true,
        "limit_per_action": null,
        "api_name": "field_updates",
        "supported_in_scheduled_action": true,
        "name": "Fieldupdate",
        "limit": 5
      },
      {
        "is_clickable": true,
        "associate_action": false,
        "limit_per_action": 10,
        "api_name": "add_tags",
        "supported_in_scheduled_action": true,
        "name": "AddTags",
        "limit": 1
      },
      {
        "is_clickable": true,
        "associate_action": true,
        "limit_per_action": null,
        "api_name": "email_notifications",
        "supported_in_scheduled_action": true,
        "name": "Alert",
        "limit": 5
      },
      {
        "is_clickable": true,
        "associate_action": true,
        "limit_per_action": null,
        "api_name": "webhooks",
        "supported_in_scheduled_action": true,
        "name": "Webhook",
        "limit": 1
      },
      {
        "is_clickable": true,
        "associate_action": false,
        "limit_per_action": null,
        "api_name": "create_record",
        "supported_in_scheduled_action": true,
        "name": "CreateRecord",
        "limit": 1
      },
      {
        "is_clickable": true,
        "associate_action": false,
        "limit_per_action": null,
        "api_name": "schedule_call",
        "supported_in_scheduled_action": true,
        "name": "ScheduleCall",
        "limit": 1
      },
      {
        "is_clickable": true,
        "associate_action": false,
        "limit_per_action": null,
        "api_name": "add_meeting",
        "supported_in_scheduled_action": true,
        "name": "AddMeeting",
        "limit": 1
      },
      {
        "is_clickable": true,
        "associate_action": false,
        "limit_per_action": null,
        "api_name": "flow",
        "supported_in_scheduled_action": true,
        "name": "Flow",
        "limit": 1
      }
    ]
  }
}
```

### Status `400` — `application/json` — RequiredParamMissingResponse

REQUIRED_PARAM_MISSING error when the module parameter is omitted

```json
{
  "code": "REQUIRED_PARAM_MISSING",
  "details": {
    "param_name": "module"
  },
  "message": "required param not found",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidModuleResponse

INVALID_MODULE error when the module API name is not valid

```json
{
  "code": "INVALID_MODULE",
  "details": {
    "param_name": "module"
  },
  "message": "The value provided to the param is Invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse

NO_PERMISSION error when workflow management privilege is absent

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```
