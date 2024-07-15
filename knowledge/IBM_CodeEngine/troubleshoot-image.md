---

copyright:
  years: 2023, [{CURRENT_YEAR}]
lastupdated: "[{LAST_UPDATED_DATE}]"

keywords: benefits, terminology, developers, capabilities, code engine

subcollection: {[subcollection]}

---

{{site.data.keyword.attribute-definition-list}}

# Debugging images
{: #troubleshoot-images} 
{: troubleshoot}

Use the troubleshooting tips to learn how to troubleshoot images. 
{: shortdesc}


## Working with images
{: #ts-image-workwith}

A build, or image build, is a mechanism that you can use to create a container image from your source code. 

{[defregistry.md]}

{[kn-service]} requires access to container registries to complete the following actions:
- To retrieve (or "pull") a container image to run an app or job
- To store a newly created container image as an output of an image build
- To store and retrieve local files when a build is run from local source

Whether your code exists as source in a local file or in a Git repository, or your code is a container image that exists in a public or private registry, {[kn-service]} provides you a streamlined way to run your code as an app or job.

When you want {[kn-service]} to handle the build process for you, {[kn-service]} can pull your source code and create the container image for you from your source code. {[kn-service]} supports building from a Dockerfile or Cloud Native Buildpacks. 

Consider the following points before you build your container image:

* Before you start building images, review [planning information]({[url]}plan-build). You'll also need to verify that you can access the registry. See [Setting up authorities for container registries]({[url]}add-registry#authorities-registry).

* If you build multiple versions of the same container image, the latest version of the container image is downloaded and used when you run your job or deploy your application, unless a tag is specified for the image. If a tag is specified for the image, then the tagged image is used for the app or job. 

* Build runs that are submitted with the CLI that do not reference a defined build configuration are not viewable from the console.

* {[kn-service]} has quotas for build runs within a project. For more information about {[kn-service]} limits, see [Limits and quotas for {[kn-service]}]({[url]}limits). 

Build runs that complete are ultimately automatically deleted. When you run a build run with a single CLI command such that it is not based on a build configuration, this build run is deleted after 1 hour if the build run is successful. If the build run is not successful, this build run is deleted after 24 hours. You can only display information about this build run with the CLI. You cannot view this build run in the console.
{: note}

For more details, see the following information.  

* [Planning to build container images]({[url]}plan-build).
* [Working with apps]({[url]}application-workloads)
* [Working with jobs and job runs]({[url]}job-plan)


## Getting logs for my images
{: #ts-images-logs}

Logs can be helpful to troubleshoot problems when you deploy applications, run jobs, or run builds to create images. 
{: shortdesc}

See the following topics for ways to get logs. 

* [Getting logs for builds]({[url]}troubleshoot-build#ts-build-gettinglogs).
* [Getting logs for apps]({[url]}troubleshoot-apps#ts-app-gettinglogs).
* [Getting logs for jobs]({[url]}troubleshoot-job#ts-jobrun-gettinglogs).


## Getting system event information for my images
{: #ts-images-systemevents}

System event information can be helpful to troubleshoot problems when you deploy applications, run jobs, or run builds to create images. 

See the following topics for ways to get system events. 

* [Getting system event information for builds]({[url]}troubleshoot-build#ts-build-gettingevent).
* [Getting system event information for apps]({[url]}troubleshoot-apps#ts-app-gettingevent).
* [Getting system event information for jobs]({[url]}troubleshoot-job#ts-job-gettingevent).







