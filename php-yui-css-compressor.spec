# TODO
# - gui
# - cli tool
%define		php_min_version 5.0.0
%define		subver 10
%include	/usr/lib/rpm/macros.php
Summary:	A PHP port of the YUI CSS compressor
Name:		php-yui-css-compressor
Version:	4.1.0
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://github.com/tubalmartin/YUI-CSS-compressor-PHP-port/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0db7fd4a3af66b68df701317e7ed50b8
URL:		https://github.com/tubalmartin/YUI-CSS-compressor-PHP-port
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		appdir	%{php_data_dir}/tubalmartin/CssMin

%description
A PHP port of the YUI CSS compressor

This port is based on version 2.4.8 (Jun 12, 2013) of the YUI
compressor.

This port contains fixes & features not present in the original YUI
compressor.

%prep
%setup -q -n YUI-CSS-compressor-PHP-port-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{appdir}
cp -a src/* $RPM_BUILD_ROOT%{appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %(dirname %{appdir})
%{appdir}
