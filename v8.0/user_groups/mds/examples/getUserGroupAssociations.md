# Examples: getUserGroupAssociations

**GET /settings/user_groups/{group}/actions/associations**

## Response examples

### Status `200` — `application/json` — Success200

Successful response with group associations

```json
{
  "associations": [
    {
      "type": "data_sharing",
      "resource": {
        "id": "16045511334961104",
        "name": "Sharing Rule Name"
      },
      "details": {
        "module": {
          "id": "16045511334961105",
          "api_name": "Leads"
        }
      }
    },
    {
      "type": "workflow_rules",
      "resource": {
        "id": "16045511334961105",
        "name": "Workflow Name"
      },
      "details": null
    },
    {
      "type": "assignment_rules",
      "resource": {
        "id": "16045511334961106",
        "name": "Assignment Rule Name"
      },
      "details": {
        "module": {
          "id": "16045511334961105",
          "api_name": "Leads"
        }
      }
    },
    {
      "type": "email_notifications",
      "resource": {
        "id": "16045511334961107",
        "name": "Email Notification Name"
      },
      "details": null
    },
    {
      "type": "approval_process",
      "resource": {
        "id": "16045511334961108",
        "name": "Approval Process Name"
      },
      "details": null
    },
    {
      "type": "review_process",
      "resource": {
        "id": "16045511334961109",
        "name": "Review Process Name"
      },
      "details": null
    },
    {
      "type": "calendar_bookings",
      "resource": {
        "id": "16045511334961110",
        "name": "Calendar Booking Name"
      },
      "details": {
        "module": {
          "id": "16045511334961105",
          "api_name": "Leads"
        }
      }
    }
  ]
}
```

### Status `400` — `application/json` — InvalidDataResponse1

Invalid group ID in request URL

```json
{
  "code": "INVALID_DATA",
  "details": {
    "resource_path_index": 2
  },
  "message": "the related id given seems to be invalid",
  "status": "error"
}
```

### Status `404` — `application/json` — InvalidData

Invalid URL pattern

```json
{
  "code": "INVALID_URL_PATTERN",
  "details": {},
  "message": "The provided group ID is invalid.",
  "status": "error"
}
```
