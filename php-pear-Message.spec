%include	/usr/lib/rpm/macros.php
%define		_class		Message
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - Message hash and digest (HMAC) generation methods and classes
Summary(pl):	%{_pearname} - klasy i metody do generowania skrótów (HMAC) wiadomo¶ci
Name:		php-pear-%{_pearname}
Version:	0.6
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d37e02108ecd6a90fc1e2c71cc875be7
URL:		http://pear.php.net/package/Message/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Message/{HMAC,Hash}

install %{_pearname}-%{version}/*.php      $RPM_BUILD_ROOT%{php_pear_dir}/Message
install %{_pearname}-%{version}/HMAC/*.php $RPM_BUILD_ROOT%{php_pear_dir}/Message/HMAC
install %{_pearname}-%{version}/Hash/*.php $RPM_BUILD_ROOT%{php_pear_dir}/Message/Hash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{README,misc}
%{php_pear_dir}/%{_pearname}
