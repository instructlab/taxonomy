In the ever-demanding world of virtualized environments, storage performance plays a critical role. Traditional storage solutions can become bottlenecks, hindering application responsiveness and overall system performance. This is where NVMe-oF (NVMe over Fabrics) shines, offering significantly lower latency and higher bandwidth compared to conventional storage protocols.

This blog post guides you through configuring a VMware ESXi host (version 7.0U3 or later) as an NVMe-oF initiator to leverage the power of a Ceph NVMe-oF gateway. By following these steps, you can unlock the potential of NVMe-oF and experience a noticeable boost in your virtualized storage performance.

Prerequisites

Before diving in, ensure you have the following in place:

An ESXi host running VMware vSphere Hypervisor (ESXi) 7.0U3 or later

A deployed Ceph NVMe-oF gateway

A functional IBM Storage Ceph cluster with properly configured ceph-nvmeof settings

A defined subsystem within the gateway (refer to specific documentation for "Defining an NVMe-oF subsystem")

A configured NVMe/TCP adapter with NVMe/TCP enabled on a physical NIC (use the command esxcli nvme fabrics enable --protocol TCP --device vmnicN - replace N with the NIC number)

A VMkernel NIC tagged to permit NVMe/TCP traffic (use the command esxcli network ip interface tag add --interface-name vmkN --tagname NVMeTCP - replace N with the VMkernel ID)







Configuration Steps

1. List NVMe-oF Adapter:
Use the following command to view information about available NVMe-oF adapters on your ESXi host:

esxcli nvme adapter list

This will provide details like adapter name, transport type, and associated devices.

2. (Optional) Discover NVMe-oF Subsystems:
This step is optional if you only want to discover available NVMe-oF subsystems without establishing a connection. Use the following command, replacing placeholders with your specific details:

esxcli nvme fabrics discover -a NVME_TCP_ADAPTER -i GATEWAY_IP -p 8009

NVME_TCP_ADAPTER: Replace with the adapter name obtained in step 1.

GATEWAY_IP: Replace with the IP address of your NVMe-oF gateway.

8009: Replace with the discovery port if it differs from the default (8009).

3. Connect to NVMe-oF Gateway Subsystem:
To discover and connect to the NVMe-oF gateways in the gateway group, use this command:


esxcli nvme fabrics discover -a NVME_TCP_ADAPTER -i GATEWAY_IP -p 8009 -c

Replace placeholders as mentioned in step 2.

4. Alternatively, for a specific connection:
If you want to connect to a particular subsystem identified by its NQN (name), use this command:


esxcli nvme fabrics connect -a NVME_TCP_ADAPTER -i GATEWAY_IP -s SUBSYSTEM_NQN -p 8009


Replace placeholders with your specific details, including the SUBSYSTEM_NQN.

5. Verify Connection:
Run the following command to check if the connection is established successfully. Look for "true" under the "Connected" column:


esxcli nvme controller list |grep TCP

 

6. List NVMe/TCP Controllers:
To view a list of NVMe/TCP controllers discovered on your ESXi host, use this command:


esxcli nvme controller list


This will display information like controller name, adapter, transport type, and online status.

7. List NVMe-oF Namespaces:
Finally, use this command to see the available NVMe-oF namespaces within the connected subsystem:


esxcli nvme namespace list


This will provide details like namespace name, controller number, block size, and capacity.

8. Verification in vSphere Client:

Once you've completed the configuration steps, navigate to the ESXi host in your vSphere Client. Go to the "Storage" page and then the "Devices" tab. If the NVMe-oF initiator is configured correctly, you should see the NVMe/TCP disks listed in the table.