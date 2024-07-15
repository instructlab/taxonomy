---

copyright:
  years: 2020, [{CURRENT_YEAR}]
lastupdated: "[{LAST_UPDATED_DATE}]"

keywords: troubleshooting for code engine, troubleshooting builds in code engine, tips for builds in code engine, resolution of builds in code engine, builds

subcollection: {[subcollection]}

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Debugging builds 
{: #troubleshoot-build}
{: troubleshoot}

Use the troubleshooting tips to learn how to troubleshoot {{site.data.keyword.codeenginefull}} builds and runs of your build.
{: shortdesc}

{[note-ts-build-fail-beforebegin.md]} 

When your build isn't behaving as expected, looking at logs and system events can provide information that might help you debug the problem. 

## Build limits to consider 
{: #ts-build-limits}

The maximum number of build configurations that you can have per project is 100. You are limited to a total of 100 build runs per project before you need to remove or clean up old ones.

For more information about limits for builds including memory and CPU, see [Limits and quotas for {[kn-service]}]({[url]}limits).

{[note-project-limits-example.md]}

## Getting logs for my builds
{: #ts-build-gettinglogs}

Logs can be helpful to troubleshoot problems when you run builds. You can view logs for builds with the CLI or the console. 
{: shortdesc}

### Getting logs for my builds from the console
{: #ts-build-gettinglogs-ui}

You can display logs for specific build run instances from the console. 
{: shortdesc}

1. Go to the [{{site.data.keyword.codeengineshort}} dashboard]({[dashboard]}).
2. Select a project (or [create one]({[url]}manage-project#create-a-project)).
3. From the project page, click **Image builds**.
4. From the **Image build** tab, click the name of your image build to open the build page for a defined build, or [create a build]({[url]}build-create-config1#build-create-console).
5. From the build page for your defined build, click the name of the instance of your build run in the **Build runs** section. You might need to click **Submit build** to create a build run.  
6. From the build run instance page, you can view the build log information. Expand the specific build steps for detailed logging information.

For more information, see [viewing build logs from the console]({[url]}view-logs#view-build-ui).

### Getting logs for my builds with the CLI
{: #ts-build-gettinglogs-cli}

Use the [**`{[ickn]} buildrun logs`**]({[url]}cli#cli-buildrun-logs) command to display logs about the build run. Use this command to display logs of all the instances of a build run based on the name of the build run.

To view the logs for all instances of the `mybuildrun` build run, specify the name of the build run with the `--name` option; for example,  

```txt
{[ickn]} buildrun logs --name mybuildrun
```
{: pre}

Example output

```txt
Getting build run 'mybuildrun'...
Getting instances of build run 'mybuildrun'...
Getting logs for build run 'mybuildrun'...
OK

mybuildrun-bvzbg-pod-tppvg/step-source-default:
2021/09/21 09:39:08 Info: ssh (/usr/bin/ssh): OpenSSH_8.0p1, OpenSSL 1.1.1g FIPS  21 Apr 2020
2021/09/21 09:39:08 Info: git (/usr/bin/git): git version 2.27.0
2021/09/21 09:39:08 Info: git-lfs (/usr/bin/git-lfs): git-lfs/2.11.0 (GitHub; linux amd64; go 1.14.4)
2021/09/21 09:39:08 /usr/bin/git clone --quiet --no-tags --branch main --depth 1 --single-branch -- https://github.com/IBM/CodeEngine /workspace/source
2021/09/21 09:39:09 /usr/bin/git -C /workspace/source submodule update --init --recursive --depth 1
2021/09/21 09:39:10 /usr/bin/git -C /workspace/source rev-parse --abbrev-ref HEAD
2021/09/21 09:39:10 Successfully loaded https://github.com/IBM/CodeEngine (main) into /workspace/source
2021/09/21 09:39:10 /usr/bin/git -C /workspace/source rev-parse --verify HEAD

mybuildrun-bvzbg-pod-tppvg/step-build-and-push:
INFO[0000] Retrieving image manifest golang:alpine
INFO[0000] Retrieving image golang:alpine from registry index.docker.io
INFO[0001] Retrieving image manifest alpine
INFO[0001] Retrieving image alpine from registry index.docker.io
INFO[0003] Built cross stage deps: map[0:[/codeengine]]
INFO[0003] Retrieving image manifest golang:alpine
INFO[0003] Returning cached image manifest
INFO[0003] Executing 0 build triggers
INFO[0003] Unpacking rootfs as cmd COPY ./helloworld /helloworld requires it.
INFO[0009] COPY ./helloworld /helloworld
INFO[0009] Taking snapshot of files...
INFO[0009] COPY codeengine.go /
INFO[0009] Taking snapshot of files...
INFO[0009] RUN go build -o /codeengine /codeengine.go
INFO[0009] Taking snapshot of full filesystem...
INFO[0017] cmd: /bin/sh
INFO[0017] args: [-c go build -o /codeengine /codeengine.go]
INFO[0017] Running: [/bin/sh -c go build -o /codeengine /codeengine.go]
INFO[0018] Taking snapshot of full filesystem...
INFO[0018] Saving file codeengine for later use
INFO[0018] Deleting filesystem...
INFO[0019] Retrieving image manifest alpine
INFO[0019] Returning cached image manifest
INFO[0019] Executing 0 build triggers
INFO[0019] Unpacking rootfs as cmd COPY --from=0 /codeengine /codeengine requires it.
INFO[0019] COPY --from=0 /codeengine /codeengine
INFO[0019] Taking snapshot of files...
INFO[0019] CMD /codeengine
INFO[0019] Pushing image to us.icr.io/acme-namespace/codeengine-sample
INFO[0023] Pushed image to 1 destinations
```
{: screen}

## Getting system event information for my builds
{: #ts-build-gettingevent}

System event information can be helpful to troubleshoot problems when you run builds. You can view system event information for builds with the CLI. 
{: shortdesc}

1. Use the [**`{[ickn]} buildrun list`**]({[url]}cli#cli-buildrun-list) command to list all your build runs in a project; for example,

    ```txt
    {[ickn]} buildrun list  
    ```
    {: pre}

2. Use the [**`{[ickn]} buildrun get`**]({[url]}cli#cli-buildrun-get) command to get the details of your a build run, for example,

    ```txt
    {[ickn]} buildrun get --name mybuildrun  
    ```
    {: pre}

    Example output 

    ```txt
    Getting build run 'mybuildrun'...
    Run 'ibmcloud ce buildrun events -n mybuildrun' to get the system events of the build run.
    Run 'ibmcloud ce buildrun logs -f -n mybuildrun' to follow the logs of the build run.
    OK

    Name:          mybuilddrun
    [...]

    Created:       2021-06-01T11:43:24-04:00

    Summary:  Succeeded
    Status:   Succeeded
    Reason:   All Steps have completed executing

    Image:  us.icr.io/mynamespace/codeengine-codeengine-200
    ```
    {: screen}

    If you want more fine-grained details about your build run, use the `--o yaml` option with the **`buildrun get`** command; for example, `{[ickn]} buildrun get --name myapp --o yaml`. This option is useful to show more detailed information in the CLI for the build run.
    {: tip}

3. Display the system events of your build run. Use the [**`{[ickn]} buildrun events`**]({[url]}cli#cli-buildrun-events) command; for example,

    ```txt
    {[ickn]} buildrun events --name mybuildrun 
    ```
    {: pre} 

    Example output 

    ```txt
    Getting build run 'mybuildrun'...
    Getting instances of build run 'mybuildrun'...
    Getting events for build run 'mybuildrun'...
    OK

    mybuildrun-bvzbg-pod-tppvg:
        Type    Reason     Age    Source                Messages
        Normal  Scheduled  4m43s  default-scheduler     Successfully assigned 62ckpsxlh7x/mybuildrun-bvzbg-pod-tppvg to 10.242.0.17
        Normal  Pulled     4m42s  kubelet, 10.242.0.17  Container image "icr.io/obs/codeengine/tekton-pipeline/entrypoint-bff0a22da108bc2f16c818c97641a296:v0.23.0-rc6@sha256:43dd56a6c7c10f80300a861615f6f8d91c026deba744f81553a4e536b301b322" already present on machine
        Normal  Created    4m42s  kubelet, 10.242.0.17  Created container place-tools
        Normal  Started    4m41s  kubelet, 10.242.0.17  Started container place-tools
        Normal  Pulled     4m40s  kubelet, 10.242.0.17  Container image "icr.io/obs/codeengine/git:v0.8.100" already present on machine
        Normal  Created    4m40s  kubelet, 10.242.0.17  Created container step-source-default
        Normal  Started    4m40s  kubelet, 10.242.0.17  Started container step-source-default
        Normal  Pulled     4m40s  kubelet, 10.242.0.17  Container image "icr.io/obs/codeengine/buildkit/builder:v0.9.0-rc.19" already present on machine
        Normal  Created    4m40s  kubelet, 10.242.0.17  Created container step-build-and-push
        Normal  Started    4m40s  kubelet, 10.242.0.17  Started container step-build-and-push
    ```
    {: screen}

    Events are only stored for one hour in the system.
    {: tip}


