%define oname Vulkan-Headers
#define snapshot 20220115

Name:		vulkan-headers
Version:	1.3.224
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Vulkan Header files and API registry
License:	ASL 2.0
URL:		https://github.com/KhronosGroup/Vulkan-Headers
Source0:	https://github.com/KhronosGroup/Vulkan-Headers/archive/%{?snapshot:refs/heads/main}%{!?snapshot:v%{version}/%{oname}-%{version}}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildArch:	noarch

%description
Vulkan Header files and API registry.

%prep
%autosetup -n %{oname}-%{?snapshot:main}%{!?snapshot:%{version}}
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%license LICENSE.txt
%doc README.md
%{_includedir}/vulkan
%{_includedir}/vk_video
%{_datadir}/vulkan
