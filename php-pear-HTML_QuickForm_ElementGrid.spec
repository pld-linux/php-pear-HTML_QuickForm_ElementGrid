%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	HTML_QuickForm_ElementGrid
Summary:	%{_pearname} - HTML_QuickForm meta-element which holds any other element in a grid
Summary(pl.UTF-8):	%{_pearname} - metaelement HTML_QuickForm przechowujący inny element tabeli danych
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	46771abf9ee78fce0b78cef7aefddc14
URL:		http://pear.php.net/package/HTML_QuickForm_ElementGrid/
BuildRequires:	php-pear-PEAR >= 1:1.4.3
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-HTML_QuickForm >= 3.2.5
Requires:	php-pear-HTML_Table >= 1.7.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An HTML_QuickForm meta-element which holds multiple HTML_QuickForm
elements in an HTML_Table. The elements in the table should behave
exactly like normal elements in a form, such as freezing and getting
defaults and submitted values correctly.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa ta dostarcza metaelementu przechowującego wiele elementów
HTML_QuickForm w tabeli HTML_Table. Elementy tej tabeli zachowują się
identycznie jak typowe elementy formularza - można je "zamrozić" oraz
pobrać domyślne jak i wysłane wartości.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/HTML_QuickForm_ElementGrid/examples/elementGrid.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTML/QuickForm/ElementGrid.php
