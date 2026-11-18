Successful response with AB Testing configuration details


```json
{
  "AB_testing": [
    {
      "created_time": "2025-12-19T13:41:15+05:30",
      "dynamic_allocation_by_zia": false,
      "complete_restart_info": null,
      "module": {
        "api_name": "Leads",
        "id": "111111000000002652"
      },
      "suggestion": null,
      "base_form": {
        "winner": false,
        "old_traffic": null,
        "name": "Webform",
        "id": "111111000000119105",
        "winner_confidence": null,
        "traffic": 50
      },
      "created_by": {
        "name": "Kk",
        "id": "111111000000059475"
      },
      "notify": false,
      "traffic_diversion": null,
      "condition": {
        "unit": 30,
        "period": "days",
        "type": "duration",
        "remaining": 29
      },
      "variant_form": [
        {
          "encrypted_form_id": "4173971da72c0aaacac7f1c2fc9def0d5126bcf7155aabc25da49ffe49327df2ecd2a9e2b8448761d23472adeb23b967",
          "form_fields": [
            {
              "help": null,
              "hidden": false,
              "field": {
                "api_name": "Last_Name",
                "field_label": "Last Name",
                "id": "111111000000004840"
              },
              "date_format": null,
              "type": "general",
              "required": true,
              "field_name": "Last Name"
            }
          ],
          "winner": false,
          "old_traffic": null,
          "name": "Webform",
          "button_attributes": [
            {
              "color": "#fff",
              "name": "Submit"
            },
            {
              "color": "#fff",
              "name": "Reset"
            }
          ],
          "id": "111111000000119113",
          "form_attributes": {
            "color": "white",
            "width": 600,
            "font_attributes": {
              "size": 12,
              "color": "black",
              "family": "Arial"
            },
            "align": "left"
          },
          "tracking_code": "<!-- Do not remove this --- Analytics Tracking code starts --><script id='wf_anal' src='https://kiruba-5799.csez.zohocorpin.com:8443/crm/WebFormAnalyticsServeServlet?rid=36250793e16caedc474e057c39a6d1a3f353204b8399d50e0af97aa01b041e98ec710a7a573691966d8c133aaddd5d1fgid8e00c046b496966024fd9e77144aca3ca81f890587ea7d65c1128a45f9e65e4fgida42c64dcd4e8d4490fcfa196a5edf56bdcc078053c19a39c7bc9c8541652e8e6gid74e5eee8092dfc97b99f96007a8a0ba43632b07d0f901a58a4d6ebd666dab550gid84b2393a64ddcabd2e502a79eb16e3a84fe35e853d02106d45b01b93805a0540cbf9caacc76cde89d2fbdd24d125aea7&tw=193916e8ea0dcc654e035198c32be88e2b73f03742b9f19baa9b80f5a37d4cd2'></script><!-- Do not remove this --- Analytics Tracking code ends. -->",
          "winner_confidence": null,
          "traffic": 50
        }
      ],
      "pause_resume_info": null,
      "name": "ABTesting_Leads",
      "winner_configuration": {
        "announce_automatically": false
      },
      "id": "111111000000119112",
      "status": "running",
      "traffic": 100
    }
  ]
}
```
