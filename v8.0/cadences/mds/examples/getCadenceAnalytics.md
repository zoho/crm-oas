# Examples: getCadenceAnalytics

**GET /settings/automation/cadences/{id}/actions/analytics**

## Response examples

### Status `200` — `application/json` — Success200

Successful Cadence analytics response

```json
{
  "cadences": [
    {
      "module": {
        "api_name": "Leads",
        "id": "111112000000002628"
      },
      "name": "publish cadence",
      "follow_ups": [
        {
          "analytics": {
            "open_tasks_count": 1,
            "failed_tasks_count": 0,
            "subject": "task1",
            "completed_tasks_count": 0,
            "tasks_count": 1
          },
          "parent_follow_up": null,
          "action": {
            "name": "task1",
            "type": "tasks"
          },
          "id": "111112000000094014"
        },
        {
          "analytics": {
            "created_calls_count": 0,
            "cancelled_calls_count": 0,
            "failed_calls_count": 0,
            "completed_calls_count": 0,
            "scheduled_calls_count": 1,
            "subject": "Call scheduled with test",
            "calls_count": 1,
            "overdue_calls_count": 0,
            "missed_calls_count": 0
          },
          "parent_follow_up": {
            "id": "111112000000094014",
            "type": "tasks"
          },
          "action": {
            "name": "Demo",
            "type": "schedule_call"
          },
          "id": "111112000000094026"
        },
        {
          "analytics": {
            "email_count": 0,
            "bounced_email_count": 0,
            "clicked_email_count": 0,
            "replied_email_count": 0,
            "sent_email_count": 0,
            "unsent_email_count": 1,
            "opened_email_count": 0
          },
          "parent_follow_up": {
            "id": "111112000000094026",
            "type": "schedule_call"
          },
          "action": {
            "template": {
              "name": "Template",
              "id": "111112000000080016"
            },
            "name": "1",
            "type": "email_notifications"
          },
          "id": "111112000000094048"
        },
        {
          "analytics": {
            "whatsapp_count": 0,
            "delivered_whatsapp_count": 0,
            "failed_whatsapp_count": 0
          },
          "parent_follow_up": {
            "id": "111111000000115093",
            "type": "email_notifications"
          },
          "action": {
            "message_template": {
              "id": "111111000000115032",
              "title": "templatewhtsapp"
            },
            "name": "cad whtsapp",
            "id": "111111000000115279",
            "type": "whatsapp_message_notification"
          },
          "id": "111111000000115111"
        }
      ],
      "id": "111112000000094004",
      "created_by": {
        "name": "Poongodi89 S",
        "id": "111112000000057662"
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidCadenceId

Invalid Cadence ID error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 3
  },
  "message": "the given id seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Invalid filter data error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "follow_ups_executed_from"
  },
  "message": "The given from param is invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse1

Missing api_name in field error

```json
{
  "code": "DEPENDENT_PARAM_MISSING",
  "details": {
    "dependee": {
      "param_name": "follow_ups_executed_till"
    },
    "param_name": "follow_ups_executed_from"
  },
  "message": "Dependent Param missing",
  "status": "error"
}
```

### Status `400` — `application/json` — MandatoryNotFoundResponse2

Missing filters parameter error

```json
{
  "code": "DEPENDENT_PARAM_MISSING",
  "details": {
    "dependee": {
      "param_name": "follow_ups_executed_from"
    },
    "param_name": "follow_ups_executed_till"
  },
  "message": "Dependent Param missing",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersMandatorynotFound

Mandatory field not found in filters error

```json
{
  "code": "MANDATORY_NOT_FOUND",
  "details": {
    "api_name": "api_name",
    "json_path": "$.field.api_name",
    "param_name": "filters"
  },
  "message": "required field not found",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersComparatorMissing

Missing comparator in filters error

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "details": {
    "dependee": {
      "api_name": "field",
      "json_path": "$.field"
    },
    "api_name": "comparator",
    "json_path": "$.comparator",
    "param_name": "filters"
  },
  "message": "dependent field is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersValueMissing

Missing value in filters error

```json
{
  "code": "DEPENDENT_FIELD_MISSING",
  "details": {
    "dependee": {
      "api_name": "field",
      "json_path": "$.field"
    },
    "api_name": "value",
    "json_path": "$.value",
    "param_name": "filters"
  },
  "message": "dependent field is missing",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersFieldMissing

Missing field in filters error

```json
{
  "code": "EXPECTED_FIELD_MISSING",
  "details": {
    "expected_fields": [
      {
        "api_name": "field",
        "json_path": "$.field"
      }
    ]
  },
  "message": "Specify atleast one field",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersApiNameInvalidDataType

Invalid data type for filters api_name error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "text",
    "api_name": "api_name",
    "json_path": "$.field.api_name",
    "supported_values": [
      "follow_ups.action.type"
    ],
    "param_name": "filters"
  },
  "message": "invalid data",
  "status": "error"
}
```

### Status `400` — `application/json` — FiltersValueNotSupported

Unsupported filter value error

```json
{
  "code": "DEPENDENT_MISMATCH",
  "details": {
    "dependee": {
      "api_name": "api_name",
      "json_path": "$.field.api_name"
    },
    "api_name": "value",
    "json_path": "$.value",
    "supported_values": [
      "tasks",
      "schedule_call",
      "email_notifications",
      "whatsapp_message_notification"
    ],
    "param_name": "filters"
  },
  "message": "The value given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — ComparatorNotSupported

Unsupported comparator value error

```json
{
  "code": "DEPENDENT_MISMATCH",
  "details": {
    "dependee": {
      "api_name": "api_name",
      "json_path": "$.field.api_name"
    },
    "api_name": "comparator",
    "json_path": "$.comparator",
    "supported_values": [
      "equal"
    ],
    "param_name": "filters"
  },
  "message": "The value given seems to be invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataType

Invalid data type in filters error

```json
{
  "code": "INVALID_DATA",
  "details": {
    "expected_data_type": "datetime",
    "param_name": "follow_ups_executed_from"
  },
  "message": "invalid data type",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

No permission to view Cadence analytics error

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_View_Cadences"
    ]
  },
  "message": "No permission",
  "status": "error"
}
```
