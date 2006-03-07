%include	/usr/lib/rpm/macros.php
%define		_class		Message
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - Message hash and digest (HMAC) generation methods and classes
Summary(pl):	%{_pearname} - klasy i metody do generowania skrótów (HMAC) wiadomo¶ci
Name:		php-pear-%{_pearname}
Version:	0.6
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d37e02108ecd6a90fc1e2c71cc875be7
URL:		http://pear.php.net/package/Message/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Classes for message hashing and HMAC signature generation using the
mhash functions.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasy do generowania skrótów i sygnatur HMAC wiadomo¶ci przy u¿yciu
funkcji mhash.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

install -d docs/%{_pearname}
mv ./%{php_pear_dir}/%{_class}/misc docs/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_pearname}
