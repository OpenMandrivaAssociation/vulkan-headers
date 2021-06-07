%define	oname	Vulkan-Headers

Name:		vulkan-headers
Version:	1.2.180
Release:	1
Summary:	Vulkan Header files and API registry
License:	ASL 2.0
URL:		https://github.com/KhronosGroup/Vulkan-Headers
Source0:	https://github.com/KhronosGroup/Vulkan-Headers/archive/v%{version}/%{oname}-%{version}.tar.gz
Patch0:		https://github.com/KhronosGroup/Vulkan-Headers/commit/cd913e84a81dd9b4e35aad4b10c2388f6f034063.patch
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
mkdir -p %{buildroot}%{_includedir}/vk_video
mv *.h %{buildroot}%{_includedir}/vk_video/

%files
%license LICENSE.txt
%doc README.md
%{_includedir}/vulkan/
%{_includedir}/vk_video/
%dir %{_datadir}/vulkan/
%{_datadir}/vulkan/registry/
