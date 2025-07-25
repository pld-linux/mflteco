Summary:	Infamous TECO - Editor From Hell
Summary(pl.UTF-8):	Niesławny TECO - Edytor z Piekła Rodem
Name:		mflteco
Version:	36
Release:	1
License:	distributable
Group:		Applications/Editors
Source0:	http://catb.org/~esr/retro/%{name}.tar.gz
# Source0-md5:	78ad88889d98e0c420a4863b4d22ec7a
Source1:	real.programmers.html
Patch0:		%{name}-config.patch
URL:		http://catb.org/~esr/retro/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yes, it's the Editor From Hell... the infamous TECO, bane of lusers
and tricky, unforgiving tool of master hackers. Install this to find
out (a) what we lived with before Emacs, and (b) how expressive line
noise can be. This is Sander Van Malsen's ANSIfied version of TECO for
Ultrix.

%description -l pl.UTF-8
Taaa... to edytor z piekła rodem, niesławny TECO, postrach luserów i
tajemne, niewybaczające narzędzie Wielkich Hakerów. Zainstaluj to by
przekonać się (a) jak wyglądało życie przed Emacsem, oraz (b) jak
wymowny może być biały szum. To zANSIfizowana przez Sander Van Malse'a
wersja TECO dla Ultrixa.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%{__make} CC="%{__cc}" CDF="%{rpmcflags}" -f Makefile.sunv te
mv -f te teco
cp -f %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install teco $RPM_BUILD_ROOT%{_bindir}

mv -f .tecorc sample_tecorc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  00README pi.tec real.programmers.html sample_tecorc teco.doc teco.doc.1 tecorc.mch
%attr(755,root,root) %{_bindir}/teco
