---

copyright:
  years: 2020, [{CURRENT_YEAR}]
lastupdated: "[{LAST_UPDATED_DATE}]"

keywords: troubleshooting for code engine, troubleshooting jobs in code engine, troubleshooting batch jobs in code engine, job run troubleshooting in code engine, job troubleshooting in code engine, job, job run

subcollection: {[subcollection]}

content-type: troubleshoot

---

{{site.data.keyword.attribute-definition-list}}

# Debugging jobs
{: #troubleshoot-job}
{: troubleshoot}

Use the troubleshooting tips to learn how to troubleshoot {{site.data.keyword.codeenginefull}} jobs and runs of your job.
{: shortdesc}

## Job limits to consider 
{: #ts-job-limits}

The maximum number of jobs that you can have per project is 100. You are limited to a total of 100 job runs per project before you need to remove or clean up old ones. 

For more information about limits for jobs including memory and CPU, see [Limits and quotas for {[kn-service]}]({[url]}limits).

{[note-project-limits-example.md]}

## Getting logs for my jobs 
{: #ts-jobrun-gettinglogs}

Logs can be helpful to troubleshoot problems when you run jobs. You can view job logs from the console or with the CLI. 
{: shortdesc}

When you view logs from the console, you must create an {{site.data.keyword.la_full_notm}} instance in the same region as your {[kn-service]} project. You are not required to create this instance before you work with your {[kn-service]} job. {[kn-service]} makes it easy to enable logging for your jobs. You can view job logs after you add logging capabilities. For more information, see [viewing job logs from the console]({[url]}view-logs#view-joblogs-ui).

When working with the CLI, you can display logs of all the instances of your running job or display logs of a specific instance of your job. 

1. Use the [**`{[ickn]} jobrun list`**]({[url]}cli#cli-jobrun-list) command to list all your defined job runs; for example,

    ```txt
    {[ickn]} jobrun list  
    ```
    {: pre}

2. Use the [**`{[ickn]} jobrun get`**]({[url]}cli#cli-jobrun-get) command to get the details of your job run, including the name of the instances for the job run; for example,

    ```txt
    {[ickn]} jobrun get --name myjobrun 
    ```
    {: pre}

    Example output 

    ```txt
    Getting jobrun 'myjobrun'...
    Getting instances of jobrun 'myjobrun'...
    Getting events of jobrun 'myjobrun'...
    Run 'ibmcloud ce jobrun events -n myjobrun' to get the system events of the job run instances.
    Run 'ibmcloud ce jobrun logs -f -n myjobrun' to follow the logs of the job run instances.
    OK

    Name:          myjobrun
    [...]
    Created:       2021-03-03T14:47:04-05:00

    Image:                icr.io/codeengine/firstjob
    Resource Allocation:
        CPU:                1
        Ephemeral Storage:  400M
        Memory:             4G

    Runtime:
        Mode:                  task
        Array Indices:         1 - 4
        Array Size:            4
        JOP_ARRAY_SIZE Value:  4
        Max Execution Time:    7200
        Retry Limit:           3

    Status:
        Completed:          28m
        Instance Statuses:
        Succeeded:  4
        Conditions:
        Type      Status  Last Probe  Last Transition
        Pending   True    28m         28m
        Running   True    28m         28m
        Complete  True    28m         28m

    Events:
        Type    Reason     Age                Source                Messages
        Normal  Updated    29m (x8 over 29m)  batch-job-controller  Updated JobRun "myjobrun"
        Normal  Completed  29m                batch-job-controller  JobRun completed successfully

    Instances:
        Name          Running  Status     Restarts  Age
        myjobrun-1-0  0/1      Succeeded  0         29m
        myjobrun-2-0  0/1      Succeeded  0         29m
        myjobrun-3-0  0/1      Succeeded  0         29m
        myjobrun-4-0  0/1      Succeeded  0         29m
    ```
    {: screen}

    If you want more fine-grained details about your job run, use the `--o yaml` option with the **`jobrun get`** command; for example, `{[ickn]} jobrun get --name myjobrun --o yaml`. This option is useful to show more detailed information in the CLI for the job run.
    {: tip}


3. Display the logs of instances of your job run. 

    * To display the logs of a specific instance of your job run, use the [**`{[ickn]} jobrun logs --instance INSTANCE_NAME`**]({[url]}cli#cli-jobrun-logs) command; for example,

        ```txt
        {[ickn]} jobrun logs --instance  myjobrun-4-0
        ```
        {: pre} 

        Example output 

        ```txt
        Getting logs for job run instance 'myjobrun-4-0'...
        OK

        myjobrun-4-0/myjobrun:
        Hi from a batch job! My index is: 4
        ```
        {: screen}

    * To display the logs of all the instances of your job run, use the [**`{[ickn]} jobrun logs --jobrun JOBRUN_NAME`**]({[url]}cli#cli-jobrun-logs) command; for example,

        ```txt
        {[ickn]} jobrun logs --jobrun myjobrun 
        ```
        {: pre} 

        Example output 

        ```txt
        Getting logs for all instances of job run 'myjobrun'...
        Getting jobrun 'myjobrun'...
        Getting instances of jobrun 'myjobrun'...
        OK

        myjobrun-1-0/myjobrun:
        Hi from a batch job! My index is: 1

        myjobrun-2-0/myjobrun:
        Hi from a batch job! My index is: 2

        myjobrun-3-0/myjobrun:
        Hi from a batch job! My index is: 3

        myjobrun-4-0/myjobrun:
        Hi from a batch job! My index is: 4
        ```
        {: screen}

For more information, see [Viewing job logs with the CLI]({[url]}view-logs#view-joblog-cli).

## Getting system event information for my jobs 
{: #ts-job-gettingevent}

System event information can be helpful to troubleshoot problems when you run jobs. You can view system event information with the CLI.
{: shortdesc}

You can display system events of all the instances of a job run or display system events of a specific instance of a job run. 

1. Use the [**`{[ickn]} jobrun list`**]({[url]}cli#cli-jobrun-list) command to list all your defined job runs; for example,

    ```txt
    {[ickn]} jobrun list  
    ```
    {: pre}

2. Use the [**`{[ickn]} jobrun get`**]({[url]}cli#cli-jobrun-get) command to get the details of your job run, including the name of the instances of the job run; for example,

    ```txt
    {[ickn]} jobrun get --name myjobrun 
    ```
    {: pre}

    Example output 

    ```txt
    Getting jobrun 'myjobrun'...
    Getting instances of jobrun 'myjobrun'...
    Getting events of jobrun 'myjobrun'...
    OK

    Name:          myjobrun
    [...]
    Created:       2021-03-03T14:47:04-05:00

    Image:                icr.io/codeengine/firstjob
    Resource Allocation:
        CPU:                1
        Ephemeral Storage:  400M
        Memory:             4G

    Runtime:
        Mode:                  task
        Array Indices:         1 - 4
        Array Size:            4
        JOP_ARRAY_SIZE Value:  4
        Max Execution Time:    7200
        Retry Limit:           3

    Status:
        Completed:          28m
        Instance Statuses:
        Succeeded:  4
        Conditions:
        Type      Status  Last Probe  Last Transition
        Pending   True    28m         28m
        Running   True    28m         28m
        Complete  True    28m         28m

    Events:
        Type    Reason     Age                Source                Messages
        Normal  Updated    29m (x8 over 29m)  batch-job-controller  Updated JobRun "myjobrun"
        Normal  Completed  29m                batch-job-controller  JobRun completed successfully

    Instances:
        Name          Running  Status     Restarts  Age
        myjobrun-1-0  0/1      Succeeded  0         29m
        myjobrun-2-0  0/1      Succeeded  0         29m
        myjobrun-3-0  0/1      Succeeded  0         29m
        myjobrun-4-0  0/1      Succeeded  0         29m
    ```
    {: screen}

    If you want more fine-grained details about your job run, use the `--o yaml` option with the **`jobrun get`** command; for example, `{[ickn]} jobrun get --name myjobrun --o yaml`. This option is useful to show more detailed information in the CLI for the job run.
    {: tip}

3. Display the system events of instances of your job run.  

    * To display the events of a specific instance of your job run, use the [**`{[ickn]} jobrun events --instance INSTANCE_NAME`**]({[url]}cli#cli-jobrun-events) command; for example,

        ```txt
        {[ickn]} jobrun events --instance myjobrun-4-0 
        ```
        {: pre} 

        Example output 

        ```txt
        Getting events for job run instance 'myjobrun-4-0'...
        OK

        myjobrun-4-0:
        Type    Reason     Age    Source                 Messages
        Normal  Scheduled  2m14s  default-scheduler      Successfully assigned 4svg40kna19/myjobrun-4-0 to 10.240.64.10
        Normal  Pulling    2m13s  kubelet, 10.240.64.10  Pulling image "icr.io/codeengine/firstjob"
        Normal  Pulled     2m12s  kubelet, 10.240.64.10  Successfully pulled image "icr.io/codeengine/firstjob" in 1.234456436s
        Normal  Created    2m11s  kubelet, 10.240.64.10  Created container myjobrun
        Normal  Started    2m11s  kubelet, 10.240.64.10  Started container myjobrun
        ```
        {: screen}

    * To display events of all the instances of your job run, use the [**`{[ickn]} jobrun events --jobrun JUBRUN_NAME`**]({[url]}cli#cli-jobrun-events) command; for example,

        ```txt
        {[ickn]} jobrun events --jobrun myjobrun 
        ```
        {: pre} 

        Example output 

        ```txt
        Getting jobrun 'myjobrun'...
        Getting instances of jobrun 'myjobrun'...
        Getting events for all instances of job run 'myjobrun'...
        OK

        myjobrun-1-0:
        Type    Reason     Age  Source                  Messages
        Normal  Scheduled  66s  default-scheduler       Successfully assigned 4svg40kna19/myjobrun-1-0 to 10.240.128.22
        Normal  Pulling    65s  kubelet, 10.240.128.22  Pulling image "icr.io/codeengine/firstjob"
        Normal  Pulled     64s  kubelet, 10.240.128.22  Successfully pulled image "icr.io/codeengine/firstjob" in 427.276949ms
        Normal  Created    64s  kubelet, 10.240.128.22  Created container myjobrun
        Normal  Started    64s  kubelet, 10.240.128.22  Started container myjobrun

        myjobrun-2-0:
        Type    Reason     Age  Source                Messages
        Normal  Scheduled  66s  default-scheduler     Successfully assigned 4svg40kna19/myjobrun-2-0 to 10.240.0.11
        Normal  Pulling    65s  kubelet, 10.240.0.11  Pulling image "icr.io/codeengine/firstjob"
        Normal  Pulled     63s  kubelet, 10.240.0.11  Successfully pulled image "icr.io/codeengine/firstjob" in 1.268252989s
        Normal  Created    63s  kubelet, 10.240.0.11  Created container myjobrun
        Normal  Started    63s  kubelet, 10.240.0.11  Started container myjobrun

        myjobrun-3-0:
        Type    Reason     Age  Source                Messages
        Normal  Scheduled  66s  default-scheduler     Successfully assigned 4svg40kna19/myjobrun-3-0 to 10.240.0.37
        Normal  Pulling    65s  kubelet, 10.240.0.37  Pulling image "icr.io/codeengine/firstjob"
        Normal  Pulled     63s  kubelet, 10.240.0.37  Successfully pulled image "icr.io/codeengine/firstjob" in 1.118647987s
        Normal  Created    63s  kubelet, 10.240.0.37  Created container myjobrun
        Normal  Started    63s  kubelet, 10.240.0.37  Started container myjobrun

        myjobrun-4-0:
        Type    Reason     Age  Source                 Messages
        Normal  Scheduled  66s  default-scheduler      Successfully assigned 4svg40kna19/myjobrun-4-0 to 10.240.64.10
        Normal  Pulling    65s  kubelet, 10.240.64.10  Pulling image "icr.io/codeengine/firstjob"
        Normal  Pulled     64s  kubelet, 10.240.64.10  Successfully pulled image "icr.io/codeengine/firstjob" in 1.234456436s
        Normal  Created    63s  kubelet, 10.240.64.10  Created container myjobrun
        Normal  Started    63s  kubelet, 10.240.64.10  Started container myjobrun
        ```
        {: screen}

## Verifying the container image reference for my job 
{: #ts-jobrun-verifyimage}

When you work with {[kn-service]} jobs, you must specify a container image reference and a registry secret to access the image. For the job to work correctly, the image reference and its access properties must remain valid for the life of the job. 

See [How can I verify my image reference]({[url]}ts-build-verify-image)?



