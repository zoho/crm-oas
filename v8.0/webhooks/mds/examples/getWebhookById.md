# Examples: getWebhookById

**GET /settings/automation/webhooks/{webhookId}**

## Response examples

### Status `200` — `application/json` — Success200

Successful response for Get Webhook by ID

```json
{
  "webhooks": [
    {
      "created_time": "2025-07-06T04:16:24-07:00",
      "headers": {
        "module_parameters": [
          {
            "name": "lead_modified_time",
            "value": "${!Leads.Modified_Time}"
          }
        ],
        "custom_parameters": [
          {
            "name": "x-api-key",
            "value": "my-static-api-key"
          }
        ]
      },
      "lock_status": {
        "locked": false,
        "message": null
      },
      "editable": true,
      "module": {
        "api_name": "Leads",
        "id": "5725767000000002175"
      },
      "related_module": null,
      "url_parameters": null,
      "deletable": true,
      "description": "Sends lead data to external CRM sync service",
      "source": "user",
      "body": {
        "type": "form_data",
        "format": null,
        "form_data_content": {
          "module_parameters": [
            {
              "name": "lead_email",
              "value": "${!Leads.Email}"
            }
          ],
          "custom_parameters": [
            {
              "name": "source_system",
              "value": "zoho_crm"
            }
          ]
        }
      },
      "created_by": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "url": "https://example.com/webhook-handler",
      "feature_type": "workflow",
      "http_method": "POST",
      "modified_time": "2025-07-12T06:55:54-07:00",
      "associated": true,
      "name": "Lead Sync Webhook",
      "modified_by": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "id": "5725767000007084001",
      "date_time_format": {
        "date_format": "dd-mmmm-yyyy",
        "datetime_format": "dd-mm-yyyy H:M:S",
        "time_zone": "Etc/GMT+12"
      },
      "authentication": {
        "type": "general",
        "connection_name": ""
      }
    }
  ]
}
```

### Status `403` — `application/json` — NoPermissionResponse1

NO_PERMISSION error for missing Manage Webhook permission

```json
{
  "code": "NO_PERMISSION",
  "details": {
    "permissions": [
      "Crm_Implied_Manage_Workflow"
    ]
  },
  "message": "permission denied",
  "status": "error"
}
```
