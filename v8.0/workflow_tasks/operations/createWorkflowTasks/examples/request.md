### `application/json` — SamplePostRequest

Sample request body

```json
{
  "tasks": [
    {
      "module": {
        "api_name": "Leads",
        "id": "6660682000000002175"
      },
      "notify": true,
      "field_mappings": [
        {
          "field": {
            "api_name": "Description",
            "id": "6660682000000002291"
          },
          "type": "merge_field",
          "value": "Automated task for ${!Leads.First_Name}${!Leads.Last_Name}"
        },
        {
          "field": {
            "api_name": "Subject",
            "id": "6660682000000002271"
          },
          "type": "static",
          "value": "SampleTask"
        },
        {
          "field": {
            "id": "6660682000000000223",
            "api_name": "Due_Date"
          },
          "type": "execution_time",
          "value": {
            "period": "business_days",
            "unit": "3",
            "trigger_field": "${CURRENTTIME}",
            "sign": "plus"
          }
        },
        {
          "field": {
            "api_name": "Status",
            "id": "6660682000000002279"
          },
          "type": "static",
          "value": "Not Started"
        },
        {
          "field": {
            "api_name": "Priority",
            "id": "6660682000000002281"
          },
          "type": "static",
          "value": "High"
        },
        {
          "field": {
            "api_name": "URL_1",
            "id": "6660682000001522480"
          },
          "type": "merge_field",
          "value": "${!Leads.Website}"
        },
        {
          "field": {
            "api_name": "Number_1",
            "id": "6660682000001522575"
          },
          "type": "merge_field",
          "value": "${!Leads.No_of_Employees}"
        },
        {
          "display_value": "100000000000000000",
          "field": {
            "api_name": "Long_Integer_1",
            "id": "6660682000001522533"
          },
          "type": "static",
          "value": "100000000000000000"
        },
        {
          "field": {
            "api_name": "Single_Line_1",
            "id": "6660682000001522561"
          },
          "type": "static",
          "value": "sample task"
        },
        {
          "field": {
            "api_name": "Pick_List_1",
            "id": "6660682000000922691"
          },
          "type": "static",
          "value": "Voter ID"
        },
        {
          "field": {
            "api_name": "Email_1",
            "id": "6660682000001465098"
          },
          "type": "static",
          "value": "john@zohotest.cim"
        },
        {
          "field": {
            "api_name": "Percent_1",
            "id": "6660682000001522617"
          },
          "type": "static",
          "value": "50"
        },
        {
          "field": {
            "api_name": "Currency_1",
            "id": "6660682000001522589"
          },
          "type": "merge_field",
          "value": "${!Leads.Annual_Revenue}"
        },
        {
          "field": {
            "api_name": "Phone_1",
            "id": "6660682000001522603"
          },
          "type": "merge_field",
          "value": "${!Leads.Phone}"
        },
        {
          "field": {
            "api_name": "Decimal_1",
            "id": "6660682000001522547"
          },
          "type": "static",
          "value": "12"
        }
      ],
      "name": "NewTask",
      "feature_type": "workflow"
    }
  ]
}
```
