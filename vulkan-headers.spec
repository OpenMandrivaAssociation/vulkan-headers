%define	oname	Vulkan-Headers

Name:		vulkan-headers
Version:	1.2.140
Release:	1
Summary:	Vulkan Header files and API registry
License:	ASL 2.0
URL:		https://github.com/KhronosGroup/Vulkan-Headers
Source0:	https://github.com/KhronosGroup/Vulkan-Headers/archive/v%{version}/%{oname}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildArch:	noarch

%description
Vulkan Header files and API registry

%prep
%autosetup -n %{oname}-%{version}

%build
%cmake \
	-G Ninja

%ninja_build

%install
%ninja_install -C build

%files
%license LICENSE.txt
%doc README.md
%{_includedir}/vulkan/
%dir %{_datadir}/vulkan/
%{_datadir}/vulkan/registry/
