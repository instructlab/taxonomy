Biosbits is a software written by Josh Triplett that can be downloaded
from https://biosbits.org/. The github codebase can be found
[here](https://github.com/biosbits/bits/tree/master). It is a software that executes
the bios components such as acpi and smbios tables directly through acpica
bios interpreter (a freely available C based library written by Intel,
downloadable from https://acpica.org/ and is included with biosbits) without an
operating system getting involved in between.
There are several advantages to directly testing the bios in a real physical
machine or VM as opposed to indirectly discovering bios issues through the
operating system. For one thing, the OSes tend to hide bios problems from the
end user. The other is that we have more control of what we wanted to test
and how by directly using acpica interpreter on top of the bios on a running
system.
For QEMU, developers maintain a fork of bios bits in gitlab along with all the
dependent submodules in https://gitlab.com/qemu-project/biosbits-bits
This fork contains numerous fixes, a newer acpica and changes specific to
running this avocado QEMU tests using bits.
