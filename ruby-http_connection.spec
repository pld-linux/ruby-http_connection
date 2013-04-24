%define	gem_name http_connection
Summary:	RightScale's robust HTTP/S connection module
Name:		ruby-%{gem_name}
Version:	1.4.1
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/%{gem_name}-%{version}.gem
# Source0-md5:	5329fb3e933dbf7243c2ab08c5024b6b
URL:		https://github.com/appoxy/http_connection
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rightscale::HttpConnection is a robust HTTP(S) library. It implements
a retry algorithm for low-level network errors.

%prep
%setup -q -n %{gem_name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{ruby_vendorlibdir}/right_http_connection.rb
