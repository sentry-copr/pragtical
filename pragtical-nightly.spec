%global         realname pragtical
%global         build_timestamp %{lua: print(os.date("%Y%m%d"))}

%bcond_without  luajit

%global         widget_commit   db1c8cdc52f79753e14016a95ea3967fd833c388

Name:           %{realname}-nightly
Version:        nightly
Release:        %{build_timestamp}%{?dist}
Summary:        practical and pragmatic code editor.

License:        MIT
URL:            https://github.com/pragtical/pragtical
Source0:        https://github.com/pragtical/pragtical/archive/refs/heads/master.tar.gz#/%{name}-%{build_timestamp}.tar.gz
Source1:        https://github.com/pragtical/widget/archive/refs/heads/master.tar.gz#/%{name}-widget-%{build_timestamp}.tar.gz

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

Conflicts:      %{realname}

%description
Pragtical is a code editor which was forked from Lite XL (also a
fork of lite) written mostly in Lua with a focus on been practical
rather than minimalist.

%prep
%autosetup -n %{realname}-master -a 1

rmdir data/widget
mv widget-master data/widget

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
