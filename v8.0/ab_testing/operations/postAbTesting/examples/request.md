### `application/json` — SamplePostRequest

Create AB testing with base form, variant form, and duration condition

```json
{
  "AB_testing": [
    {
      "dynamic_allocation_by_zia": false,
      "base_form": {
        "id": "111111000000118837",
        "traffic": 50
      },
      "notify": true,
      "variant_form": [
        {
          "traffic": 50,
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
      "traffic": 100,
      "module": {
        "api_name": "Leads"
      },
      "condition": {
        "type": "duration",
        "period": "days",
        "unit": 30
      },
      "name": "ABTesting_Leads",
      "winner_configuration": {
        "announce_automatically": true,
        "conversion_percentage_difference": 20
      },
      "status": "running"
    }
  ]
}
```
