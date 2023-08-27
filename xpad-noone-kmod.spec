%if 0%{?fedora}
%global buildforkernels akmod
%global debug_package %{nil}
%endif

Name:     xpad-noone-kmod
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Linux Kernel Driver for the Xbox/ Xbox 360 Controllers
License:  GPLv2
URL:      https://github.com/ublue-os/xpad-noone

Source:   %{url}/archive/refs/heads/master.tar.gz

BuildRequires: kmodtool
BuildRequires: sed

%{expand:%(kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Linux Kernel Driver for the Xbox/ Xbox 360 Controllers

%prep
# error out if there was something wrong with kmodtool
%{?kmodtool_check}

# print kmodtool output for debugging purposes:
kmodtool --target %{_target_cpu} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c xpad-noone-master

find . -type f -name '*.c' -exec sed -i "s/#VERSION#/%{version}/" {} \+

for kernel_version  in %{?kernel_versions} ; do
  cp -a xpad-noone-master _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version  in %{?kernel_versions} ; do
  make V=1 %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} VERSION=v%{version} modules
done

%install
for kernel_version in %{?kernel_versions}; do
 mkdir -p %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 install -D -m 755 _kmod_build_${kernel_version%%___*}/xpad-noone.ko %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/
 chmod a+x %{buildroot}%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix}/xpad-noone.ko
done
%{?akmod_install}

%changelog
{{{ git_dir_changelog }}}
