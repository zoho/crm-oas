Scheduled jobs list retrieved successfully

```json
{
  "scheduled_jobs": [
    {
      "job_id": "3759037000000570605",
      "action": "REPLACE_PICKLIST_OPTION",
      "module": {
        "id": "3759037000000570346",
        "api_name": "Potentials"
      },
      "details": {
        "records": {
          "total": 400,
          "processed": 0,
          "failed": 0
        },
        "workflow_rules": {
          "total": 10,
          "processed": 0,
          "failed": 0
        },
        "field_dependency": {
          "total": 3,
          "processed": 0,
          "failed": 0
        },
        "dashboard_criteria": {
          "total": 5,
          "processed": 0,
          "failed": 0
        }
      },
      "status": "SCHEDULED",
      "message": "Job scheduled"
    },
    {
      "job_id": "3759037000000570606",
      "action": "DELETE_PICKLIST_OPTION",
      "module": {
        "id": "3759037000000570456",
        "api_name": "Leads"
      },
      "details": {
        "records": {
          "total": 400,
          "processed": 300,
          "failed": 100
        },
        "workflow_rules": {
          "total": 10,
          "processed": 10,
          "failed": 0
        },
        "field_dependency": {
          "total": 2,
          "processed": 2,
          "failed": 0
        },
        "dashboard_criteria": {
          "total": 5,
          "processed": 5,
          "failed": 0
        }
      },
      "status": "COMPLETED",
      "message": "Job completed"
    }
  ],
  "info": {
    "page": 1,
    "per_page": 200,
    "count": 10,
    "more_records": true
  }
}
```
