#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-PerlIO-eol
Version  : 0.17
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/PerlIO-eol-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/PerlIO-eol-0.17.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libperlio-eol-perl/libperlio-eol-perl_0.17-1.debian.tar.xz
Summary  : 'PerlIO layer for normalizing line endings'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-PerlIO-eol-license = %{version}-%{release}
Requires: perl-PerlIO-eol-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
normalizing line endings.  It requires Perl version 5.7.3 or later.
* Installation

%package dev
Summary: dev components for the perl-PerlIO-eol package.
Group: Development
Provides: perl-PerlIO-eol-devel = %{version}-%{release}
Requires: perl-PerlIO-eol = %{version}-%{release}

%description dev
dev components for the perl-PerlIO-eol package.


%package license
Summary: license components for the perl-PerlIO-eol package.
Group: Default

%description license
license components for the perl-PerlIO-eol package.


%package perl
Summary: perl components for the perl-PerlIO-eol package.
Group: Default
Requires: perl-PerlIO-eol = %{version}-%{release}

%description perl
perl components for the perl-PerlIO-eol package.


%prep
%setup -q -n PerlIO-eol-0.17
cd %{_builddir}
tar xf %{_sourcedir}/libperlio-eol-perl_0.17-1.debian.tar.xz
cd %{_builddir}/PerlIO-eol-0.17
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/PerlIO-eol-0.17/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-PerlIO-eol
cp %{_builddir}/PerlIO-eol-0.17/LICENSE %{buildroot}/usr/share/package-licenses/perl-PerlIO-eol/62ce230ce8facdd09910ddaa2ba5a1b59e906c95
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-PerlIO-eol/4ed81cda73b4be0e220be7d5fb11baf974e9cf8c
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PerlIO::eol.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-PerlIO-eol/4ed81cda73b4be0e220be7d5fb11baf974e9cf8c
/usr/share/package-licenses/perl-PerlIO-eol/62ce230ce8facdd09910ddaa2ba5a1b59e906c95

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/PerlIO/eol.pm
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/auto/PerlIO/eol/eol.so
