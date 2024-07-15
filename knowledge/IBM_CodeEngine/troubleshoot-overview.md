---

copyright:
  years: [{CURRENT_YEAR}]
lastupdated: "[{LAST_UPDATED_DATE}]"

keywords: troubleshooting, issues, status, get help, code engine, getting help

subcollection: {[subcollection]}

---

{{site.data.keyword.attribute-definition-list}}

# Troubleshooting overview
{: #troubleshooting_over}

Review some general help for troubleshooting issues with {{site.data.keyword.codeenginefull}}.
{: shortdesc}

## General ways to resolve issues
{: #help-general}

* Make sure that your command-line tools are up-to-date.
    * In the command line, you are notified when updates to the `ibmcloud` CLI and plug-ins are available. Be sure to keep your CLI up-to-date so that you can use all available commands and options.
    * Update the `ibmcloud ce` CLI plug-in whenever an update is available. For more information, see [Updating the {[kn-service]} CLI]({[url]}install-cli#update-cli)
    * When you use any of the CLI `get` commands, such as the **`app get`**, **`job get`**, **`jobrun get`**, **`build get`**, or **`buildrun get`** commands, you can specify the `--o yaml` option to obtain more fine-grained details about your {[kn-service]} component, which can be helpful in troubleshooting. For more information about the `get` commands, see [CLI Reference]({[url]}cli).
* Review the other troubleshooting issues for {[kn-service]}.
* Review the [FAQs]({[url]}faqs).
* Enable and review [logging]({[url]}view-logs) and [monitoring]({[url]}monitor) details to troubleshoot your {[kn-service]} components.

## Reviewing Cloud issues and status
{: #help-cloud-status}

1. To see whether {{site.data.keyword.cloud_notm}} is available, [check the {{site.data.keyword.cloud_notm}} status page](https://cloud.ibm.com/status?selected=status){: external}.
2. Filter for the **Code Engine** component and review any cloud status issue.
3. Review the [Limits and quotas for {[kn-service]}]({[url]}limits).
4. For issues in open source projects that are used by {{site.data.keyword.cloud_notm}}, see the [IBM open source and third-party policy](https://www.ibm.com/support/pages/node/737271){: external}.

## Getting help
{: #help-functions}

If you still cannot resolve your issue, see [Getting support]({[url]}get-support). For any general questions or feedback, post in Slack.



