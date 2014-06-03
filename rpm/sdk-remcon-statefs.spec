Name:       sdk-remcon-statefs

Summary:    Create interface between remcon widget and emulator
Version:    0.1
Release:    1
Group:      Qt/Qt
License:    TBD
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch

%description
%{Summary}.


%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp -a sdk-remcon-statefs.sh %{buildroot}%{_bindir}
mkdir -p %{buildroot}/lib/systemd/system/multi-user.target.wants
cp -a sdk-remcon-statefs.service %{buildroot}/lib/systemd/system
ln -s .. %{buildroot}/lib/systemd/system/multi-user.target.wants/sdk-remcon-statefs.service

%files
%defattr(-,root,root,-)
%{_bindir}/sdk-remcon-statefs.sh
/lib/systemd/system/sdk-remcon-statefs.service
/lib/systemd/system/multi-user.target.wants/sdk-remcon-statefs.service

