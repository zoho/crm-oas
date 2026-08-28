# Examples: getWebhooks

**GET /settings/automation/webhooks**

## Response examples

### Status `200` — `application/json` — Success200

Successful list of webhook summary objects

```json
{
  "webhooks": [
    {
      "created_time": "2025-07-12T06:55:54-07:00",
      "lock_status": {
        "locked": false
      },
      "editable": true,
      "module": {
        "api_name": "Leads",
        "id": "5725767000000002175"
      },
      "related_module": null,
      "deletable": true,
      "description": "Protected Data",
      "source": "crm",
      "created_by": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "url": "https://webhook.site/3588de27-e3bd-4237-894b-f140143f3d99",
      "feature_type": "workflow",
      "http_method": "POST",
      "modified_time": "2025-07-12T06:55:54-07:00",
      "associated": false,
      "name": "Zoho's Data",
      "modified_by": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "id": "5725767000007186002"
    },
    {
      "created_time": "2025-07-06T08:00:01-07:00",
      "lock_status": {
        "locked": false
      },
      "editable": true,
      "module": {
        "api_name": "Leads",
        "id": "5725767000000002175"
      },
      "related_module": null,
      "deletable": true,
      "description": null,
      "source": "crm",
      "created_by": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "url": "https://webhook.site/3588de27-e3bd-4237-894b-f140143f3d99",
      "feature_type": "workflow",
      "http_method": "POST",
      "modified_time": "2025-07-06T08:00:01-07:00",
      "associated": false,
      "name": "Zoho",
      "modified_by": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "id": "5725767000007084238"
    },
    {
      "created_time": "2025-07-06T04:16:24-07:00",
      "lock_status": {
        "locked": false
      },
      "editable": true,
      "module": {
        "api_name": "Leads",
        "id": "5725767000000002175"
      },
      "related_module": null,
      "deletable": true,
      "description": "Description about the webhook",
      "source": "crm",
      "created_by": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "url": "https://webhook.site/3588de27-e3bd-4237-894b-f140143f3d99",
      "feature_type": "workflow",
      "http_method": "POST",
      "modified_time": "2025-07-06T04:16:24-07:00",
      "associated": false,
      "name": "New Lead Webhook API",
      "modified_by": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "id": "5725767000007093002"
    }
  ],
  "info": {
    "per_page": 200,
    "count": 10,
    "page": 1,
    "more_records": false,
    "max_limit": 200
  }
}
```

### Status `200` — `application/json` — Success200Paginated

Successful paginated list showing page one of two pages containing records.

```json
{
  "webhooks": [
    {
      "created_time": "2025-07-12T06:55:54-07:00",
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
      "deletable": true,
      "description": null,
      "source": "user",
      "created_by": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "url": "https://example.com/webhook-handler",
      "feature_type": "workflow",
      "http_method": "POST",
      "modified_time": "2025-07-12T06:55:54-07:00",
      "associated": false,
      "name": "Lead Notification Webhook",
      "modified_by": {
        "name": "Patricia Boyle",
        "id": "5725767000000411001"
      },
      "id": "5725767000007186002"
    }
  ],
  "info": {
    "per_page": 1,
    "count": 1,
    "page": 1,
    "more_records": true
  }
}
```

### Status `400` — `application/json` — InvalidModuleResponse1

Invalid module API name in module parameter

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

### Status `400` — `application/json` — InvalidDataResponse1

Invalid query parameter value for sort_order

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "sort_order"
  },
  "message": "The value provided to the param is Invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse2

Invalid sort_by parameter value

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "sort_by"
  },
  "message": "The value provided to the param is Invalid",
  "status": "error"
}
```

### Status `400` — `application/json` — InvalidDataResponse3

Invalid feature_type parameter value

```json
{
  "code": "INVALID_DATA",
  "details": {
    "param_name": "feature_type"
  },
  "message": "The value provided to the param is Invalid",
  "status": "error"
}
```

### Status `403` — `application/json` — NoPermissionResponse1

Missing Manage Workflow permission for listing webhooks

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
