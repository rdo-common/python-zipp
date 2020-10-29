%global pypi_name zipp

%bcond_with tests

Name:           python-%{pypi_name}
Version:        3.4.0
Release:        1%{?dist}
Summary:        Backport of pathlib-compatible object wrapper for zip files

License:        MIT
URL:            https://github.com/jaraco/zipp
Source0:        %{pypi_source}
Patch1:         0001-Set-use_scm_version-to-True-in-setup.py.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm >= 1.15.0
BuildRequires:  python3-toml

%description
A pathlib-compatible Zipfile object wrapper. A backport of the Path object.


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A pathlib-compatible Zipfile object wrapper. A backport of the Path object.


%prep
%autosetup -n %{pypi_name}-%{version}

%build
# the metapackage setuptools_scm[toml] is not yet packaged in CentOS
# as it has been added since python-setuptools_scm-4.1.2-2 [1], and
# PowerTools repo provides python3-setuptools_scm-1.15.7-4.
# We need to add manually python3-toml as BR.
# [1] https://src.fedoraproject.org/rpms/python-setuptools_scm/c/1dcc5fa198e99e3a2e4f4d64b1e0a583829edf55?branch=master
sed -i 's/setuptools_scm\[toml\].*/setuptools_scm/' setup.cfg
%py3_build

%install
%py3_install


%if %{with tests}
%check
%{__python3} setup.py test
%endif # with tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/__pycache__/%{pypi_name}.*
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info/

%changelog
* Fri Oct 30 2020 Joel Capitao <jcapitao@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-1
- Initial package
