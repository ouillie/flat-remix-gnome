Name: flat-remix-gnome
Version: 20211105
Release: 1
License: CC-BY-SA-4.0
Summary: Flat Remix GNOME theme
Url: https://drasite.com/flat-remix-gnome
Group: User Interface/Desktops
Source: https://github.com/daniruiz/%{name}/archive/%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch
Requires: glib2-devel, gnome-extensions-app, gnome-shell >= 40.0, gnome-shell-extension-user-theme, ImageMagick, make
BuildRequires: make

%description
Flat Remix is a GNOME Shell theme inspired by material design. It is mostly 
flat using a colorful palette with some shadows, highlights, and gradients for 
some depth.

Themes:
 • Flat Remix
 • Flat Remix Dark
 • Flat Remix Darkest
 • Flat Remix Miami
 • Flat Remix Miami Dark

Variants:
 • Full Panel: No topbar spacing

Color Variants:
 • Blue
 • Green
 • Red
 • Yellow


%prep
%setup -q

%install
%make_install

%build


%post
cd /usr/share/flat-remix-gnome
make
make install


%preun
if [ $1 == 0 ]
then
	cd /usr/share/flat-remix-gnome
	make uninstall
fi

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_datadir}/flat-remix-gnome

