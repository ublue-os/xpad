%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     xpad-noone
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Linux Kernel Driver for the Xbox/ Xbox 360 Controllers
License:  GPLv2
URL:      https://github.com/ublue-os/xpad-noone

Source:   %{url}/archive/refs/heads/master.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Linux Kernel Driver for the Xbox/ Xbox 360 Controllers

%prep
%setup -q -c xpad-noone-master

%install
install -D -m 0644 xpad-noone-master/xpad-noone-blacklist.conf %{buildroot}%{_modprobedir}/xpad-noone-blacklist.conf
install -D -m 0644 xpad-noone-master/xpad-noone.conf %{buildroot}%{_modulesloaddir}/xpad-noone.conf

%files
%doc xpad-noone-master/README.md
%license xpad-noone-master/LICENSE
%{_modprobedir}/xpad-noone-blacklist.conf
%{_modulesloaddir}/xpad-noone.conf

%changelog
{{{ git_dir_changelog }}}
