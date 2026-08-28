# Examples: getTimelines

**GET /{module}/{recordId}/__timeline**

## Response examples

### Status `200` — `application/json` — GetTimelinesResponse

Sample timeline response for a CRM record

```json
{
  "__timeline": [
    {
      "done_by": {
        "name": "NMP",
        "id": "104456369000000325980"
      },
      "extension": null,
      "related_record": {
        "module": {
          "api_name": "Bugs",
          "id": "1034369000000813008"
        },
        "name": "Leads",
        "id": "1034369001121265138"
      },
      "automation_details": {
        "rule": {
          "name": "PriorityUpdateRule",
          "id": "1034369000016628528"
        },
        "type": "workflow_rule"
      },
      "record": {
        "module": {
          "api_name": "Deluge",
          "id": "null"
        },
        "name": "PriorityUpdateByNava",
        "id": "1034369000016628523"
      },
      "audited_time": "2025-11-12T13:13:15+05:30",
      "action": "updated",
      "id": "1034369001121309003",
      "source": "workflow",
      "type": "timeline",
      "field_history": null
    },
    {
      "done_by": {
        "name": "NMP",
        "id": "104456369000000325980"
      },
      "extension": {
        "namespace": "email",
        "id": "1467588000000119001",
        "signal": {
          "display_label": "zoho.email.incoming",
          "action": "received",
          "id": "1467588000000119019",
          "medium": "Emails"
        }
      },
      "related_record": {
        "module": {
          "api_name": "NMP_CRICKET",
          "id": "1034369000000813008"
        },
        "name": "Leads",
        "id": "1034369001121265138"
      },
      "automation_details": {
        "rule": {
          "name": "NMP RULE",
          "id": "1034369000016628528"
        },
        "type": "workflow_rule"
      },
      "record": {
        "module": {
          "api_name": "Dhoni",
          "id": "null"
        },
        "name": "MS Dhoni",
        "id": "1034369000016628523"
      },
      "audited_time": "2025-11-12T13:13:15+05:30",
      "action": "updated",
      "id": "1034369001121309003",
      "source": "workflow",
      "type": "timeline",
      "field_history": null
    },
    {
      "extension": {
        "namespace": "emailinsight",
        "id": "892620000000119000",
        "signal": {
          "display_label": "zoho.emailinsight.bounce",
          "action": "bounce",
          "id": "892620000000119000",
          "medium": "Emails"
        }
      },
      "done_by": null,
      "related_record": {
        "module": {
          "api_name": "Leads",
          "id": "892620000000000125"
        },
        "name": "praveen mail check",
        "id": "892620000005519100"
      },
      "automation_details": null,
      "record": {
        "module": null,
        "name": "Blah",
        "id": null
      },
      "audited_time": "2025-11-10T11:22:03+05:30",
      "action": "added",
      "id": "892620000005524002",
      "source": "crm_api",
      "type": "signal",
      "field_history": null
    }
  ],
  "info": {
    "next_page_token": null,
    "previous_page_token": null,
    "count": 11,
    "more_records": false,
    "page": 1,
    "per_page": 25
  }
}
```

### Status `400` — `application/json` — GetTimelinesBadRequestResponse

Error response for invalid request parameters

```json
{
  "status": "error",
  "code": "INVALID_MODULE",
  "message": "the module name given seems to be invalid",
  "details": {
    "resource_path_index": 1
  }
}
```
