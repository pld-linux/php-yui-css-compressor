# TODO
# - gui
%define		php_min_version 5.0.0
%define		ver	2.4.8
%define		subver 10
Summary:	A PHP port of the YUI CSS compressor
Name:		php-yui-css-compressor
Version:	%{ver}.%{subver}
Release:	4
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/tubalmartin/YUI-CSS-compressor-PHP-port/archive/v%{ver}-p%{subver}/%{name}-%{version}.tar.gz
# Source0-md5:	5013d0b1448cce1a001241d778c7c5f4
Patch0:		abspath.patch
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
%setup -q -n YUI-CSS-compressor-PHP-port-%{ver}-p%{subver}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/cssmin
ln -s cssmin/cssmin.php $RPM_BUILD_ROOT%{php_data_dir}/cssmin.php
ln -s cssmin/cssmin.php $RPM_BUILD_ROOT%{php_data_dir}/CSSmin.php
cp -a cssmin.php data $RPM_BUILD_ROOT%{php_data_dir}/cssmin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/cssmin.php
%{php_data_dir}/CSSmin.php
%{php_data_dir}/cssmin
