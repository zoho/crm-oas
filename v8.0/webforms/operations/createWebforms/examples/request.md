### `application/json` — SamplePostRequest

Full webform creation request for a Leads module form with double opt-in and spam control

```json
{
  "webforms": [
    {
      "name": "NewForm",
      "module": {
        "id": "4149211000000000125",
        "api_name": "Leads"
      },
      "layout": {
        "id": "4149211000000095055"
      },
      "form_attributes": {
        "color": "white",
        "width": 600,
        "align": "left",
        "font_attributes": {
          "size": 12,
          "color": "black",
          "family": "Arial"
        },
        "display_form_name": true
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
      "owner": {
        "id": "4149211000000605001"
      },
      "assignment_rule": {
        "id": "4149211000000851010"
      },
      "create_contact": false,
      "tags": [
        {
          "name": "tag1",
          "id": "4149211000000941079"
        }
      ],
      "spam_control": {
        "spam_possibility_threshold": 20
      },
      "double_optin_enabled": true,
      "double_optin_details": {
        "email_template": {
          "from_address": {
            "type": "3",
            "email": "Record Owner's Email",
            "api_name": "Owner"
          },
          "subject": "Confirm Your Registration with ${!org.company_name}",
          "content": "<html> <head> <meta http-equiv=\"Content-Type\" content=\"text/html;charset=UTF-8\"> <meta content=\"width=device-width\" name=\"viewport\"> <style> @media only screen and (max-width: 480px){} </style> </head> <body> <div style=\"direction:ltr;word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <div style=\"word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <div style=\"word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" width=\"100%\" style=\"width: 100%;background: #F4F7FF; padding: 0; margin: 0;font-family: Helvetica, sans-serif, arial;color: #444444;font-size: 15px;padding: 20px 0;\"> <tbody> <tr> <td> <table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" align=\"center\" width=\"600\" style=\"width: 600px;\"> <tbody> <tr> <td style=\"padding:10px 15px;\"> <p style=\"text-align: left; padding: 0px; margin: 0px;\"><font size=\"3\" face=\"Arial,Helvetica,sans-serif\">${!companyLogo}</font></p> </td> </tr> <tr> <td> <div style=\"border-radius: 10px; width: 100%; padding: 60px 50px; box-sizing: border-box; background: #fff;line-height: 1.4;box-shadow: 0px 5px 10px #0000000d;\"> <table style=\"line-height: 1.4;\"> <tr> <td> <p style=\"padding-bottom: 35px; margin: 0px;\">Hello ${!Leads.Last_Name},</p> <p style=\"padding-bottom: 35px; margin: 0px;\"><span style=\"font-family: Arial, Helvetica, sans-serif;\">Thank you for registering with&nbsp;<b>${!org.company_name}.</b></span><span style=\"font-family: Arial, Helvetica, sans-serif;\">&nbsp;To confirm your registration please click on the button given below. This option expires in <b>60 days.</b>&nbsp;</span></p> <table cellspacing=\"0\" cellpadding=\"0\" style=\"font-size: 15px; border: 1px solid rgb(83, 174, 119); background-color: rgb(91, 188, 130); border-radius: 5px;\"> <tbody> <tr> <td align=\"center\" style=\"overflow-wrap: break-word; word-break: break-word; border: 0px;\"><a href=\"#DOUBLEOPTIN_LINK#\" target=\"_blank\" rel=\"noopener noreferrer\" style=\"padding: 9px 15px;font-weight: bold;background: #43c177;display: block;font-size: 14px;color: #fff;text-decoration: none;\" data-zcqa=\"wf_TemplateConfirmBtn\">Confirm Registration</a></td> </tr> </tbody> </table> <p style=\"padding-bottom: 2px; padding-top: 20px; margin: 0px;\"><span style=\"font-family: Arial, Helvetica, sans-serif;\">If you have not registered, please just ignore this email.</span></p> <p style=\"padding-bottom: 2px; padding-top: 40px; margin: 0px;\">Regards, </p> <p style=\"margin: 0px;\"><span style=\"font-family: Arial, Helvetica, sans-serif;\"><b>${!org.company_name}</b></span></p> </td> </tr> </table> </div> </td> </tr> </tbody> </table> </td> </tr> <tr id=\"wfDot_dontreplynote\"></tr> </tbody> </table> </div> </div> </div> </body> </html>"
        },
        "confirm_page_content": "<html> <head> <meta http-equiv=\"Content-Type\"> <meta name=\"viewport\"> </head> <body> <div style=\"direction:ltr;word-wrap: break-word; word-break: break-word;\"> <div style=\"word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <div style=\"word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <div style=\"word-wrap: break-word; word-break: break-word; font-size:14px; color:#313949;\"> <table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" width=\"100%\" style=\"width: 100%;background: #F4F7FF; padding: 0; margin: 0;font-family: Helvetica, sans-serif, arial;color: #444444;font-size: 15px;padding: 20px 0;\"> <tbody> <tr> <td> <table cellpadding=\"0\" cellspacing=\"0\" border=\"0\" align=\"center\" width=\"600\" style=\"width: 600px;\"> <tbody> <tr> <td style=\"padding:10px 15px;\"> <p style=\"text-align: left; padding: 0px; margin: 0px;\"> <font size=\"3\" face=\"Arial,Helvetica,sans-serif\">${!companyLogo} </font> </p> </td> </tr> <tr> <td> <div style=\"border-radius: 10px; width: 100%; padding: 40px; box-sizing: border-box; background: #fff;box-shadow: 0px 5px 10px #0000000d;\"> <table style=\"margin-bottom: 10px;\"> <tbody> <tr> <td><img src=\"#infoalert.svg#\" align=\"\" height=\"24\" width=\"24\"></td> <td> <font size=\"4\"> <b>Please confirm your email.</b> </font> </td> </tr> </tbody> </table> <table style=\"line-height: 1.4;\"> <tr> <td> <p style=\"margin: 0px;\"> <font size=\"3\"> A configuration email has been sent to <b>${!Leads.Email}</b>. Please click on the <b>Confirm Registration</b> button in the email. </font> </p> </td> </tr> </table> </div> </td> </tr> </tbody> </table><br> </td> </tr> </tbody> </table> </div> </div> </div> </div> </body> </html>"
      },
      "notify_owner": {
        "system_mail": true,
        "id": "4149211000001200324",
        "name": "Zoho Bookings Template for Leads"
      },
      "acknowledge_visitor": {
        "auto_response_rule": {
          "id": "4149211000002923009",
          "name": "NewWebFormRule"
        },
        "template_id": "4149211000001200324",
        "template_name": "Zoho Bookings Template for Leads",
        "from_address": {
          "id": "4149211000000605001",
          "email": "mathivani.d+auditt0@zohotest.com",
          "name": "mathivani.d+auditt0@zohotest.com",
          "type": "0"
        },
        "reply_to_address": {
          "type": "0",
          "id": "4149211000000605001",
          "email": "",
          "api_name": "user"
        }
      },
      "visitor_tracking": {
        "portal_name": "salesunique",
        "tracking_code": "salesunique"
      },
      "approval_request": true,
      "type": "webform",
      "action_on_submit": "redirect_url",
      "action_value": "https://crmsec3.localzoho.com/crm/org104137941/settings/webform/create?name=NewForm&module=Leads&userTypeId=&type=webform",
      "location_url": [
        "http://mathi-14300.csez.zohocorpin.com:9007/crm/org44061292/settings/modules/Leads/layouts/111113000000003656",
        "https://crmsec3.localzoho.com/crm/org104137941/settings/webform/create?name=NewForm&module=Leads&userTypeId=&type=webform"
      ],
      "analytics_data": {
        "analytics_enabled": true,
        "url_analytics_enabled": true
      },
      "user_type": {
        "name": "ClientPortal",
        "active": true,
        "id": "4149211000002914008"
      },
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
      ]
    }
  ]
}
```
