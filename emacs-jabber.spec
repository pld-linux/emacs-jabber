Summary:	Minimal jabber client for Emacs
Summary(pl):	Prosty klient jabbera dla Emacsa
Name:		emacs-jabber
Version:	0.6.1
Release:	0.1
License:	GPL v2
Group:		Applications/Editors/Emacs
Source0:	http://dl.sourceforge.net/emacs-jabber/%{name}-%{version}.tar.gz
# Source0-md5:	44f4780ea0d29738111ee853293b7997
URL:		http://intellectronica.net/emac-jabber/
Requires:	emacs >= 21.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minimal jabber client for Emacs.

%description -l pl
Prosty klient jabbera dla Emacsa.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
install *.el	$RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp
install -d	$RPM_BUILD_ROOT%{_infodir}
install *.info	$RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS AUTHORS README filetransfer.txt
%{_infodir}/*.info*
%{_datadir}/emacs/site-lisp/*.el
