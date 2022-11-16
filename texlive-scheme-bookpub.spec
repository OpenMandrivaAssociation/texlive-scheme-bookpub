Name:		texlive-scheme-bookpub
Version:	63547
Release:	1
Summary:	book publishing scheme (core LaTeX and add-ons)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/scheme-bookpub
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-bookpub.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a book publishing scheme, containing core (Lua)LaTeX
and selected additional packages likely to be useful for
non-technical book publication. It does not contain additional
fonts (different books need different fonts, and the packages
are large), nor does it contain additional mathematical or
other technical packages.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
