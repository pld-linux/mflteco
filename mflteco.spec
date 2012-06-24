Summary:	Infamous TECO - Editor From Hell
Summary(pl):	Nies�awny TECO - Edytor z Piek�a Rodem
Name:		mflteco
Version:	36
Release:	1
License:	distributable
Group:		Applications/Editors
Source0:	http://www.tuxedo.org/~esr/retro/%{name}.tar.gz
Source1:	real.programmers.html
Patch0:		%{name}-config.patch
URL:		http://www.tuxedo.org/~esr/retro/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yes, it's the Editor From Hell... the infamous TECO, bane of lusers
and tricky, unforgiving tool of master hackers. Install this to find
out (a) what we lived with before Emacs, and (b) how expressive line
noise can be. This is Sander Van Malsen's ANSIfied version of TECO for
Ultrix.

%description -l pl
Taaa... to edytor z piek�a, nies�awny TECO, postrach luser�w i
tajemne, niewybaczaj�ce narz�dzie Wielkich Haker�w. Zainstaluj to by
przekona� si� (a) jak wygl�da�o �ycie przed Emacsem, oraz (b) jak
wymowny mo�e by� bua�y szum. To zANSIfizowana przez Sander Van Malse'a
wersja TECO dla Ultrixa.

%prep
%setup -q -n mflteco
%patch0 -p1

%build
%{__make} CC=%{__cc} CDF="%{rpmcflags}" -f Makefile.sunv te
mv -f te teco
cp -f %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 teco $RPM_BUILD_ROOT%{_bindir}

mv -f .tecorc sample_tecorc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc  00README pi.tec real.programmers.html sample_tecorc teco.doc teco.doc.1 tecorc.mch 
%attr(755,root,root) %{_bindir}/teco
