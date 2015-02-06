%define upstream_name    Module-Install-Repository
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Automatically sets repository URL from svn/svk/Git checkout
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.lzma

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Filter::Util::Call)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Module::Install::Repository is a Module::Install plugin to automatically
figure out repository URL and set it via _repository()_ which then will be
added to resources under _META.yml_.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.60.0-3mdv2011.0
+ Revision: 657793
- rebuild for updated spec-helper

* Sat Sep 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 580971
- import perl-Module-Install-Repository

