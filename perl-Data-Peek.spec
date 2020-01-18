Name:           perl-Data-Peek
Version:        0.38
Release:        3%{?dist}
Summary:        Collection of low-level debug facilities
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Peek/
Source0:        http://www.cpan.org/authors/id/H/HM/HMBRAND/Data-Peek-%{version}.tgz
# automatically create also DP.pm as alias of Data-Peek
Patch0:         Data-Peek-0.33.patch
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Data::Peek started off as DDumper being a wrapper module over Data::Dumper,
but grew out to be a set of low-level data introspection utilities that no
other module provided yet, using the lowest level of the perl internals API
as possible.

%prep
%setup -q -n Data-Peek-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{perl_vendorarch}/DP.pm
%{_mandir}/man3/*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.38-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.38-2
- Mass rebuild 2013-12-27

* Fri Oct 19 2012 Marcela Mašláňová <mmaslano@redhat.com> 0.38-1
- Update to 0.38

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 0.33-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.33-2
- Perl mass rebuild

* Mon Apr 04 2011 Marcela Mašláňová <mmaslano@redhat.com> 0.33-1
- Specfile autogenerated by cpanspec 1.79.
- apply patch to automatically create alias -> DP on Data::Peek
