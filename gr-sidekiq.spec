%define debug_package %{nil}
Name:           gr-sidekiq
Version:        %{VERSION}
Release:        1%{?dist}
Summary:        GNU Radio Sidekiq Support
Group:          System Environment/Libraries
License:        Apache 2.0
URL:            https://github.com/epiqsolutions/gr-sidekiq
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gnuradio-devel
BuildRequires:  boost-devel
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++ 
BuildRequires:  cmake
Requires:       boost-filesystem
Requires:	boost-system

%description
GNU Radio Sidekiq Support

%prep
%setup -n %{name}-GNURADIO_v3.7__GR-SIDEKIQ_v%{version}

%build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc README.md
/usr/

%changelog
