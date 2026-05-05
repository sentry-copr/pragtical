%bcond_without  luajit

%global         widget_commit   73469f651b3d362b70363c59e42de358c5d199f6

Name:           pragtical
Version:        3.9.0
Release:        1%{?dist}
Summary:        practical and pragmatic code editor.

License:        MIT
URL:            https://github.com/pragtical/pragtical
Source0:        https://github.com/pragtical/pragtical/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/pragtical/widget/archive/%{widget_commit}.tar.gz#/%{name}-widget-%{widget_commit}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: meson
%if %{with luajit}
BuildRequires: pkgconfig(luajit)
%else
BuildRequires: (pkgconfig(lua) >= 5.2 with pkgconfig(lua) < 5.5)
%endif
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(sdl3)
BuildRequires: pkgconfig(sdl3-image)
BuildRequires: pkgconfig(uchardet)
BuildRequires: desktop-file-utils

%description
Pragtical is a code editor which was forked from Lite XL (also a
fork of lite) written mostly in Lua with a focus on been practical
rather than minimalist.

%prep
%autosetup -a 1

mv widget-%{widget_commit} data/widget

%build
%meson \
    -Duse_system_lua=true \
    -Drepl_history=false \
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
%{_datadir}/applications/dev.pragtical.Pragtical.desktop
%{_metainfodir}/dev.pragtical.Pragtical.appdata.xml
%license LICENSE
%{_docdir}/pragtical/licenses.md

%changelog
* Tue May 05 2026 Jan200101 <sentrycraft123@gmail.com> - 3.9.0-1
- Update to 3.9.0

* Wed Oct 30 2024 Jan200101 <sentrycraft123@gmail.com> - 3.5.1-1
- Update to 3.5.1

* Sun Jul 14 2024 Jan200101 <sentrycraft123@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Fri Feb 23 2024 Jan Drögehoff <sentrycraft123@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Fri Oct 13 2023 Jan Drögehoff <sentrycraft123@gmail.com> - 3.1.2-1
- Update to 3.1.2

* Fri Sep 08 2023 Jan Drögehoff <sentrycraft123@gmail.com> - 3.1.1-1
- Initial spec

