---

copyright:
  years: [{CURRENT_YEAR}]
lastupdated: "[{LAST_UPDATED_DATE}]"

keywords: troubleshooting for code engine subscriptions, subscriptions, tips for subscriptions, ping, cron, object storage

subcollection: {[subcollection]}

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Debugging subscriptions
{: #troubleshoot-subscriptions}
{: troubleshoot}

Use the tips to learn how to troubleshoot {{site.data.keyword.codeenginefull}} subscriptions.
{: shortdesc}

## Subscription limits to consider 
{: #ts-subscription-limits}

The maximum number of {{site.data.keyword.cos_full_notm}} subscriptions that you can have per project is 100. You are limited to a total of 100 cron subscriptions per project.  

For more information about limits for subscriptions, see [Limits and quotas for {[kn-service]}]({[url]}limits).

## Subscription logs
{: #ts-subscription-cos-logs}

You can retrieve the logs of the {{site.data.keyword.cos_short}} subscription for further debugging by using [{{site.data.keyword.la_full_notm}}](/docs/cloud-object-storage?topic=cloud-object-storage-mm-cos-integration) for log management capabilities.


