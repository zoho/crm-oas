Successful retrieval of a single webform by ID

```json
{
  "webforms": [
    {
      "google_site": null,
      "encrypted_form_id": "5e8d3188a721b7ba5d9aabba2adddae6ea6a9f8379d32e0ec0bc16c2286dc36f97b6d5f4bd15b0ae3d133f4bc33d7383",
      "acknowledge_visitor": {
        "reply_to_address": {
          "id": "111113000000112455",
          "type": "0"
        },
        "template_name": "TestForm",
        "auto_response_rule": {
          "name": "TestRule",
          "id": "111113000000118101"
        },
        "template_id": "111113000000118094",
        "from_address": {
          "id": "111113000000112455",
          "type": "0"
        },
        "email_meta": {
          "userLookupEmailsObj": {},
          "otherEmailsObj": {},
          "orgEmailsArr": []
        }
      },
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
      "type": "webform",
      "action_on_submit": "thank_you_message",
      "form_fields": [
        {
          "help": null,
          "field": {
            "api_name": "Company",
            "field_label": "Company",
            "id": "4945485000000000555"
          },
          "hidden": false,
          "date_format": null,
          "type": "general",
          "required": true,
          "field_name": "Company"
        },
        {
          "help": null,
          "field": {
            "api_name": "Last_Name",
            "field_label": "Last Name",
            "id": "4945485000000000559"
          },
          "hidden": false,
          "date_format": null,
          "type": "general",
          "required": true,
          "field_name": "Last Name"
        }
      ],
      "encrypted_zgid": "f1da4d040c221de61d9c256b5f08a0ee6475d4bf65d7760f1bf7b742209b26bc",
      "action_value": "<p style=\"margin-bottom:5px\"><span id=\"successicon\" style=\"background:url(/crm/CRMClient/images/successalert.svg) no-repeat 0 0; width:22px; height:22px; display:inline-block; vertical-align:middle\"> </span><b>Thank you for your Confirmation</b></p><p><span style=\"\">Your response has been submitted successfully. We will reach out to you soon.</span></p>",
      "id": "111113000000133351",
      "owner": null,
      "created_time": "2025-11-26T17:55:32+05:30",
      "double_optin_details": {
        "confirm_page_content": "<html> <head> <meta http-equiv=\"Content-Type\"> <meta name=\"viewport\"> </head> <body> <div style=\"direction:ltr;word-wrap: break-word; word-break: break-word;\"> <div style=\"word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <div style=\"word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <div style=\"word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" width=\"100%\" style=\"width: 100%;background: #F4F7FF; padding: 0; margin: 0;font-family: Helvetica, sans-serif, arial;color: #444444;font-size: 15px;padding: 20px 0;\"> <tbody> <tr> <td> <table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" align=\"center\" width=\"600\" style=\"width: 600px;\"> <tbody> <tr> <td style=\"padding:10px 15px;\"> <p style=\"text-align: left; padding: 0px; margin: 0px;\"> <font size=\"3\" face=\"Arial,Helvetica,sans-serif\">${!companyLogo} </font> </p> </td> </tr> <tr> <td> <div style=\"border-radius: 10px; width: 100%; padding: 40px; box-sizing: border-box; background: #fff;box-shadow: 0px 5px 10px #0000000d;\"> <table style=\"margin-bottom: 10px;\"> <tbody> <tr> <td><img src=\"#infoalert.svg#\" align=\"\" height=\"24\" width=\"24\"></td> <td> <font size=\"4\"> <b>Please confirm your email.</b> </font> </td> </tr> </tbody> </table> <table style=\"line-height: 1.4;\"> <tr> <td> <p style=\"margin: 0px;\"> <font size=\"3\"> A configuration email has been sent to <b>${!Leads.Email}</b>. Please click on the <b>Confirm Registration</b> button in the email. </font> </p> </td> </tr> </table> </div> </td> </tr> </tbody> </table><br> </td> </tr> </tbody> </table> </div> </div> </div> </div> </body> </html>",
        "email_template": {
          "subject": "Confirm Your Registration with ${!org.company_name}",
          "from_address": {
            "api_name": "Owner",
            "id": "111113000000004816",
            "type": "field",
            "email": "Record Owner's Email"
          },
          "content": "<html> <head> <meta http-equiv=\"Content-Type\"> <meta name=\"viewport\"> <style> @media only screen and (max-width: 480px){} </style> </head> <body> <div style=\"direction:ltr;word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <div style=\"word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <div style=\"word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" width=\"100%\" style=\"width: 100%;background: #F4F7FF; padding: 0; margin: 0;font-family: Helvetica, sans-serif, arial;color: #444444;font-size: 15px;padding: 20px 0;\"> <tbody> <tr> <td> <table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" align=\"center\" width=\"600\" style=\"width: 600px;\"> <tbody> <tr> <td style=\"padding:10px 15px;\"> <p style=\"text-align: left; padding: 0px; margin: 0px;\"><font size=\"3\" face=\"Arial,Helvetica,sans-serif\">${!companyLogo}</font></p> </td> </tr> <tr> <td> <div style=\"border-radius: 10px; width: 100%; padding: 60px 50px; box-sizing: border-box; background: #fff;line-height: 1.4;box-shadow: 0px 5px 10px #0000000d;\"> <table style=\"line-height: 1.4;\"> <tr> <td> <p style=\"padding-bottom: 35px; margin: 0px;\">Hello ${!Leads.Last_Name},</p> <p style=\"padding-bottom: 35px; margin: 0px;\"><span style=\"font-family: Arial, Helvetica, sans-serif;\">Thank you for registering with&nbsp;<b>${!org.company_name}.</b></span><span style=\"font-family: Arial, Helvetica, sans-serif;\">&nbsp;To confirm your registration please click on the button given below. This option expires in <b>60 days.</b>&nbsp;</span></p> <table cellspacing=\"0\" cellpadding=\"0\" style=\"font-size: 15px; border: 1px solid rgb(83, 174, 119); background-color: rgb(91, 188, 130); border-radius: 5px;\"> <tbody> <tr> <td align=\"center\" style=\"overflow-wrap: break-word; word-break: break-word; border: 0px;\"><a href=\"#DOUBLEOPTIN_LINK#\" target=\"_blank\" rel=\"noopener noreferrer\" style=\"padding: 9px 15px;font-weight: bold;background: #43c177;display: block;font-size: 14px;color: #fff;text-decoration: none;\" data-zcqa=\"wf_TemplateConfirmBtn\">Confirm Registration</a></td> </tr> </tbody> </table> <p style=\"padding-bottom: 2px; padding-top: 20px; margin: 0px;\"><span style=\"font-family: Arial, Helvetica, sans-serif;\">If you have not registered, please just ignore this email.</span></p> <p style=\"padding-bottom: 2px; padding-top: 40px; margin: 0px;\">Regards, </p> <p style=\"margin: 0px;\"><span style=\"font-family: Arial, Helvetica, sans-serif;\"><b>${!org.company_name}</b></span></p> </td> </tr> </table> </div> </td> </tr> </tbody> </table> </td> </tr> <tr id=\"wfDot_dontreplynote\"></tr> </tbody> </table> </div> </div> </div> </body> </html>"
        }
      },
      "analytics_data": {
        "iframe_url_tracking_code": "<script>function wfa_pstMesgFrmFom (evt){if(evt.origin === 'https://mathi-14300.csez.zohocorpin.com:9007'|| evt.origin === 'https://crm.zohopublic.com'){var loc_obj=JSON.stringify({ origin:window.location.origin, pathname:window.location.pathname, search:window.location.search, hash:window.location.hash}); evt.source.postMessage(('prnt_wnd_pg_lc_rc_frm_prwindow_'+loc_obj), evt.origin);}}window.addEventListener('message', wfa_pstMesgFrmFom, false);</script>",
        "url_analytics_enabled": true,
        "analytics_enabled": true,
        "analytics_enabled_time": "2025-11-26T17:55:32+05:30",
        "tracking_code": "<!-- Do not remove this --- Analytics Tracking code starts --><script id='wf_anal' src='https://mathi-14300.csez.zohocorpin.com:9007/crm/WebFormAnalyticsServeServlet?rid=4a5ba47d875ed3b41bbb85f863ba78126c11e6f689847babd764187124f9d1cf49f05da9a976fa0c8991857f8040dd38gid8685cb282012eff955c7891a4b351cc2bd6376d83532bba8c38a965a5f165549gidc087d5a4ff91d116c8ac5fa00f7dc2882e5146e41a21b32e74fdcaac3fc50ac4gidb1eddeed62daf947f14070e887ea8b8da1e6f0bf6c80cd92386b44a7ed4696aa&tw=edd39a70ca6b636cea046395f51efbb5d341b133c180e88b9a42cd1ddb6fc800'></script><!-- Do not remove this --- Analytics Tracking code ends. -->"
      },
      "module": {
        "api_name": "Leads",
        "id": "111113000000002652"
      },
      "suggestion": null,
      "encrypted_module": "TGVhZHM=",
      "active": true,
      "adword_enabled": false,
      "notify_owner": {
        "name": "TestForm",
        "id": "111113000000118094"
      },
      "created_by": {
        "name": "Mathivani",
        "id": "111113000000112455"
      },
      "form_attributes": {
        "color": "white",
        "width": 600,
        "font_attributes": {
          "size": 12,
          "color": "black",
          "family": "Arial"
        },
        "display_form_name": true,
        "align": "left"
      },
      "location_url": [
        "https://mathi-14300.csez.zohocorpin.com:9007/crm/org44061292/settings/webform/create?name=ContainsAllData&module=Leads",
        "https://mathi-14300.csez.zohocorpin.com:9007/crm/org44061292/settings/webform/create?name=ContainsAllData&module=Leads&userTypeId=&type=webform"
      ],
      "double_optin_enabled": true,
      "tags": [
        {
          "name": "tas",
          "id": "111113000000118115"
        },
        {
          "name": "asdsa",
          "id": "111113000000120574"
        }
      ],
      "layout": {
        "display_label": "Standard",
        "name": "Standard",
        "id": "111113000000003656"
      },
      "approval_request": true,
      "create_contact": false,
      "assignment_rule": {
        "name": "test",
        "id": "111113000000123180"
      },
      "name": "ContainsAllData",
      "visitor_tracking": null,
      "spam_control": {
        "spam_possibility_threshold": 40
      }
    }
  ]
}
```
