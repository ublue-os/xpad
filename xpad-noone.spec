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

%build

%files
%doc xpad-noone-master/README.md
%license xpad-noone-master/LICENSE

%changelog
{{{ git_dir_changelog }}}
