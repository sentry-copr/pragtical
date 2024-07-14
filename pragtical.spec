%bcond_without  luajit

%global         widget_commit   a5f14c250c47b6b3a62ff8888e2b4858bb32964e

Name:           pragtical
Version:        3.4.1
Release:        1%{?dist}
Summary:        practical and pragmatic code editor.

License:        MIT
URL:            https://github.com/pragtical/pragtical
Source0:        https://github.com/pragtical/pragtical/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/pragtical/widget/archive/%{widget_commit}.tar.gz#/%{name}-widget-%{widget_commit}.tar.gz

BuildRequires: gcc
BuildRequires: meson
%if %{with luajit}
BuildRequires: pkgconfig(luajit)
%else
BuildRequires: (pkgconfig(lua) >= 5.4 with pkgconfig(lua) < 5.5)
%endif
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(uchardet)
BuildRequires: desktop-file-utils

%description
Pragtical is a code editor which was forked from Lite XL (also a
fork of lite) written mostly in Lua with a focus on been practical
rather than minimalist.

%prep
%autosetup -a 1

rmdir data/widget
mv widget-%{widget_commit} data/widget

%build
%meson \
    -Duse_system_lua=true \
    -Dextra_colors=false \
    -Dextra_languages=false \
%if %{with luajit}
    -Djit=true \
%else
    -Djit=false \
%endif
    -Dppm=false \
    -Darch_tuple=%{_arch}-linux

%meson_build

%install
%meson_install

%files
%{_bindir}/pragtical
%{_datadir}/pragtical
%{_datadir}/icons/hicolor/scalable/apps/pragtical.svg
%{_datadir}/applications/org.pragtical.pragtical.desktop
%{_metainfodir}/org.pragtical.pragtical.appdata.xml
%license LICENSE
%{_docdir}/pragtical/licenses.md

%changelog
* Sun Jul 14 2024 Jan200101 <sentrycraft123@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Fri Feb 23 2024 Jan Drögehoff <sentrycraft123@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Fri Oct 13 2023 Jan Drögehoff <sentrycraft123@gmail.com> - 3.1.2-1
- Update to 3.1.2

* Fri Sep 08 2023 Jan Drögehoff <sentrycraft123@gmail.com> - 3.1.1-1
- Initial spec

