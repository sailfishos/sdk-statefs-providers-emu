Name:       sdk-statefs-providers-emu

Summary:    Emulation of multiple statefs properties
Version:    0.1
Release:    1
Group:      Qt/Qt
License:    BSD
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch

%description
%{Summary}. Licensed under the New BSD License (BSD-new).


%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp -a sdk-statefs-providers-emu.sh %{buildroot}%{_bindir}
mkdir -p %{buildroot}/lib/systemd/system/multi-user.target.wants
cp -a sdk-statefs-providers-emu.service %{buildroot}/lib/systemd/system
ln -s .. %{buildroot}/lib/systemd/system/multi-user.target.wants/sdk-statefs-providers-emu.service

%files
%defattr(-,root,root,-)
%{_bindir}/sdk-statefs-providers-emu.sh
/lib/systemd/system/sdk-statefs-providers-emu.service
/lib/systemd/system/multi-user.target.wants/sdk-statefs-providers-emu.service

