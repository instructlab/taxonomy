---

copyright:
  years: 2022, [{CURRENT_YEAR}]
lastupdated: "[{LAST_UPDATED_DATE}]"

keywords: troubleshooting for code engine toolchains, toolchain, tips for code engine and toolchain, help for toolchain and code engine, debugging toolchains for code engine

subcollection: {[subcollection]}

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Debugging your {[kn-service]} toolchain
{: #troubleshoot-toolchain-ce}
{: troubleshoot}

Use these tips to learn how to troubleshoot {{site.data.keyword.codeenginefull}} issues with toolchain.
{: shortdesc}

A toolchain is a set of tool integrations that support development, deployment, and operations tasks. Toolchains are part of {{site.data.keyword.cloud_notm}}'s {{site.data.keyword.contdelivery_short}} pipeline. You can set up a toolchain to automate the build and deployment of your {[kn-service]} workloads.

## Creating a debug log file for your pipeline
{: #troubleshoot-toolchain-ce-log}

You can create a debug log for your pipeline, which allows you to better understand what is happening with your toolchain. To create a debug log, start another pipeline run after you set the toolchain environment property `pipeline-debug` to `1` (`0` is the default). This property enables trace output in the log files and lists all files that are packaged. 

1. Open the **Overview** page for your toolchain.
2. Under **Delivery pipelines**, open your `ci-pipeline`.
3. Click **Environment properties**.
4. Find the `pipeline-debug` property and set it to `1`.
5. Start another pipeline run.
6. Find the log files.


## More information
{: #troubleshoot-toolchain-ce-info}

For more information about {{site.data.keyword.contdelivery_short}} and toolchain as well as finding troubleshooting information, see the following topics.
  
- [Integrating {[kn-service]} workloads with {{site.data.keyword.contdelivery_short}}]({[url]}toolchain-ce).
- [Getting help and support for {{site.data.keyword.contdelivery_short}}](/docs/ContinuousDelivery?topic=ContinuousDelivery-help-and-support).
- [FAQs for toolchain](/docs/ContinuousDelivery?topic=ContinuousDelivery-faq_toolchains).
- [Troubleshooting for toolchains](/docs/ContinuousDelivery?topic=ContinuousDelivery-troubleshoot-toolchains).
  

