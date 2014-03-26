# TODO
# - gui
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	A PHP port of the YUI CSS compressor
Name:		php-yui-css-compressor
Version:	2.4.8
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/tubalmartin/YUI-CSS-compressor-PHP-port/archive/v%{version}-2/%{name}-%{version}.tar.gz
# Source0-md5:	edc35670fab95ac0d08a80113b2c31a2
URL:		https://github.com/tubalmartin/YUI-CSS-compressor-PHP-port
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A PHP port of the YUI CSS compressor

This port is based on version 2.4.8 (Jun 12, 2013) of the YUI
compressor.

%prep
%setup -q -n YUI-CSS-compressor-PHP-port-%{version}-2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p cssmin.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/cssmin.php
