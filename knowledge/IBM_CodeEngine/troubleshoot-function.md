---

copyright:
  years: 2023, [{CURRENT_YEAR}]
lastupdated: "[{LAST_UPDATED_DATE}]"

keywords: troubleshooting for code engine, troubleshooting functions in code engine, function in code engine, function

subcollection: {[subcollection]}

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Debugging functions
{: #troubleshoot-function}
{: troubleshoot}

Use the troubleshooting tips to learn how to troubleshoot {{site.data.keyword.codeenginefull}} functions.
{: shortdesc}

## Function limits to consider 
{: #ts-function-limits}

When you create functions, you must consider the [Function limits]({[url]}limits#limits_functions).

{[resourcequota.md]}

{[note-project-limits-example.md]}


## Getting logs for my function 
{: #ts-funcrtion-gettinglogs}

Logs can be helpful to troubleshoot problems when you run functions. You can view function logs from the console. 
{: shortdesc}

When you view logs from the console, you must create an {{site.data.keyword.la_full_notm}} instance in the same region as your {[kn-service]} project. You are not required to create this instance before you work with your {[kn-service]} function. {[kn-service]} makes it easy to enable logging for your functions. You can view function logs after you add logging capabilities. For more information, see [viewing function logs from the console]({[url]}view-logs#view-funlogs-ui).

## Keep your runtime and CLI versions up to date
{: #ts-function-uptodate}

Verify that your runtime is supported. See [Runtimes]({[url]}fun-runtime).

## Verifying the code bundle reference for my function 
{: #ts-function-verifyimage}

{[defcodebundle.md]}    ``
  
When you work with {[kn-service]} functions, you must specify a code bundle reference and a registry secret to access the image. For the function to work correctly, the code bundle reference and its access properties must remain valid for the life of the function.

Because code bundles and images are similar, you can verify your code bundle in the same ways that you verify an image. See [How can I verify my image reference]({[url]}ts-build-verify-image)?


## Additional topics
{: #ts-function-topics}

You can find more help in the following topics.

- [Troubleshooting overview]({[url]}troubleshooting_over).
- [Debugging builds]({[url]}troubleshoot-build).

