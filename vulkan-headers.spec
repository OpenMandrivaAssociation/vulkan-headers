%undefine _debugsource_packages
%define oname Vulkan-Headers
#define snapshot 20220115

Name:		vulkan-headers
Version:	1.4.319
Release:	%{?snapshot:1.%{snapshot}.}1
Summary:	Vulkan Header files and API registry
License:	ASL 2.0
URL:		https://github.com/KhronosGroup/Vulkan-Headers
Source0:	https://github.com/KhronosGroup/Vulkan-Headers/archive/%{?snapshot:refs/heads/main}%{!?snapshot:v%{version}/%{oname}-%{version}}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildArch:	noarch
Requires:	pkgconfig(wayland-client)
Requires:	pkgconfig(x11)
Requires:	pkgconfig(xcb)
Requires:	pkgconfig(xrandr)

%description
Vulkan Header files and API registry.

%prep
%autosetup -n %{oname}-%{?snapshot:main}%{!?snapshot:%{version}} -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%license LICENSE.md
%doc README.md
%{_includedir}/vulkan
%{_includedir}/vk_video
%{_datadir}/vulkan
%dir %{_datadir}/cmake/VulkanHeaders
%{_datadir}/cmake/VulkanHeaders/*.cmake
