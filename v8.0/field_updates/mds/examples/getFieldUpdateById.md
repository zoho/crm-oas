# Examples: getFieldUpdateById

**GET /settings/automation/field_updates/{id}**

## Response examples

### Status `200` — `application/json` — Success200

Success response for status 200

```json
{
  "field_updates": [
    {
      "created_time": "2025-11-19T03:12:20-08:00",
      "update_type": "append",
      "lock_status": {
        "locked": false
      },
      "apply_assignment_threshold": false,
      "editable": true,
      "module": {
        "singular_label": "Deal",
        "plural_label": "Deals WF",
        "api_name": "Deals",
        "moduleName": "Potentials",
        "id": "3361265000000000131"
      },
      "related_module": null,
      "deletable": true,
      "source": "crm",
      "type": "static",
      "created_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "notify": false,
      "feature_type": "workflow",
      "modified_time": "2025-11-19T03:12:20-08:00",
      "field": {
        "ui_type": 2,
        "api_name": "Pipeline",
        "id": "3361265000000236001"
      },
      "dependent_fields": [
        {
          "field": {
            "ui_type": 26,
            "api_name": "Stage",
            "id": "3361265000000000525"
          },
          "value": "Qualification"
        }
      ],
      "associated": false,
      "related_records": [
        {
          "api_name": "Events",
          "id": "3361265000000000145"
        },
        {
          "api_name": "Calls",
          "id": "3361265000000017015"
        }
      ],
      "name": "FieldUpdateGET",
      "modified_by": {
        "name": "B Indumathi",
        "id": "3361265000000535001"
      },
      "id": "3361265000006103364",
      "value": "Test"
    }
  ]
}
```

### Status `400` — `application/json` — InvalidIncludeInnerDetailsResponse

Error response with code INVALID_DATA: include_inner_details value is invalid

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "include_inner_details"
  },
  "message": "The value provided to the param is Invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Error response with code NO_PERMISSION: feature not available in this edition

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow",
      "Crm_Implied_Customize_Zoho_CRM",
      "Crm_Implied_Manage_ConnectedWorkflow"
    ]
  },
  "message": "feature not available in this edition",
  "status": "error"
}
```
