
Name: app-user-dropbox-plugin
Epoch: 1
Version: 1.6.5
Release: 1%{dist}
Summary: Dropbox User Policy - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-user-dropbox-plugin-%{version}.tar.gz
Buildarch: noarch

%description
Dropbox plugin provides access control to allow users to create a home directory folder sync to the cloud-based Dropbox (http://www.dropbox.com) service.

%package core
Summary: Dropbox User Policy - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
Dropbox plugin provides access control to allow users to create a home directory folder sync to the cloud-based Dropbox (http://www.dropbox.com) service.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/user_dropbox_plugin
cp -r * %{buildroot}/usr/clearos/apps/user_dropbox_plugin/

install -D -m 0644 packaging/dropbox.php %{buildroot}/var/clearos/accounts/plugins/dropbox.php

%post core
logger -p local6.notice -t installer 'app-user-dropbox-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/user_dropbox_plugin/deploy/install ] && /usr/clearos/apps/user_dropbox_plugin/deploy/install
fi

[ -x /usr/clearos/apps/user_dropbox_plugin/deploy/upgrade ] && /usr/clearos/apps/user_dropbox_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-user-dropbox-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/user_dropbox_plugin/deploy/uninstall ] && /usr/clearos/apps/user_dropbox_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/user_dropbox_plugin/packaging
%dir /usr/clearos/apps/user_dropbox_plugin
/usr/clearos/apps/user_dropbox_plugin/deploy
/usr/clearos/apps/user_dropbox_plugin/language
/var/clearos/accounts/plugins/dropbox.php
