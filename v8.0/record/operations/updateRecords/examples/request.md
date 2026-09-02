### `application/json` — Leads

Records retrieved from the Leads module

```json
{
  "data": [
    {
      "Layout": {
        "id": "554023000002734009"
      },
      "Lead_Source": "Employee Referral",
      "Company": "ABC",
      "Last_Name": "Daly",
      "First_Name": "Paul",
      "Email": "p.daly@zylker.com",
      "State": "Texas",
      "id": "111112000000142001"
    }
  ],
  "apply_feature_execution": [
    {
      "name": "layout_rules"
    }
  ],
  "skip_feature_execution": [
    {
      "name": "cadences"
    }
  ],
  "trigger": [
    "approval",
    "workflow",
    "blueprint",
    "pathfinder",
    "orchestration"
  ]
}
```

### `application/json` — SubformExample

Example request body for updating multiple subform records. "Project_Details" is the subform API name, and "Project_Name", "Project_Type", and "Expected_Budget" are fields in the subform.

```json
{
  "data": [
    {
      "Last_Name": "Patricia",
      "Company": "Info Technology",
      "id": "111112000000142001",
      "Project_Details": [
        {
          "Project_Name": "Mobile App Development",
          "Project_Type": "Development",
          "Expected_Budget": 50000
        },
        {
          "Project_Name": "Infrastructure Upgrade",
          "Project_Type": "Infrastructure",
          "Expected_Budget": 30000
        }
      ]
    }
  ]
}
```
