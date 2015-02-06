%define upstream_name    WWW-Mechanize-FormFiller
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	WWW::Mechanize::FormFiller - framework to automate HTML forms
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/WWW/WWW-Mechanize-FormFiller-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(Data::Random)
BuildRequires:	perl(HTML::Form)
BuildRequires:	perl(HTML::TokeParser)
BuildRequires:	perl(Test::MockObject)
BuildRequires:	perl(Test::Inline)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/WWW/Mechanize/FormFiller
%dir %{perl_vendorlib}/WWW/Mechanize/FormFiller/Value
%dir %{perl_vendorlib}/WWW/Mechanize/FormFiller/Value/Random
%{perl_vendorlib}/WWW/Mechanize/FormFiller.pm
%{perl_vendorlib}/WWW/Mechanize/FormFiller/*.pm
%{perl_vendorlib}/WWW/Mechanize/FormFiller/Value/*.pm
%{perl_vendorlib}/WWW/Mechanize/FormFiller/Value/Random/*.pm
%{_mandir}/*/*

%changelog
* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 401916
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2010.0
+ Revision: 370247
- update to new version 0.10

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.08-4mdv2009.0
+ Revision: 258791
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.08-3mdv2009.0
+ Revision: 246712
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.08

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.06-1mdv2008.0
+ Revision: 20750
- 0.06


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-3mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-2mdk
- Fix BuildRequires

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.05-1mdk
- initial Mandriva package


