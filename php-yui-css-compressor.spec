# TODO
# - gui
%define		php_min_version 5.0.0
%define		ver	2.4.8
%define		subver 4
%include	/usr/lib/rpm/macros.php
Summary:	A PHP port of the YUI CSS compressor
Name:		php-yui-css-compressor
Version:	%{ver}.%{subver}
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/tubalmartin/YUI-CSS-compressor-PHP-port/archive/v%{ver}-p%{subver}/%{name}-%{version}.tar.gz
# Source0-md5:	c146d844bcf8d1478e97e7d180939883
Patch0:		https://github.com/tubalmartin/YUI-CSS-compressor-PHP-port/pull/32.patch
# Patch0-md5:	bd22ac4208c2be134910723ae77c25b3
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
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -p cssmin.php $RPM_BUILD_ROOT%{php_data_dir}
ln -s cssmin.php $RPM_BUILD_ROOT%{php_data_dir}/CSSmin.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/cssmin.php
%{php_data_dir}/CSSmin.php
