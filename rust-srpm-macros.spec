Name:           rust-srpm-macros
Version:        4
Release:        2%{?dist}
Summary:        RPM macros for building Rust source packages

License:        MIT
URL:            https://pagure.io/fedora-rust/rust2rpm
Source0:        https://releases.pagure.org/fedora-rust/rust2rpm/rust2rpm-%{version}.tar.xz

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n rust2rpm-%{version}

%install
install -D -p -m 0644 -t %{buildroot}%{_rpmconfigdir}/macros.d data/macros.rust-srpm

%files
%license LICENSE
%{_rpmconfigdir}/macros.d/macros.rust-srpm

%changelog
* Sat Jul 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4-2
- Include license

* Fri Jul 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4-1
- Update to 4

* Tue Jun 13 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3-1
- Initial package
