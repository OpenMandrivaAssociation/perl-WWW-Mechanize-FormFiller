%define upstream_name    WWW-Mechanize-FormFiller
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	WWW::Mechanize::FormFiller - framework to automate HTML forms
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Data::Random)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Test::Inline)
BuildRequires:  perl-libwww-perl
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
WWW::Mechanize::FormFiller and its submodules are useful to automate
web forms. The FormFiller object is filled with a set of rules how to
fill out HTML form field and then let loose on a HTML form. It fills
in the fields according to the preset rules.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# pod2test is gone in perl-Test-Inline
perl -pi -e "s|pod2test|/bin/true|g" Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/WWW/Mechanize/FormFiller
%dir %{perl_vendorlib}/WWW/Mechanize/FormFiller/Value
%dir %{perl_vendorlib}/WWW/Mechanize/FormFiller/Value/Random
%{perl_vendorlib}/WWW/Mechanize/FormFiller.pm
%{perl_vendorlib}/WWW/Mechanize/FormFiller/*.pm
%{perl_vendorlib}/WWW/Mechanize/FormFiller/Value/*.pm
%{perl_vendorlib}/WWW/Mechanize/FormFiller/Value/Random/*.pm
%{_mandir}/*/*
