# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device oneplus3
%define vendor oneplus

%define vendor_pretty OnePlus
%define device_pretty OnePlus 3

%define installable_zip 1
%define droid_target_aarch64 1

# For OTA kernel update
%define enable_kernel_update 1

%define android_config \
#define WANT_ADRENO_QUIRKS 1 \
#define QCOM_BSP 1 \
%{nil}

%define straggler_files \
/init.qcom.sh\
/init.qcom.usb.sh\
/selinux_version\
/service_contexts\
/bugreports\
/d\
/file_contexts.bin\
/property_contexts\
/sdcard\
/vendor\
/cache\
%{nil}

%define makefstab_skip_entries /dev/cpuctl

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

