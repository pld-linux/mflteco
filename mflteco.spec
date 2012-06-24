Summary:	Infamous TECO - Editor From Hell
Summary(pl):	Nies�awny TECO - Edytor z Piek�a Rodem
Name:		mflteco
Version:	36
Release:	1
Copyright:	Distributable
Group:		Applications/Editors	
Group(pl):	Aplikacje/Edytory	
Source0:	mflteco.tar.gz
Source1:	real.programmers.html
Patch0:		mflteco-config.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
Yes, it's the Editor From Hell... the infamous TECO, bane of lusers and
tricky, unforgiving tool of master hackers. Install this to find out (a)
what we lived with before Emacs, and (b) how expressive line noise can
be.  This is Sander Van Malsen's ANSIfied version of TECO for Ultrix.

%description -l pl
Taaa... to edytor z piek�a, nies�awny TECO, postrach luser�w i tajemne,
niewybaczaj�ce narz�dzie Wielkich Haker�w. Zainstaluj to by przekona�
si� (a) jak wygl�da�o �ycie przed Emacsem, oraz (b) jak wymowny
mo�e by� bua�y szum. To zANSIfizowana przez Sander Van Malse'a 
wersja TECO dla Ultrixa.

%prep
%setup  -q -n mflteco
%patch0 -p1

%build
make CC=gcc CDF="$RPM_OPT_FLAGS" -f Makefile.sunv te
mv te teco
strip teco
cp %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 teco $RPM_BUILD_ROOT%{_bindir}

mv .tecorc sample_tecorc
gzip -9fn 00README teco.doc teco.doc.1 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz sample_tecorc pi.tec tecorc.mch real.programmers.html

%attr(755,root,root) %{_bindir}/teco
