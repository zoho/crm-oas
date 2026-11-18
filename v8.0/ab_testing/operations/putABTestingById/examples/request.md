### `application/json` — SamplePutRequest

Update AB testing configuration with scheduled date range

```json
{
  "AB_testing": [
    {
      "dynamic_allocation_by_zia": false,
      "base_form": {
        "id": "111111000000119267",
        "traffic": 40
      },
      "notify": false,
      "variant_form": [
        {
          "traffic": 40,
          "form_attributes": {
            "color": "#4F5252",
            "width": 800,
            "font_attributes": {
              "size": 14,
              "color": "#D5DEDE",
              "family": "Arial"
            },
            "align": "right"
          },
          "button_attributes": [
            {
              "color": "#fff",
              "name": "SubmitVar"
            },
            {
              "color": "#fff",
              "name": "ResetVar"
            }
          ],
          "form_fields": [
            {
              "help": null,
              "field": {
                "api_name": "Last_Name",
                "field_label": "Last Name",
                "id": "111111000000004840"
              },
              "hidden": false,
              "date_format": null,
              "type": "general",
              "required": true,
              "field_name": "Last Name"
            },
            {
              "help": null,
              "field_info": {
                "type": "file_upload",
                "field_label": "File Upload"
              },
              "hidden": false,
              "type": "advanced",
              "required": false
            }
          ]
        }
      ],
      "traffic": 80,
      "module": {
        "api_name": "Leads"
      },
      "condition": {
        "type": "range",
        "from": "2025-12-19T00:00:00+05:30",
        "to": "2025-12-29T00:00:00+05:30"
      },
      "name": "ABTesting_Leads_Updated",
      "winner_configuration": {
        "announce_automatically": false
      },
      "status": "scheduled"
    }
  ]
}
```
