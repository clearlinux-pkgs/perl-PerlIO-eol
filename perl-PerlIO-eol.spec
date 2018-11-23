#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PerlIO-eol
Version  : 0.17
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/PerlIO-eol-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/PerlIO-eol-0.17.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libperlio-eol-perl/libperlio-eol-perl_0.17-1.debian.tar.xz
Summary  : 'PerlIO layer for normalizing line endings'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-PerlIO-eol-lib = %{version}-%{release}
Requires: perl-PerlIO-eol-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
normalizing line endings.  It requires Perl version 5.7.3 or later.
* Installation

%package dev
Summary: dev components for the perl-PerlIO-eol package.
Group: Development
Requires: perl-PerlIO-eol-lib = %{version}-%{release}
Provides: perl-PerlIO-eol-devel = %{version}-%{release}

%description dev
dev components for the perl-PerlIO-eol package.


%package lib
Summary: lib components for the perl-PerlIO-eol package.
Group: Libraries
Requires: perl-PerlIO-eol-license = %{version}-%{release}

%description lib
lib components for the perl-PerlIO-eol package.


%package license
Summary: license components for the perl-PerlIO-eol package.
Group: Default

%description license
license components for the perl-PerlIO-eol package.


%prep
%setup -q -n PerlIO-eol-0.17
cd ..
%setup -q -T -D -n PerlIO-eol-0.17 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/PerlIO-eol-0.17/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-PerlIO-eol
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-PerlIO-eol/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/PerlIO/eol.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PerlIO::eol.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/PerlIO/eol/eol.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-PerlIO-eol/LICENSE
